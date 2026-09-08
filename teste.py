import aroeira as ar
import math as mat
import random as rd

#tela
#(fazer resoluções selecionaveis no menu e linkar aqui)
tamanho_tela_x = 1400
tamanho_tela_y = 800
tela = ar.Tela("pegking", tamanho_tela_x, tamanho_tela_y, "cinza")

#tentativa do lançador
corpo = ar.Circulo(ar.Ponto(tamanho_tela_x // 2,0),75,"vermelho")
inicio_mira = ar.Ponto(tamanho_tela_x // 2,0)
fim_mira = ar.Ponto(tamanho_tela_x // 2,75)
mira = ar.Linha(inicio = inicio_mira, fim = fim_mira , cor = "preto", espessura = 4)

def desenha_linha():
    global fim_mira
    fx = inicio_mira.x+mat.sin()*75
    fy = inicio_mira.y+mat.cos()*75
    fim_mira = ar.Ponto(fx,fy)
    mira = ar.Linha(inicio = inicio_mira, fim = fim_mira , cor = "preto", espessura = 4)

#def clicou(ponto):
#    global fim_mira
#    fim_mira.x = ponto.x
#    fim_mira.y = ponto.y

#projetil
velocidade_projetil = 5
angulo = 0
projeteis = []

def troca_angulo(d_ang):
     global angulo, projeteis
     if len(projeteis) > 0:
          return False
     angulo+= d_ang

def tiro(tiro):
    global angulo,fim_mira
    if tiro == ' ':
        projetil = ar.Circulo(ar.Ponto(fim_mira.x, fim_mira.y), 5, cor="preto")
        if len(projeteis) == 0:
            projeteis.append(projetil)
            tela.adicionar(projetil)
            return True
        

def atualizar():
    for projetil in projeteis:
        dx = velocidade_projetil*mat.sin(mat.radians(angulo))
        dy = velocidade_projetil*mat.cos(mat.radians(angulo))
        projetil.mover(dx, dy)
        if projetil.y > tamanho_tela_y or projetil.x > tamanho_tela_x:
            tela.remover(projetil)
            projeteis.remove(projetil)

#ordens
tela.ao_clicar(desenha_linha)
tela.adicionar(corpo)
tela.adicionar(mira)
tela.ao_pressionar_tecla(tiro)
tela.animar(atualizar, fps=60)
tela.executar()