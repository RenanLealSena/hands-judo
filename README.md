### README.md

# Judô Pegada Tracking

Este projeto utiliza o **MediaPipe**, **OpenCV**, e o **Filtro Kalman** para rastrear as pegadas de dois atletas em um vídeo de judô. Ele determina qual atleta (vestindo kimono azul ou branco) mantém a pegada no adversário por mais tempo.

---

## 📋 **Funcionalidades**

1. **Rastreamento de Mãos com MediaPipe**  
   Detecta e rastreia as mãos dos atletas em tempo real usando a biblioteca MediaPipe.

2. **Filtro Kalman para Suavização**  
   Usa o Filtro Kalman para suavizar as posições detectadas das mãos e prever movimentos.

3. **Detecção de Cor dos Kimonos**  
   Identifica os atletas com base na cor do kimono (azul ou branco) para associar a pegada ao atleta correto.

4. **Análise de Pegada**  
   Determina o vencedor da pegada se o atleta segurar por mais de 7 segundos consecutivos.

5. **Visualização em Tempo Real**  
   Mostra os status das pegadas ("Ativa" ou "Inativa") diretamente no vídeo, além de imprimir o vencedor no terminal.

---

## 📜 **Dependências**

- [OpenCV](https://opencv.org/)  
- [MediaPipe](https://mediapipe.dev/)  
- [NumPy](https://numpy.org/)  
- [Colorama](https://pypi.org/project/colorama/)

---

## 🛠️ **Instalação**

1. Clone este repositório:
   ```bash
   git clone https://github.com/RenanLealSena/hands-judo.git
   cd judo-pegada-tracking
   ```

2. Instale os pacotes necessários:
   ```bash
   pip install opencv-python
   pip install mediapipe
   pip install numpy
   pip install colorama
   ```

3. Certifique-se de ter um vídeo no caminho `caminho_do_video.mp4` ou atualize a variável `video_path` no código.

---

## ▶️ **Como Executar**

1. Certifique-se de que todas as dependências estão instaladas.
2. Execute o script:
   ```bash
   python app.py
   ```
3. Para sair da visualização do vídeo, pressione `q`.

---

## 📂 **Estrutura do Código**

- **Detecção de Mãos (MediaPipe)**  
  Rastreia as mãos dos atletas e mapeia suas posições para determinar pegadas.

- **Filtro Kalman**  
  Usado para suavizar a detecção de movimentos e prever a posição futura das mãos.

- **Verificação de Pegadas**  
  Analisa o tempo contínuo da pegada e determina o vencedor com base na duração mínima de 7 segundos.

- **Detecção de Cores (HSV)**  
  Identifica os atletas com base na cor do kimono:
  - Azul: `[100, 150, 50]` a `[140, 255, 255]`
  - Branco: `[0, 0, 200]` a `[180, 30, 255]`

---

## 🔧 **Configuração e Personalização**

- **Ajustar o tempo mínimo de pegada**  
  Altere o valor `7` na função `verificar_pegada()` para modificar o tempo necessário para determinar o vencedor.

- **Configuração de tolerância para desaparecimento**  
  A variável `tolerancia_desaparecimento` define o tempo máximo sem detecção antes de considerar a pegada como perdida.

- **Caminho do vídeo**  
  Atualize a variável `video_path` com o caminho do seu vídeo personalizado.

---

# Caso Esteja No Jupyter Notebook


## 📜 **Dependências**

Certifique-se de ter o Python 3.x instalado em seu sistema, junto com as bibliotecas necessárias. Para isso, utilize o comando abaixo para instalar os pacotes necessários:

- [OpenCV](https://opencv.org/)  
- [MediaPipe](https://mediapipe.dev/)  
- [NumPy](https://numpy.org/)  
- [Ipython](https://ipython.org/)
- [Pillow](https://pypi.org/project/pillow/)
- [Colorama](https://pypi.org/project/colorama/)

---

## 🛠️ **Instalação**

1. Clone este repositório:
   ```bash
   git clone https://github.com/RenanLealSena/hands-judo.git
   cd judo-pegada-tracking
   ```

2. Instale os pacotes necessários:

   ```bash
   !pip install opencv-python 
   !pip install mediapipe 
   !pip install numpy 
   !pip install ipython 
   !pip install pillow 
   !pip install colorama
   ```

3. Certifique-se de ter um vídeo no caminho `caminho_do_video.mp4` ou atualize a variável `video_path` no código.

---

# 📈 **Futuras Melhorias**

- Adicionar suporte a mais cores de kimono.  
- Implementar visualizações gráficas do tempo de pegada.  
- Otimizar o uso do Filtro Kalman para múltiplas mãos simultaneamente.

---



## 🏆 **Licença**

Este projeto é livre para uso e modificação, sujeito aos termos da [MIT License](LICENSE).

---
