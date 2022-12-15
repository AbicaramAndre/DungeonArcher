from PPlay.gameimage import GameImage
from PPlay.window import*
from PPlay.sprite import *
from random import randint

pedras_verde="sprites/objetos/pedra_verde_1.png"
detalhe_chao="sprites/objetos/detalhe_chao.png"

def rand_bg(N):
    bg=[]
    janela=(830,500)
    for i in range(N):
        pedra_temp=Sprite(pedras_verde,1)
        pedra_temp.x=randint(30,janela[0]-pedra_temp.width)
        pedra_temp.y=randint(30,janela[1]-pedra_temp.height)
        bg.append(pedra_temp)
    return bg
def rand_chao(N):
    chao=[]
    janela=(830,500)
    for i in range(N):
        pedra_temp=Sprite(detalhe_chao,1)
        pedra_temp.x=randint(30,janela[0]-pedra_temp.width)
        pedra_temp.y=randint(30,janela[1]-pedra_temp.height)
        chao.append(pedra_temp)
    return chao

def draw_chao(chao):
    for i in range(len(chao)):
        chao[i].draw()

def draw_bg(bg):
    for i in range(len(bg)):
        bg[i].draw()
