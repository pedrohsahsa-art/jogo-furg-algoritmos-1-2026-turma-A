import aroeira
import configurações

tela_x, tela_y = configurações.config()

botão_largura = 300


def opcao_hitbox(ponto, botao):
    return (botao.origem.x <= ponto.x <= botao.origem.x + botao.largura and botao.origem.y <= ponto.y <= botao.origem.y + botao.altura)


def clicar(ponto):
    print(ponto.x, ponto.y)
    if (opcao_hitbox(ponto, placeholder_botão) or opcao_hitbox(ponto, placeholder_botão2)):
        tela.remover(placeholder_botão)
        tela.remover(placeholder_botão2)
        tela.fechar("Teste")
    


tela = aroeira.Tela("PEEGLE", altura=tela_y, largura=tela_x)
placeholder_botão = aroeira.Retangulo(origem=(aroeira.Ponto(((tela_x/2)-(botão_largura/2)),tela_y/2)),largura=botão_largura, cor="azul")
placeholder_botão2 = aroeira.Retangulo(origem=(aroeira.Ponto(((tela_x/2)-(botão_largura/2)),(tela_y/2+botão_largura/2))),largura=botão_largura, cor="azul")

placeholder_background = aroeira.Retangulo(origem=(aroeira.Ponto(00,00)),largura=tela_x,altura=tela_y)

tela.adicionar(placeholder_background)
tela.adicionar(placeholder_botão)
tela.adicionar(placeholder_botão2)

tela.ao_clicar(clicar)



tela.executar(tela_cheia=True)