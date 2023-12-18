import datetime
import cv2
import time
import os


contador = 0

def captura_imagem(ret, frame):
    # Verifica se o quadro foi capturado corretamente
    if not ret:
        print("Não foi possível capturar o quadro")
        exit()

    # Obtém o diretório atual
    diretorio_atual = os.getcwd()

    # Define o nome da pasta para salvar as imagens
    nome_pasta = "imagens"

    # Caminho completo para a pasta de imagens
    caminho_pasta = os.path.join(diretorio_atual, nome_pasta)

    # Verifica se a pasta de imagens existe e, se não existir, a cria
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    # Salva o quadro em um arquivo de imagem dentro da pasta de imagens
    agora = datetime.datetime.now()
    data_hora_formatada = agora.strftime("%Y-%m-%d_%H-%M-%S")
    nome_saida = f"captura_{data_hora_formatada}.jpg"

    # Caminho completo para salvar a imagem na pasta de imagens
    caminho_saida = os.path.join(caminho_pasta, nome_saida)

    cv2.imwrite(caminho_saida, frame)

