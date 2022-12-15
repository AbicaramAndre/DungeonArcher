from PPlay.gameimage import GameImage
from PPlay.window import*
from PPlay.sprite import *
from drop import *


def draw_ghost_tiro(GHOST_tiro):
    for tiro in GHOST_tiro["lista"]:
        tiro[0].x+=tiro[1]*GHOST_tiro["velocidade"]
        tiro[0].y+=tiro[2]*GHOST_tiro["velocidade"]
        if tiro[0].x<0 or tiro[0].x>800 or tiro[0].y<0 or tiro[0].y>530:
            GHOST_tiro["lista"].remove(tiro)
        tiro[0].draw()

def up_shoot(shoot_up,player,sprite):
    shoot_img="sprites/cima.png"
    temp=Sprite(shoot_img,1)
    temp.x=player.x+player.width/2-temp.width/2
    temp.y=player.y+player.height/2-temp.height/2
    shoot_up.append(temp)
    return shoot_up

def down_shoot(shoot_down,player,sprite):
    shoot_img=sprite
    temp=Sprite(shoot_img,1)
    temp.x=player.x+player.width/2-temp.width/2
    temp.y=player.y+player.height/2-temp.height/2
    shoot_down.append(temp)
    return shoot_down

def left_shoot(shoot_left,player,sprite):
    shoot_img=sprite
    temp=Sprite(shoot_img,1)
    temp.x=player.x+player.width/2-temp.width/2
    temp.y=player.y+player.height/2-temp.height/2
    shoot_left.append(temp)
    return shoot_left

def right_shoot(shoot_right,player,sprite):
    shoot_img=sprite
    temp=Sprite(shoot_img,1)
    temp.x=player.x+player.width/2-temp.width/2
    temp.y=player.y+player.height/2-temp.height/2
    shoot_right.append(temp)
    return shoot_right

def draw_shoot_up(shoot,vel_tiro,dt):
    for i in shoot:
        i.y-=10*dt*vel_tiro
        i.draw()
        if i.y<30:
            shoot.remove(i)
            print("removido")

def draw_shoot_down(shoot,vel_tiro,dt):
    for i in shoot:
        i.y+=10*dt*vel_tiro
        i.draw()
        if i.y>530-i.height:
            shoot.remove(i)
            print("removido")

def draw_shoot_left(shoot,vel_tiro,dt):
    for i in shoot:
        i.x-=10*dt*vel_tiro
        i.draw()
        if i.x<0:
            shoot.remove(i)
            print("removido")

def draw_shoot_right(shoot,vel_tiro,dt):
    for i in shoot:
        i.x+=10*dt*vel_tiro
        i.draw()
        if i.x>800 -i.width:
            shoot.remove(i)
            print("removido")


def colisao_flecha(up,dano,INIMIGO,uni,dir,lista_vida,SCORE):
    hit=pygame.mixer.Sound('sprites/Meat_impacts_2.mp3')
    temp_tiro=[]
    temp_cobra=[]
    for i in range(len(up)):
        for j in range(len(INIMIGO["lista"])):
                if up[i].collided(INIMIGO["lista"][j][0]) and not(i in temp_tiro):
                    hit.play()
                    print("colisao, vida=",INIMIGO["lista"][j][1])
                    INIMIGO["lista"][j][1]-=dano
                    temp_tiro.append(i)
                    print("vida pos colisao",INIMIGO["lista"][j][1])
                    
                    if dir=="y" and INIMIGO["tipo"]!="boss":
                        INIMIGO["lista"][j][0].y+=uni*INIMIGO["lista"][j][0].height
                    elif dir=="x"and INIMIGO["tipo"]!="boss":
                        INIMIGO["lista"][j][0].x+=uni*INIMIGO["lista"][j][0].width
                    if INIMIGO["lista"][j][1]<=0:
                        print("cobra morta")
                        lista_vida=drop_vida(INIMIGO["lista"][j][0],lista_vida)
                        temp_cobra.append(j)
                        SCORE["Kills"]+=1
                        break
                    break
    for i in range(len(temp_tiro)):
        del up[temp_tiro[i]]
    for i in range(len(temp_cobra)):
        del INIMIGO["lista"][temp_cobra[i]]
    return up,lista_vida
    

