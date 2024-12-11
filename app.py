import cv2
import mediapipe as mp
import time
import numpy as np
from IPython.display import display, clear_output
from PIL import Image

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

# Inicialização do vídeo
video_path = 'caminho_do_video.mp4'
cap = cv2.VideoCapture(video_path)

# Funções auxiliares
def detectar_kimono_cor(frame_hsv):
    azul_baixo = np.array([100, 150, 50])
    azul_alto = np.array([140, 255, 255])
    branco_baixo = np.array([0, 0, 200])
    branco_alto = np.array([180, 30, 255])
    mask_azul = cv2.inRange(frame_hsv, azul_baixo, azul_alto)
    mask_branco = cv2.inRange(frame_hsv, branco_baixo, branco_alto)
    atleta_azul = cv2.countNonZero(mask_azul) > 1000
    atleta_branco = cv2.countNonZero(mask_branco) > 1000
    return atleta_azul, atleta_branco

def desenhar_status(frame, pegada_azul, pegada_branco):
    cv2.putText(frame, f'Pegada Azul: {"Ativa" if pegada_azul else "Inativa"}', 
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Pegada Branco: {"Ativa" if pegada_branco else "Inativa"}', 
                (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Processamento do vídeo
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro ao ler frame.")
        break

    # Converter para RGB e HSV
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Detectar cor dos kimonos
    atleta_azul, atleta_branco = detectar_kimono_cor(frame_hsv)
    
    # Processar o quadro para detecção de mãos
    results = hands.process(frame_rgb)

    # Obter tempo atual
    tempo_atual = time.time()

    # Verificar se há mãos detectadas
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Atualizar status e exibir o frame no Jupyter
    desenhar_status(frame, atleta_azul, atleta_branco)
    clear_output(wait=True)
    display(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))

cap.release()