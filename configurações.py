import os

def config():
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho_tela = os.path.join(diretorio, "tela.txt")
    with open(caminho_tela, "r") as arquivo:
        configuracoes = {}

        for linha in arquivo:
            chave, valor = linha.strip().split("=")
            configuracoes[chave.strip()] = int(valor.strip())

    tela_x = configuracoes["tela_x"]
    tela_y = configuracoes["tela_y"]
    return tela_x,tela_y