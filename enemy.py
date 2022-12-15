from PPlay.window import*
from PPlay.sprite import *
from random import randint
from math import dist
from math import sqrt

def spawn_enemy(INIMIGO,janela):

    for i  in range(INIMIGO["qtde"]):
        temp=Sprite(INIMIGO["sprite"][0],INIMIGO["frames"])
        temp.set_total_duration(1000)
        temp.x=randint(0,janela.width-temp.width)
        temp.y=randint(0,1)*(janela.height) +30
        INIMIGO["lista"].append([temp,INIMIGO["vida"],"D"])

def spawn_enemy2(INIMIGO,janela):

    for i  in range(INIMIGO["qtde"]):
        temp=Sprite(INIMIGO["sprite"][0],INIMIGO["frames"])
        temp.set_total_duration(1000)
        temp.x=randint(0,janela.width-temp.width)
        temp.y=randint(0,1)*(janela.height) +30
        INIMIGO["lista"].append([temp,INIMIGO["vida"],"D",0])

def draw_enemy(INIMIGO,player):

    for i in INIMIGO["lista"]:
        if player.x<i[0].x and i[2]=="D":
            x=i[0].x
            y=i[0].y
            i[0]=Sprite(INIMIGO["sprite"][1],INIMIGO["frames"])
            i[0].x=x
            i[0].y=y
            i[0].set_total_duration(1000)
            i[2]="E"
        if player.x>i[0].x and not(i[2]=="D"):
            x=i[0].x
            y=i[0].y
            i[0]=Sprite(INIMIGO["sprite"][0],INIMIGO["frames"])
            i[0].x=x
            i[0].y=y
            i[0].set_total_duration(1000)
            i[2]="D"
        i[0].draw()
        i[0].update()


def move_enemy(INIMIGO,player,dt):
    
    if INIMIGO["tipo"]=="cobra":
        for cobra in INIMIGO["lista"]:
            if player.x + player.width/2 > cobra[0].x + cobra[0].width/2:
                cobra[0].x+=INIMIGO["velocidade"]*dt + 30*randint(-1,1)*dt
            if player.x + player.width/2 < cobra[0].x + cobra[0].width/2:
                cobra[0].x-=INIMIGO["velocidade"]*dt + 30*randint(-1,1)*dt
            if player.y +player.height/2 > cobra[0].y + cobra[0].height/2:
                cobra[0].y+=INIMIGO["velocidade"]*dt + 30*randint(-1,1)*dt
            if player.y + player.height/2 < cobra[0].y + cobra[0].height/2:
                cobra[0].y-=INIMIGO["velocidade"]*dt + 30*randint(-1,1)*dt

            if cobra[0].y<30:
                cobra[0].y=30
            if cobra[0].y>530-cobra[0].height:
                cobra[0].y=530-cobra[0].height
            if cobra[0].x<0:
                cobra[0].x=2
            if cobra[0].x>800-cobra[0].width:
                cobra[0].x=800-cobra[0].width



    if INIMIGO["tipo"]=="aranha":
        for aranha in INIMIGO["lista"]:
            
            if player.x + player.width/2 > aranha[0].x + aranha[0].width/2:
                aranha[0].x+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                
            if player.x + player.width/2 < aranha[0].x + aranha[0].width/2:
                aranha[0].x-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                
            if player.y +player.height/2 > aranha[0].y + aranha[0].height/2:
                aranha[0].y+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                
            if player.y + player.height/2 < aranha[0].y + aranha[0].height/2:
                 aranha[0].y-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
            
            if aranha[0].y<30:
                aranha[0].y=30
            if aranha[0].y>530-aranha[0].height:
                aranha[0].y=530-aranha[0].height
            if aranha[0].x<0:
                aranha[0].x=2
            if aranha[0].x>800-aranha[0].width:
                aranha[0].x=800-aranha[0].width

        
    if INIMIGO["tipo"]=="ghost":
        for ghost in INIMIGO["lista"]:
            if dist((player.x,player.y),(ghost[0].x,ghost[0].y))>170:
                if player.x + player.width/2 > ghost[0].x + ghost[0].width/2:
                    ghost[0].x+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.x + player.width/2 < ghost[0].x + ghost[0].width/2:
                    ghost[0].x-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y +player.height/2 > ghost[0].y + ghost[0].height/2:
                    ghost[0].y+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y + player.height/2 < ghost[0].y + ghost[0].height/2:
                    ghost[0].y-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
            elif dist((player.x,player.y),(ghost[0].x,ghost[0].y))<150:
                if player.x + player.width/2 > ghost[0].x + ghost[0].width/2:
                    ghost[0].x-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.x + player.width/2 < ghost[0].x + ghost[0].width/2:
                    ghost[0].x+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y +player.height/2 > ghost[0].y + ghost[0].height/2:
                    ghost[0].y-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y + player.height/2 < ghost[0].y + ghost[0].height/2:
                    ghost[0].y+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
            if ghost[0].y<30:
                ghost[0].y=30
            if ghost[0].y>530-ghost[0].height:
                ghost[0].y=530-ghost[0].height
            if ghost[0].x<0:
                ghost[0].x=2
            if ghost[0].x>800-ghost[0].width:
                ghost[0].x=800-ghost[0].width

    if INIMIGO["tipo"]=="boss":
        for boss in INIMIGO["lista"]:
            if dist((player.x,player.y),(boss[0].x,boss[0].y))>200:
                if player.x + player.width/2 > boss[0].x + boss[0].width/2:
                    boss[0].x+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.x + player.width/2 < boss[0].x + boss[0].width/2:
                    boss[0].x-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y +player.height/2 > boss[0].y + boss[0].height/2:
                    boss[0].y+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y + player.height/2 < boss[0].y + boss[0].height/2:
                    boss[0].y-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
            elif dist((player.x,player.y),(boss[0].x,boss[0].y))<200:
                if player.x + player.width/2 > boss[0].x + boss[0].width/2:
                    boss[0].x+=INIMIGO["velocidade"]*dt*1.5 
                if player.x + player.width/2 < boss[0].x + boss[0].width/2:
                    boss[0].x-=INIMIGO["velocidade"]*dt*1.5
                if player.y +player.height/2 > boss[0].y + boss[0].height/2:
                    boss[0].y+=INIMIGO["velocidade"]*dt*1.5
                if player.y + player.height/2 < boss[0].y + boss[0].height/2:
                    boss[0].y-=INIMIGO["velocidade"]*dt*1.5
                

