def config():
    with open("tela.txt", "r", encoding="utf-8") as arquivo:
        configuracoes = {}

        for linha in arquivo:
            chave, valor = linha.strip().split("=")
            configuracoes[chave.strip()] = int(valor.strip())

    tela_x = configuracoes["tela_x"]
    tela_y = configuracoes["tela_y"]
    return tela_x,tela_y