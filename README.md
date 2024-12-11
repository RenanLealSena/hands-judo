README.md

Analisador de Pegadas de Judô com Rastreamento de Mãos

Este projeto utiliza OpenCV, MediaPipe e NumPy para analisar vídeos de judô e detectar a presença de pegadas entre atletas com base no rastreamento de mãos e na identificação da cor dos kimonos (azul ou branco).

Funcionalidades
	•	Identificação de Atletas: Detecta os kimonos azul e branco usando máscaras HSV.
	•	Rastreamento de Mãos: Utiliza MediaPipe para rastrear as mãos em tempo real.
	•	Análise de Pegada: Monitora o tempo que os atletas permanecem ativos e identifica pegadas ativas.
	•	Exibição Visual: Mostra as mãos detectadas e o status das pegadas diretamente no vídeo.
	•	Integração com Jupyter Notebook: Exibe os quadros processados no ambiente do Jupyter Notebook.

Configuração do Ambiente

Pré-requisitos
	•	Python 3.7+
	•	Bibliotecas:
	•	opencv-python
	•	mediapipe
	•	numpy
	•	pillow
	•	jupyter (opcional, se for rodar em Jupyter Notebook)

Instalação
	1.	Clone o repositório:

git clone https://github.com/seu-usuario/nome-do-repositorio.git


	2.	Entre no diretório do projeto:

cd nome-do-repositorio


	3.	Instale as dependências:

pip install opencv-python mediapipe numpy pillow


	4.	(Opcional) Instale o Jupyter Notebook:

pip install notebook

Como usar
	1.	Insira o caminho do vídeo na variável video_path:

video_path = 'caminho/do/video.mp4'


	2.	Execute o script em um ambiente Python ou Jupyter Notebook:

python app.py

Ou, se estiver usando Jupyter Notebook, execute as células no arquivo .ipynb.

	3.	Durante a execução, o vídeo será processado quadro a quadro e exibido na saída do Jupyter Notebook.

Personalização
	•	Intervalos de Cor: Ajuste os valores HSV nas variáveis azul_baixo, azul_alto, branco_baixo e branco_alto para detectar diferentes cores de kimonos.
	•	Tolerância de Desaparecimento: Modifique a variável tolerancia_desaparecimento para ajustar o tempo que um atleta pode ficar sem ser detectado antes de considerar que não está mais ativo.

Estrutura do Código

Principais Componentes
	•	Configuração do MediaPipe: Configura o rastreamento de mãos para processar quadros do vídeo.
	•	Função detectar_kimono_cor: Detecta as cores azul e branca nos quadros usando máscaras HSV.
	•	Função desenhar_status: Exibe o status das pegadas (ativa ou inativa) no vídeo.
	•	Loop Principal: Processa o vídeo quadro a quadro, detecta as mãos e atualiza os estados dos atletas.

Saídas

No Jupyter Notebook
	•	Os quadros do vídeo são exibidos com:
	•	Rastreamento de Mãos: Posições das mãos destacadas com landmarks.
	•	Status das Pegadas: Indicadores de “Ativa” ou “Inativa” para os atletas azul e branco.

No Terminal
	•	Mensagens de erro ou fim de vídeo são exibidas no terminal.

Contribuições

Contribuições são bem-vindas! Envie melhorias, correções ou ideias através de pull requests.

Licença

Este projeto é distribuído sob a licença MIT.