def move_enemy2(INIMIGO,player,dt,timer):
    if INIMIGO["tipo"]=="ghost":
        for ghost in INIMIGO["lista"]:
            if dist((player.x,player.y),(ghost[0].x,ghost[0].y))>170:
                if player.x + player.width/2 > ghost[0].x + ghost[0].width/2:
                    ghost[0].x+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.x + player.width/2 < ghost[0].x + ghost[0].width/2:
                    ghost[0].x-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y +player.height/2 > ghost[0].y + ghost[0].height/2:
                    ghost[0].y+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y + player.height/2 < ghost[0].y + ghost[0].height/2:
                    ghost[0].y-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
            elif dist((player.x,player.y),(ghost[0].x,ghost[0].y))<150:
                if player.x + player.width/2 > ghost[0].x + ghost[0].width/2:
                    ghost[0].x-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.x + player.width/2 < ghost[0].x + ghost[0].width/2:
                    ghost[0].x+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y +player.height/2 > ghost[0].y + ghost[0].height/2:
                    ghost[0].y-=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
                if player.y + player.height/2 < ghost[0].y + ghost[0].height/2:
                    ghost[0].y+=INIMIGO["velocidade"]*dt + 10*randint(-1,1)*dt
            elif timer>INIMIGO["charge_time"]:
                pass
            if ghost[0].y<30:
                ghost[0].y=30
            if ghost[0].y>530-ghost[0].height:
                ghost[0].y=530-ghost[0].height
            if ghost[0].x<0:
                ghost[0].x=2
            if ghost[0].x>800-ghost[0].width:
                ghost[0].x=800-ghost[0].width

def ghost_shoot(GHOST,GHOST_tiro,player,dt):
    for ghost in GHOST["lista"]:
        if ghost[3]<GHOST_tiro["charge_time"]:
            ghost[3]+=dt
        if ghost[3]>GHOST_tiro["charge_time"] and dist((player.x,player.y),(ghost[0].x,ghost[0].y))<GHOST_tiro["disitancia"]:
            tiro_ghost_sound=pygame.mixer.Sound("sprites/TearImpacts2.mp3")
            tiro_ghost_sound.play()
            ghost[3]=0
            hipotenusa=dist((player.x,player.y),(ghost[0].x,ghost[0].y))
            if player.y<ghost[0].y and player.x>ghost[0].x:
                sen=(player.y-ghost[0].y)/hipotenusa
                cos=(player.x-ghost[0].x)/hipotenusa
                tiro=Sprite("sprites/g_tiro.png",1)
                tiro.x=ghost[0].x+ghost[0].width/2
                tiro.y=ghost[0].y+ghost[0].height/2
                GHOST_tiro["lista"].append([tiro,cos,sen])
            if player.y>ghost[0].y and player.x>ghost[0].x:
                sen=(player.y-ghost[0].y)/hipotenusa
                cos=(player.x-ghost[0].x)/hipotenusa
                tiro=Sprite("sprites/g_tiro.png",1)
                tiro.x=ghost[0].x+ghost[0].width/2
                tiro.y=ghost[0].y+ghost[0].height/2
                GHOST_tiro["lista"].append([tiro,cos,sen])
                
            if player.y<ghost[0].y and player.x<ghost[0].x:
                sen=(player.y-ghost[0].y)/hipotenusa
                cos=(player.x-ghost[0].x)/hipotenusa
                tiro=Sprite("sprites/g_tiro.png",1)
                tiro.x=ghost[0].x+ghost[0].width/2
                tiro.y=ghost[0].y+ghost[0].height/2
                GHOST_tiro["lista"].append([tiro,cos,sen])
            
            if player.y>ghost[0].y and player.x<ghost[0].x:
                sen=(player.y-ghost[0].y)/hipotenusa
                cos=(player.x-ghost[0].x)/hipotenusa
                tiro=Sprite("sprites/g_tiro.png",1)
                tiro.x=ghost[0].x+ghost[0].width/2
                tiro.y=ghost[0].y+ghost[0].height/2
                GHOST_tiro["lista"].append([tiro,cos,sen])
            print(sen,cos)



def move_ghost_tiro(GHOST_tiro,dt):
    for tiro in GHOST_tiro["lista"]:
        tiro[0].x+=GHOST_tiro["velocidade"]*dt*tiro[1]
        tiro[0].y+=GHOST_tiro["velocidade"]*dt*tiro[2]
        if tiro[0].x<0 or tiro[0].x>800 or tiro[0].y<30 or tiro[0].y>530:
            GHOST_tiro["lista"].remove(tiro)
            print("tiro removido")
        tiro[0].draw()



            