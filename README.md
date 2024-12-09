# Análise de Lutas de Judô com Detecção de Mãos e Quimono

Este projeto é um programa que utiliza o OpenCV, MediaPipe e Imutils para analisar vídeos de lutas de judô, detectando os quimonos dos atletas e determinando quem realizou uma pegada por mais de 7 segundos.

## Funcionalidades

- **Detecção de Mãos**: Usa o MediaPipe para detectar e rastrear mãos nos frames do vídeo.
- **Detecção de Quimono**: Identifica os quimonos dos atletas com base em sua cor (azul ou branco).
- **Análise de Pegada**: Calcula o tempo que cada atleta mantém a pegada e identifica o primeiro a manter por mais de 7 segundos.
- **Exibição de Resultados**: Exibe o vídeo com detecção em tempo real e imprime no terminal o atleta que fez a pegada primeiro.

## Pré-requisitos

Certifique-se de ter os seguintes pacotes instalados:

- Python 3.7 ou superior
- OpenCV
- MediaPipe
- Imutils

Para instalar as dependências, execute:

```bash
pip install opencv-python mediapipe imutils
```

## Estrutura do Código

- **`detect_quimono(frame, lower_color, upper_color)`**: Detecta um quimono em um frame com base em um intervalo de cores em HSV.
- **`track_pegada(first_pegada_start, threshold=7)`**: Verifica se o tempo da pegada ultrapassou o limite de 7 segundos.
- **`analyze_judo_fight(video_path)`**: Função principal que analisa o vídeo e determina o atleta que fez a melhor pegada.

## Como Usar

1. Coloque o vídeo da luta em um local acessível.
2. Substitua o caminho do vídeo no código pelo caminho do seu arquivo:

   ```python
   video_path = 'caminho_para_o_video_da_luta.mp4'
   ```

3. Execute o script:

   ```bash
   python app.py
   ```

4. O vídeo será exibido com as detecções. Para sair da análise, pressione a tecla `q`.

## Configurações

### Intervalos de Cores
Os intervalos de cores para quimonos estão definidos no formato HSV. Caso precise ajustar:

```python
lower_blue = (100, 150, 0)
upper_blue = (140, 255, 255)

lower_white = (0, 0, 200)
upper_white = (180, 25, 255)
```

### Tempo de Pegada
Por padrão, o tempo mínimo para determinar uma pegada bem-sucedida é de 7 segundos. Você pode alterar o valor na função `track_pegada`:

```python
threshold=7
```

## Observações

- Certifique-se de que o vídeo possui qualidade suficiente para detectar as mãos e os quimonos.
- A configuração das cores pode precisar de ajustes dependendo das condições de iluminação do vídeo.

## Licença

Este projeto é de código aberto e está disponível sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.

---