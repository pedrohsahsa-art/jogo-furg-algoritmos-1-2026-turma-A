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
mira = ar.Linha(inicio=inicio_mira, fim=fim_mira, cor="preto", espessura=4)
angulo = mat.atan2(fim_mira.y - inicio_mira.y,fim_mira.x - inicio_mira.x)

def mouse_track(posição):
    global fim_mira, angulo
    fim_mira.x = posição.x
    fim_mira.y = posição.y
    vetor_x = fim_mira.x - inicio_mira.x
    vetor_y = fim_mira.y - inicio_mira.y
    tamanho_vetor = mat.sqrt(vetor_x**2 + vetor_y**2)
    fim_mira.x = inicio_mira.x + (vetor_x / tamanho_vetor) * 75
    fim_mira.y = inicio_mira.y + (vetor_y / tamanho_vetor) * 75
    mira.fim = fim_mira
    if tamanho_vetor == 0:
        return
    if len(projeteis) == 0:
        atualizar_angulo()

#projetil
velocidade_projetil = 5
projeteis = []

def atualizar_angulo():
    global angulo
    angulo = mat.atan2(fim_mira.y - inicio_mira.y,fim_mira.x - inicio_mira.x)

def tiro(tiro):
    global angulo,fim_mira
    if len(projeteis) == 0:
        projetil = ar.Circulo(ar.Ponto(fim_mira.x, fim_mira.y), 5, cor="preto")
        projeteis.append(projetil)
        tela.adicionar(projetil)
        print (angulo)
        return True        

def atualizar():
    for projetil in projeteis:
        dx = velocidade_projetil * mat.cos(angulo)
        dy = velocidade_projetil * mat.sin(angulo)
        projetil.mover(dx, dy)
        saiu_da_tela = (projetil.y > tamanho_tela_y or projetil.y < 0 or projetil.x > tamanho_tela_x or projetil.x < 0)
        if saiu_da_tela:
            tela.remover(projetil)
            projeteis.remove(projetil)
            atualizar_angulo()

#ordens
tela.ao_mover_mouse(mouse_track)
tela.adicionar(corpo)
tela.adicionar(mira)
tela.ao_clicar(tiro)
tela.animar(atualizar, fps=60)
tela.executar()