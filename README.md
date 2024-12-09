### README.md

# Analisador de Pegadas de Judô

Este projeto utiliza **OpenCV**, **MediaPipe** e **Colorama** para analisar vídeos de judô e determinar qual atleta mantém a pegada ativa por mais de 7 segundos. Os atletas são identificados pela cor do kimono (azul ou branco).

---

## Funcionalidades

- **Identificação dos Atletas:** Detecta a cor dos kimonos (azul e branco) no vídeo.  
- **Detecção de Mãos:** Usa MediaPipe para rastrear as mãos de ambos os atletas.  
- **Análise de Pegada:** Calcula o tempo em que cada atleta mantém a pegada ativa.  
- **Filtro Kalman:** Suaviza os movimentos para maior precisão na análise.  
- **Exibição do Vencedor:** Indica no terminal qual atleta manteve a pegada ativa por mais tempo.  

---

## Configuração do Ambiente

### Pré-requisitos
- **Python 3.7+**  
- Bibliotecas:
  - `opencv-python`
  - `mediapipe`
  - `numpy`
  - `colorama`

### Instalação
1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Instale as dependências:  
   ```bash
   pip install opencv-python mediapipe numpy colorama
   ```

---

## Como usar

1. Insira o caminho do vídeo na variável `video_path`:
   ```python
   video_path = 'assets/videos/test_0.mp4'
   ```

2. Execute o script:
   ```bash
   python main.py
   ```

3. O vídeo será exibido com informações sobre o status das pegadas. O terminal indicará o vencedor com cores específicas:
   - **Azul:** Atleta azul ganhou a pegada!  
   - **Vermelho:** Atleta branco ganhou a pegada!  

4. Pressione **Q** para sair.

---

## Estrutura do Código

### Módulos Principais
- **Detecção de Cor:** Identifica as cores azul e branca no quadro usando máscaras HSV.  
- **Rastreamento de Mãos:** Detecta e desenha landmarks das mãos dos atletas.  
- **Análise de Pegada:** Verifica se a pegada foi mantida por mais de 7 segundos.  
- **Exibição de Informações:** Mostra o status das pegadas na tela e no terminal.  

### Personalização
- **Intervalos de Cor:** Ajuste os intervalos HSV na função `detectar_kimono_cor` para outras cores.  
- **Tempo da Pegada:** Modifique o valor `7` na função `verificar_pegada` para alterar a duração necessária.  

---

## Saídas

### Na Tela
O status das pegadas é exibido no canto superior esquerdo:  
- **Pegada Azul:** Ativa ou Inativa.  
- **Pegada Branco:** Ativa ou Inativa.  

### No Terminal
Mensagens indicam o vencedor com cores diferentes:
- **Azul:**  
  ```text
  Atleta azul ganhou a pegada!
  ```
- **Vermelho:**  
  ```text
  Atleta branco ganhou a pegada!
  ```

---

## Contribuições
Contribuições são bem-vindas! Envie melhorias, correções ou ideias através de pull requests.

---

## Licença
Este projeto é distribuído sob a licença [MIT](LICENSE).  