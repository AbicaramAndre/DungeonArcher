import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

###
from PPlay.gameimage import GameImage
from PPlay.window import*
from PPlay.sprite import *
from random import randint
from gameloop import *
from rank import *##

RGB=(0,0,0)
janela = Window(800, 530)
janela.set_title("Dungeon Archer")
janela.set_background_color(RGB)
teclado = Window.get_keyboard() 
mouse=Window.get_mouse()

intro_song="sprites/01 Those Responsible.mp3"

intro_img="sprites/LAb JOgos.png"
intro=GameImage(intro_img)
dev_img="sprites/devs.png"
dev=GameImage(dev_img)
menu_img="sprites/menu.png"
menu=GameImage(menu_img)
credits="sprites/img_creditos.png"
cred=GameImage(credits)

tut=GameImage("sprites/tutorial.png")

but_sprite=["sprites/bplay.png","sprites/rank.png","sprites/bcomojogar.png","sprites/bcred.png","sprites/sair.png"]
####but play
bplay=Sprite(but_sprite[0],1)
bplay.x=janela.width/2-bplay.width/2 
bplay.y=130
#####but rank
brank=Sprite(but_sprite[1],1)
brank.x=janela.width/2-brank.width/2 
brank.y=65+130
####but how to play
bhow=Sprite(but_sprite[2],1)
bhow.x=janela.width/2-bhow.width/2 
bhow.y=130+130
#####but sair
bcred=Sprite(but_sprite[3],1)
bcred.x=janela.width/2-bcred.width/2 
bcred.y=195+130
menu_sound=pygame.mixer.Sound('sprites/05 Sacrificial.mp3')
#menu_sound.play(-1)
#####but creditos
bsair=Sprite(but_sprite[4],1)
bsair.x=janela.width/2-bsair.width/2 
bsair.y=260+130
JOGAR=False
RANK=False
HOW=False
CRED=False
SAIR=False



click= pygame.mixer.Sound('sprites/04 The Binding of Isaac Soundtrack Unknown Depths Below in HD.mp3')
intro_song=pygame.mixer.Sound(intro_song)
intro_song.play()
intro.draw()
janela.update()
time.sleep(4)
dev.draw()
janela.update()
time.sleep(4)
menu.draw()
janela.update()
time.sleep(4)
intro_song.fadeout(1000)
menu_sound.play(-1)

while(True):
    menu.draw()
    mousepos=mouse.get_position()
    bplay.draw()
    brank.draw()
    bhow.draw()
    bcred.draw()
    bsair.draw()

    if JOGAR==True:
        JOGAR=False
        x=bplay.x
        y=bplay.y
        bplay=Sprite("sprites/bplay.png")
        bplay.x=x
        bplay.y=y
    if mouse.is_over_object(bplay):
        JOGAR=True
        x=bplay.x
        y=bplay.y
        bplay=Sprite("sprites/bplay_inv.png")
        bplay.x=x
        bplay.y=y
        if mouse.is_button_pressed(1):
            print("GAME")
            menu_sound.stop()
            click.play()
            janela.set_background_color(RGB)
            janela.update()
            time.sleep(3)
            game_loop(janela)
            menu_sound.play(-1)

    if  RANK==True:
        RANK=False
        x=brank.x
        y=brank.y
        brank=Sprite("sprites/rank.png")
        brank.x=x
        brank.y=y
    if mouse.is_over_object(brank):
        RANK=True
        x=brank.x
        y=brank.y
        brank=Sprite("sprites/rank_inv.png")
        brank.x=x
        brank.y=y
        if mouse.is_button_pressed(1):
            print("RANK")
            rank(janela)
    
    if HOW==True:
        HOW=False
        x=bhow.x
        y=bhow.y
        bhow=Sprite("sprites/bcomojogar.png")
        bhow.x=x
        bhow.y=y
    if mouse.is_over_object(bhow):
        HOW=True
        x=bhow.x
        y=bhow.y
        bhow=Sprite("sprites/bcomojogar_inv.png")
        bhow.x=x
        bhow.y=y
        if mouse.is_button_pressed(1):
            while not (teclado.key_pressed("ESC")):
                tut.draw()
                janela.update()
            print("HOW TO PLAY")
        
    if CRED==True:
        CRED=False
        x=bcred.x
        y=bcred.y
        bcred=Sprite("sprites/bcred.png")
        bcred.x=x
        bcred.y=y
    if mouse.is_over_object(bcred):
        CRED=True
        x=bcred.x
        y=bcred.y
        bcred=Sprite("sprites/bcred_inv.png")
        bcred.x=x
        bcred.y=y
        if mouse.is_button_pressed(1):
            menu_sound.stop()
            cred.draw()
            janela.update()
            intro_song.play()
            time.sleep(15)
            menu_sound.play(-1)
            print("CREDITOS")
    
    if SAIR==True:
        SAIR=False
        x=bsair.x
        y=bsair.y
        bsair=Sprite("sprites/sair.png")
        bsair.x=x
        bsair.y=y
    if mouse.is_over_object(bsair):
        SAIR=True
        x=bsair.x
        y=bsair.y
        bsair=Sprite("sprites/sair_inv.png")
        bsair.x=x
        bsair.y=y
        if mouse.is_button_pressed(1):  
            print("SAIR")
            janela.close()

    janela.update()
