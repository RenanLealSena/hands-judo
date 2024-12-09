import cv2
import mediapipe as mp
import time
import numpy as np
from colorama import Fore, Back, Style

# Configuração da detecção de mãos MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Variáveis de controle
pegada_azul = False
pegada_branco = False
tempo_inicio_azul = 0
tempo_inicio_branco = 0
tempo_desaparecido_azul = 0
tempo_desaparecido_branco = 0
tolerancia_desaparecimento = 2 
vencedor = None 

# Variáveis do Filtro Kalman para suavizar e prever movimentos
kalman_filter_azul = cv2.KalmanFilter(4, 2)  # 4 estados, 2 medições (x, y)
kalman_filter_branco = cv2.KalmanFilter(4, 2)

# Inicializar parâmetros do Kalman Filter
def inicializar_kalman(kf):
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
    kf.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03

inicializar_kalman(kalman_filter_azul)
inicializar_kalman(kalman_filter_branco)

# Função para atualizar o Filtro Kalman
def atualizar_kalman(kf, x, y):
    medicao = np.array([[np.float32(x)], [np.float32(y)]])
    kf.correct(medicao)
    predicao = kf.predict()
    return int(predicao[0]), int(predicao[1])

# Função para verificar se a pegada está ativa por mais de 7 segundos
def verificar_pegada(tempo_inicio, tempo_atual):
    return (tempo_atual - tempo_inicio) >= 7

# Função para desenhar o status da pegada na tela
def desenhar_status(frame, pegada_azul, pegada_branco):
    texto_azul = f'Pegada Azul: {"Ativa" if pegada_azul else "Inativa"}'
    texto_branco = f'Pegada Branco: {"Ativa" if pegada_branco else "Inativa"}'
    cv2.putText(frame, texto_azul, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, texto_branco, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Função para detectar as cores dos kimonos (azul e branco)
def detectar_kimono_cor(frame_hsv, frame):
    # Definindo os intervalos de cores em HSV para o azul e branco
    azul_baixo = np.array([100, 150, 50])
    azul_alto = np.array([140, 255, 255])

    branco_baixo = np.array([0, 0, 200])
    branco_alto = np.array([180, 30, 255])

    # Máscara para a cor azul
    mask_azul = cv2.inRange(frame_hsv, azul_baixo, azul_alto)
    mask_branco = cv2.inRange(frame_hsv, branco_baixo, branco_alto)

    # Verificar se há grandes áreas azuis ou brancas no quadro
    atleta_azul = cv2.countNonZero(mask_azul) > 1000
    atleta_branco = cv2.countNonZero(mask_branco) > 1000

    return atleta_azul, atleta_branco

# Abrir vídeo
video_path = 'assets/videos/test_0.mp4' 
cap = cv2.VideoCapture(video_path)

# Verificar se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro ao ler frame.")
        break
    
    # Converter para RGB e HSV
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Detectar cor dos kimonos
    atleta_azul, atleta_branco = detectar_kimono_cor(frame_hsv, frame)
    
    # Processar o quadro para detecção de mãos
    results = hands.process(frame_rgb)

    # Obter tempo atual
    tempo_atual = time.time()

    # Verificar se há mãos detectadas
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Pegando o ponto 9 da mão (landmark no punho) para determinar a posição
            x_punho = int(hand_landmarks.landmark[9].x * frame.shape[1])
            y_punho = int(hand_landmarks.landmark[9].y * frame.shape[0])

            # Desenhar os pontos de landmark das mãos
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Verificar se a mão pertence ao atleta azul ou branco
            if atleta_azul:
                pegada_azul = True
                tempo_desaparecido_azul = 0  # Reseta o contador de desaparecimento
                tempo_inicio_azul = tempo_inicio_azul or tempo_atual  # Marca o tempo de início da pegada

                # Atualizar o filtro Kalman com a posição atual
                pred_azul_x, pred_azul_y = atualizar_kalman(kalman_filter_azul, x_punho, y_punho)

            elif atleta_branco:
                pegada_branco = True
                tempo_desaparecido_branco = 0  # Reseta o contador de desaparecimento
                tempo_inicio_branco = tempo_inicio_branco or tempo_atual  # Marca o tempo de início da pegada

                # Atualizar o filtro Kalman com a posição atual
                pred_branco_x, pred_branco_y = atualizar_kalman(kalman_filter_branco, x_punho, y_punho)

    else:
        # Nenhuma mão detectada: começar a contagem do tempo de desaparecimento
        if pegada_azul:
            tempo_desaparecido_azul += 1/30  # Assumindo que o vídeo tem 30fps
            if tempo_desaparecido_azul > tolerancia_desaparecimento:
                pegada_azul = False
                tempo_inicio_azul = 0

        if pegada_branco:
            tempo_desaparecido_branco += 1/30
            if tempo_desaparecido_branco > tolerancia_desaparecimento:
                pegada_branco = False
                tempo_inicio_branco = 0

    # Verificar se a pegada foi mantida por 7 segundos
    if verificar_pegada(tempo_inicio_azul, tempo_atual) and vencedor is None:
        print(Fore.BLUE + "Atleta azul ganhou a pegada!")
        vencedor = "azul"  # Marca que o atleta azul ganhou

    if verificar_pegada(tempo_inicio_branco, tempo_atual) and vencedor is None:
        print(Fore.RED + "Atleta branco ganhou a pegada!")
        vencedor = "branco"  # Marca que o atleta branco ganhou

    # Desenhar o status das pegadas no quadro
    desenhar_status(frame, pegada_azul, pegada_branco)

    # Mostrar o vídeo
    cv2.imshow('Judô Pegada Tracking', frame)

    # Adicionar tempo de espera entre frames
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
