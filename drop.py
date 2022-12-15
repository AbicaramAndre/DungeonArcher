from PPlay.sprite import *
from PPlay.animation import *
from random import randint

def drop_vida(inimigo,lista_vida):
    prob=randint(0,100)
    if prob < 20:
        print("dropou")
        temp_vida=Sprite("sprites/Pixilart Sprite Sheet.png",2)
        temp_vida.x=inimigo.x+inimigo.width/2-temp_vida.width/2
        temp_vida.y=inimigo.y+inimigo.height/2-temp_vida.height/2
        temp_vida.set_total_duration(1000)
        lista_vida.append(temp_vida)
    return lista_vida


def drop_itens(inimigo,lista_itens):
   
    return lista_itens

def draw_drop(lista_vida):
    for i in range(len(lista_vida)):
        lista_vida[i].draw()
        lista_vida[i].update()
