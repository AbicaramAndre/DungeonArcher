from PPlay.gameimage import GameImage
from PPlay.window import*
from PPlay.collision import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from random import randint
from random import choice
from enemy import *
from background import *
from flecha import *
from pygame.event import wait
def game_loop(janela):
    
    RGB=(0,0,0)
    #janela = Window(800, 530)
    #janela.set_title("Working in progress")
    janela.set_background_color(RGB)

    fundo=GameImage("sprites/fundo3.png")

    #hud
    coracao=["sprites/coracao.png","sprites/coracaovazio.png"]
    T_time_ini=time.time()
    
    #sounds
    shoot_sound=pygame.mixer.Sound('sprites/gooattach01.mp3')
    hit_sound=pygame.mixer.Sound('sprites/roblox-death-sound-effect.mp3')
    end_level=pygame.mixer.Sound('sprites/isaacbosswin.mp3')
    new_level=pygame.mixer.Sound('sprites/treasure room enter.mp3')
    vida_up=pygame.mixer.Sound('sprites/heartin.mp3')
    vida_down=pygame.mixer.Sound('sprites/heartout.mp3')
    death_sound=pygame.mixer.Sound('sprites/Momappear.wav')
    tiro_ghost_sound=pygame.mixer.Sound("sprites/TearImpacts2.mp3")
    ghost_hit=pygame.mixer.Sound("sprites/Death_Burst_Small_0.mp3")
    boss_round_sound=pygame.mixer.Sound("sprites/bossintro.mp3")
    end_boss=pygame.mixer.Sound("sprites/04 The Binding of Isaac Soundtrack Unknown Depths Below in HD.mp3")
    songs=[]
   
    FLECHA={
        "sprite":["sprites/baixo.png","sprites/cima.png","sprites/esquerda.png","sprites/direita.png"],
        "up":[],
        "down":[],
        "left":[],
        "right":[],
        "velocidade":20,
    }
    PLAYER={
        "dano":1,
        "velocidade":130,
        "vida":3,
        "vida_max":5,
        "sprite":"sprites/archer/idle_1.png",
        "idle_frame":5,
        "sprite_rund":"sprites/archer/run_direita.png",
        "sprite_rune":"sprites/archer/player_esquerda.png",
        "run_frame":10,
        "sprite_left":"sprites/archer/player_esquerda.png",
        "sprite_right":"sprites/archer/player_direita.png",
        "ataque_frame":9,
        "direcao":"down",
        "charge_time":1.5,
        "corrida":130   
    }
    player = Sprite(PLAYER["sprite"],PLAYER["idle_frame"])
    player2 = Sprite(PLAYER["sprite"],PLAYER["idle_frame"])
    player.set_total_duration(1000)
    lista_vida=[]
    teclado = Window.get_keyboard() 
    mouse=Window.get_mouse()
    new=False
    player.x=janela.width/2
    player.y=janela.height/2
    player2.x=janela.width/2
    player2.y=janela.height/2
    Spawm=True
    charge1=charge2=time.time()
    START=True
    Timer1=Timer2=time.time()
    temp_dano1=temp_dano2=time.time()
    clock=5
    despawn1=time.time()
    #dificuldade
    N_level=5
    progress=0
   
    COBRA={
        'dano':1,
        "tipo":"cobra",
        "velocidade":50,
        "vida":2,
        "qtde":2,
        "qtde_max":3,
        "sprite":["sprites/cobra/Cobra Sprite Sheet2.png","sprites/cobra/Cobra Sprite Sheet2_E.png"],
        "frames":8,
        "lista":[]
    }
    ARANHA={
        "dano":1,
        "tipo":"aranha",
        "velocidade":15,
        "vida":1,
        "qtde":3,
        "qtde_max":3,
        "sprite":["sprites/aranha/Spider_d.png","sprites/aranha/Spider.png"],
        "frames":9,
        "lista":[]
    }

    GHOST_tiro={
        "dano":1,
        "tipo":"ghost_tiro",
        "velocidade":150,
        "vida":1,
        "sprite":["sprites/g_tiro.png"],
        "frames":1,
        "charge_time":7.5,
        "up":[],
        "down":[],
        "left":[],
        "right":[],
        "disitancia":300,
        "lista":[]
    }
    GHOST={
        "tipo":"ghost",
        "velocidade":15,
        "vida":3,
        "qtde":1,
        "qtde_max":1,
        "sprite":["sprites/ghost_D.png","sprites/ghost_E.png"],
        "lista":[],
        "frames":8
    }

    BOSS={
        "dano":2,
        "tipo":"boss",
        "velocidade":15,
        "vida":10,
        "qtde":1,
        "qtde_max":1,
        "sprite":["sprites/boss_D.png","sprites/boss_E.png"],
        "lista":[],
        "frames":10,
        "sprite_morte":["sprites/boss_tiro.png"],
    }
    BOSS_tiro={
        'disitancia':300,
        "dano":1,
        "tipo":"boss_tiro",
        "velocidade":150,
        "vida":1,
        "sprite":["sprites/g_tiro.png"],
        "frames":1,
        "charge_time":7.5,
        "lista":[]
    }


    SCORE={
        "score":0,
        "N_hits":0,
        "N_shoots":0,
        "N_time":0,
        "Kills":0,
        }
   
    CORACAO={
        "sprite":["sprites/coracao.png","sprites/coracaovazio.png"],
        "frames":1
    }

    item_pool={
        "dano":["aumento de dano",1,"sprites/dano.png"],
        "velocidade":["aumento de velocidade",PLAYER["velocidade"]*1.1,"sprites/velocidade.png"],
        "vida_max":["aumento de vida maxima",PLAYER["vida_max"]+1,"sprites/coracaovazio.png"],
        "cadencia":["aumento de cadencia",PLAYER["charge_time"]*0.9,"sprites/cadencia.png"],
        "velocida_flecha":["aumento de velocidade de flecha",FLECHA["velocidade"]*1.1,"sprites/DROP_FLECHA.png"],
        #"empurrao":["aumanta empurrao de inimigos",1],
    }
    item_list=[]
    boss_item_list=[]
    boss_round=False
    colide=True
    while True:
        
        janela.set_background_color(RGB)
        fundo.x=0
        fundo.y=+30
        fundo.draw()

        #HUD###############################
        #desenha vida do player
        for k in range(PLAYER["vida_max"]):
            if k==14:
                break
            if k<PLAYER["vida"]:
                cor=Sprite(CORACAO["sprite"][0],CORACAO["frames"])
            else:
                cor=Sprite(CORACAO["sprite"][1],CORACAO["frames"])
            cor.x=k*25
            cor.y=2
            cor.draw()
        #desenha tempo
        T_time=time.time()-T_time_ini
        T_time=round(T_time,2)
        if T_time<60:
            janela.draw_text("Tempo: "+str(round(T_time//1))+" segundos",janela.width-100,5,11,(255,255,255),"Arial")
        else:
            janela.draw_text("Tempo: "+str(round(T_time//60))+":"+str(round(T_time%60))+" minutos",janela.width-100,2,11,(255,255,255),"Arial")
        #desenha score
        janela.draw_text("Score: "+str(SCORE["score"]),janela.width-100,15,11,(255,255,255),"Arial")
        #desenha level
        janela.draw_text("Level: "+str(N_level+1),janela.width/2-50,5,20,(255,255,255),"Arial")
        ####################################

        if START:
            bg=rand_bg(10)
            chao=rand_chao(10)
            START=False
        draw_bg(bg)
        draw_chao(chao)


        # desenha o player
        player.draw()
        player2.draw()
        player2.hide()
        
        
        #Spawn de inimigos/desenha inimigos/movimneto de inimigos
        if Spawm and (clock>= 5):
            score_time1=time.time()

            if N_level>0 and not(boss_round):
                new_level.play()

            Spawm=False
            spawn_enemy(COBRA,janela)
            spawn_enemy(ARANHA,janela)
            spawn_enemy2(GHOST,janela)
            if boss_round:
                spawn_enemy2(BOSS,janela)
                boss_round=False
                boss_round_sound.play()
            print("vida anranha: ",ARANHA["vida"])
            print("vida cobra: ",COBRA["vida"])
            print("vida ghost: ",GHOST["vida"])
            print("vida boss: ",BOSS["vida"])

        clock=Timer1-Timer2
        move_enemy(COBRA,player,janela.delta_time())
        move_enemy(ARANHA,player,janela.delta_time())
        move_enemy(GHOST,player,janela.delta_time())
        move_enemy(BOSS,player,janela.delta_time())
        draw_enemy(COBRA,player)
        draw_enemy(ARANHA,player)
        draw_enemy(GHOST,player)
        draw_enemy(BOSS,player)

        ghost_shoot(GHOST,GHOST_tiro,player,janela.delta_time())
        if GHOST_tiro["lista"] != []:
            move_ghost_tiro(GHOST_tiro,janela.delta_time())

        ghost_shoot(BOSS,BOSS_tiro,player,janela.delta_time())
        if BOSS_tiro["lista"] != []:
            move_ghost_tiro(BOSS_tiro,janela.delta_time())
        
    
    
        #movimentação do player
        player2.x=player.x
        player2.y=player.y
        if teclado.key_pressed("w") and player.y>30:
            prox_y=player.y - PLAYER["velocidade"]*janela.delta_time()
            player.y=prox_y
            #player.y-=PLAYER["velocidade"]*janela.delta_time()
        if teclado.key_pressed("s") and player.y<janela.height-player.height:
            prox_y=player.y + PLAYER["velocidade"]*janela.delta_time()
            player.y=prox_y
            #player.y+=PLAYER["velocidade"]*janela.delta_time()
        if teclado.key_pressed("a") and player.x>0:
            prox_x=player.x - PLAYER["velocidade"]*janela.delta_time()
            player.x=prox_x
            #player.x-=PLAYER["velocidade"]*janela.delta_time()
        if teclado.key_pressed("d") and player.x<janela.width-player.width:
            prox_x=player.x + PLAYER["velocidade"]*janela.delta_time()
            player.x=prox_x
            #player.x+=PLAYER["velocidade"]*janela.delta_time()
        for i in bg:
            if player.collided(i):
                #print("colidiu")
                player.x=player2.x
                player.y=player2.y
                colide=True
                break

        if colide==False:
            player2.x=player.x
            player2.y=player.y

        
        
        
        

        
            
        
        #ataque jogador
        charge2=time.time()
        charge=charge2-charge1
        if teclado.key_pressed("up"):
            if PLAYER["direcao"]!="up":
                PLAYER["direcao"]="up"
                x=player.x
                y=player.y
                player = Sprite(PLAYER["sprite_left"],PLAYER["ataque_frame"])
                player.x=x
                player.y=y
            if charge>=PLAYER["charge_time"]:
                shoot_sound.play()
                print("up")
                FLECHA["up"]=up_shoot(FLECHA["up"],player,FLECHA["sprite"][1])
                charge2=time.time()
                charge1=charge2
                SCORE["N_shoots"]+=1

        if teclado.key_pressed("down"):  
            if PLAYER["direcao"]!="down":
                PLAYER["direcao"]="down"
                x=player.x
                y=player.y
                player = Sprite(PLAYER["sprite_right"],PLAYER["ataque_frame"])
                player.x=x
                player.y=y
            if charge>=PLAYER["charge_time"]:
                shoot_sound.play()
                print("down")
                FLECHA["down"]=down_shoot(FLECHA["down"],player,FLECHA["sprite"][0])
                charge2=time.time()
                charge1=charge2
                SCORE["N_shoots"]+=1

        if teclado.key_pressed("left") :
            if PLAYER["direcao"]!="left":
                PLAYER["direcao"]="left"
                print("left")
                x=player.x
                y=player.y
                player = Sprite(PLAYER["sprite_left"] ,PLAYER["ataque_frame"])
                player.x=x
                player.y=y
            if charge>=PLAYER["charge_time"]:
                shoot_sound.play()
                FLECHA["left"]=left_shoot(FLECHA["left"],player,FLECHA["sprite"][2])
                charge2=time.time()
                charge1=charge2
                SCORE["N_shoots"]+=1

        if teclado.key_pressed("right"): 
            if PLAYER["direcao"]!="right":
                PLAYER["direcao"]="right"
                print("right")
                x=player.x
                y=player.y
                player = Sprite(PLAYER["sprite_right"],PLAYER["ataque_frame"])
                player.x=x
                player.y=y
            if charge>=PLAYER["charge_time"]:
                shoot_sound.play()
                FLECHA["right"]=right_shoot(FLECHA["right"],player,FLECHA["sprite"][3])
                charge2=time.time()
                charge1=charge2
                SCORE["N_shoots"]+=1


        draw_shoot_up(FLECHA["up"],FLECHA["velocidade"],janela.delta_time())
        draw_shoot_down(FLECHA["down"],FLECHA["velocidade"],janela.delta_time())
        draw_shoot_left(FLECHA["left"],FLECHA["velocidade"],janela.delta_time())
        draw_shoot_right(FLECHA["right"],FLECHA["velocidade"],janela.delta_time())
    
        ###colisao flecha inimigo######
        #cobra
        FLECHA["up"],lista_vida=colisao_flecha(FLECHA["up"],PLAYER["dano"],COBRA,-1,"y",lista_vida,SCORE)
        FLECHA["down"],lista_vida=colisao_flecha(FLECHA["down"],PLAYER["dano"],COBRA,+1,"y",lista_vida,SCORE)
        FLECHA["left"],lista_vida=colisao_flecha(FLECHA["left"],PLAYER["dano"],COBRA,-1,"x",lista_vida,SCORE)
        FLECHA["right"],lista_vida=colisao_flecha(FLECHA["right"],PLAYER["dano"],COBRA,+1,"x",lista_vida,SCORE)
        #aranha
        FLECHA["up"],lista_vida=colisao_flecha(FLECHA["up"],PLAYER["dano"],ARANHA,-1,"y",lista_vida,SCORE)
        FLECHA["down"],lista_vida=colisao_flecha(FLECHA["down"],PLAYER["dano"],ARANHA,+1,"y",lista_vida,SCORE)
        FLECHA["left"],lista_vida=colisao_flecha(FLECHA["left"],PLAYER["dano"],ARANHA,-1,"x",lista_vida,SCORE)
        FLECHA["right"],lista_vida=colisao_flecha(FLECHA["right"],PLAYER["dano"],ARANHA,+1,"x",lista_vida,SCORE)
        #ghost
        FLECHA["up"],lista_vida=colisao_flecha(FLECHA["up"],PLAYER["dano"],GHOST,-1,"y",lista_vida,SCORE)
        FLECHA["down"],lista_vida=colisao_flecha(FLECHA["down"],PLAYER["dano"],GHOST,+1,"y",lista_vida,SCORE)
        FLECHA["left"],lista_vida=colisao_flecha(FLECHA["left"],PLAYER["dano"],GHOST,-1,"x",lista_vida,SCORE)
        FLECHA["right"],lista_vida=colisao_flecha(FLECHA["right"],PLAYER["dano"],GHOST,+1,"x",lista_vida,SCORE)
        #boss
        FLECHA["up"],lista_vida=colisao_flecha(FLECHA["up"],PLAYER["dano"],BOSS,-1,"y",lista_vida,SCORE)
        FLECHA["down"],lista_vida=colisao_flecha(FLECHA["down"],PLAYER["dano"],BOSS,+1,"y",lista_vida,SCORE)
        FLECHA["left"],lista_vida=colisao_flecha(FLECHA["left"],PLAYER["dano"],BOSS,-1,"x",lista_vida,SCORE)
        FLECHA["right"],lista_vida=colisao_flecha(FLECHA["right"],PLAYER["dano"],BOSS,+1,"x",lista_vida,SCORE)
        if BOSS["lista"]!=[]:
            final_x=BOSS["lista"][-1][0].x
            final_y=BOSS["lista"][-1][0].y


        #desenha drop
        for drop in lista_vida:
            drop.draw()
            drop.update()
        #colisao drop
        for drop in lista_vida:
            if Collision.collided(player,drop) and PLAYER["vida"]< PLAYER["vida_max"]:
                vida_up.play()
                print("pegou vida")
                PLAYER["vida"]+=1
                lista_vida.remove(drop)
                break

        despawn2=time.time()
        despawn=despawn2-despawn1
        if lista_vida==[] and despawn>15:
            despawn1=time.time()
        if lista_vida!=[] and despawn>15:
            lista_vida.remove(lista_vida[0])
            despawn1=time.time()
            despawn2=time.time()    
       

        #colisao player inimigo
        temp_dano2=time.time()
        temp_dano=temp_dano2-temp_dano1
        if temp_dano >3:
            #print("pode tomar dano")
            for cobra in COBRA["lista"]:
                if player.collided(cobra[0]):
                    print("tamanho da cobra: ", cobra[0].width, cobra[0].height)
                    print("tamanho do player: ", player.width, player.height)
                    print("posicao da cobra: ", cobra[0].x, cobra[0].y)
                    print("posicao do player: ", player.x, player.y)
                    PLAYER["vida"]-=COBRA["dano"]
                    print("Vida=",PLAYER["vida"])
                    temp_dano1=temp_dano2=time.time()
                    hit_sound.play()
                    vida_down.play()
                    SCORE["N_hits"]+=1
                    break
        if temp_dano >3:
            for aranha in ARANHA["lista"]:
                if player.collided(aranha[0]):
                    print("tamanho da aranha: ", aranha[0].width, aranha[0].height)
                    print("tamanho do player: ", player.width, player.height)
                    print("posicao da aranha: ", aranha[0].x, aranha[0].y)
                    print("posicao do player: ", player.x, player.y)
                    PLAYER["vida"]-=ARANHA["dano"]
                    print("Vida=",PLAYER["vida"])
                    temp_dano1=temp_dano2=time.time()
                    hit_sound.play()
                    vida_down.play()
                    SCORE["N_hits"]+=1
                    break
        if temp_dano >3:
            for boss in BOSS["lista"]:
                if player.collided(boss[0]):
                    print("tamanho do boss: ", boss[0].width, boss[0].height)
                    print("tamanho do player: ", player.width, player.height)
                    print("posicao do boss: ", boss[0].x, boss[0].y)
                    print("posicao do player: ", player.x, player.y)
                    PLAYER["vida"]-=BOSS["dano"]
                    print("Vida=",PLAYER["vida"])
                    temp_dano1=temp_dano2=time.time()
                    hit_sound.play()
                    vida_down.play()
                    SCORE["N_hits"]+=1
                    break

        if temp_dano >3:
            for tiro in GHOST_tiro["lista"]:
                if player.collided(tiro[0]):
                    PLAYER["vida"]-=GHOST_tiro["dano"]
                    print("Vida=",PLAYER["vida"])
                    temp_dano1=temp_dano2=time.time()
                    ghost_hit.play()
                    vida_down.play()
                    GHOST_tiro["lista"].remove(tiro)
                    SCORE["N_hits"]+=1
                    break
        if temp_dano >3:
            for tiro in BOSS_tiro["lista"]:
                if player.collided(tiro[0]):
                    PLAYER["vida_max"]-=BOSS_tiro["dano"]
                    print("Vida_max=",PLAYER["vida_max"])
                    temp_dano1=temp_dano2=time.time()
                    ghost_hit.play()
                    vida_down.play()
                    BOSS_tiro["lista"].remove(tiro)
                    SCORE["N_hits"]+=1
                    break
        

        #fim da fase
        if len(COBRA["lista"])==0 and len(ARANHA["lista"])==0 and len(GHOST["lista"])==0 and len(BOSS["lista"])==0 and not(Spawm):
            if N_level%3==0 and not(boss_round):
                end_boss.play()
            else:
                end_level.play()
            #calculo do score
            score_time2=time.time()
            SCORE["N_time"]=score_time2-score_time1
            #SCORE["N_levels"]=SCORE["N_levels"]+1
            if SCORE["N_hits"]==0:
                SCORE["N_hits"]=1
            SCORE["score"]+=int((N_level+1)*1000+(1/SCORE["N_time"])*100-(SCORE["N_shoots"])*10+(SCORE["Kills"]/SCORE["N_hits"])*100)
            SCORE["N_hits"]=0
            SCORE["Kills"]=0

            
            print("Fim da fase")
            Spawm=True
            clock=0
            Timer1=time.time()
            Timer2=Timer1
            N_level+=1
            print("Nivel=",N_level)


            print(N_level)
            #aumento de dificuladade
            diff=N_level%3
            progress+=1
            if progress==3:
                BOSS["qtde"]=1
                boss_round=True
                ARANHA["qtde"]=0
                COBRA["qtde"]=0
                GHOST["qtde"]=0
                print("boss round")
                if N_level>3 and N_level<6:
                    BOSS["vida"]+=2
                    BOSS["dano"]+=1
                if N_level>6 and N_level<9:
                    BOSS["vida"]+=2
                    BOSS["dano"]+=1
                    BOSS["velocidade"]+=10
                if N_level>24:
                    BOSS["vida"]+=2
                    BOSS["dano"]+=1
                    BOSS["velocidade"]+=10
                    ARANHA["qtde"]=ARANHA["qtde_max"]-(ARANHA["qtde_max"]//2)
                    COBRA["qtde"]=COBRA["qtde_max"] -(COBRA["qtde_max"]//2)
                    GHOST["qtde"]=GHOST["qtde_max"] -(GHOST["qtde_max"]//2)
                if N_level>27:
                    BOSS["qtde"]+=1
            elif progress==4:
                ARANHA["velocidade"]+=int(ARANHA["velocidade"]*0.1)
                COBRA["velocidade"]+=int(COBRA["velocidade"]*0.1)
                GHOST["velocidade"]+=int(GHOST["velocidade"]*0.1)
                COBRA["vida"]+=int(COBRA["vida"]+(diff*1.5//1))
                ARANHA["vida"]+=int(ARANHA["vida"]+(diff//2))
                GHOST["vida"]+=int(GHOST["vida"]+(diff//3))
                ARANHA["qtde_max"]+=1
                COBRA["qtde_max"]+=1
                GHOST["qtde_max"]+=1
                ARANHA["dano"]+=1
                COBRA["dano"]+=1
                GHOST_tiro["dano"]+=1
                ARANHA["qtde"]=ARANHA["qtde_max"]
                COBRA["qtde"]=COBRA["qtde_max"]
                GHOST["qtde"]=GHOST["qtde_max"]
                print("jogo esta ficando dificil")
                item=item_pool["vida_max"]
                ITEM=Sprite(item[2])
                ITEM.x=final_x - ITEM.width/2
                ITEM.y=final_y - ITEM.height/2
                boss_item_list.append([ITEM,"vida_max"])
            elif progress==0 or progress==1 or progress==2:
                ARANHA["qtde"]+=diff
                COBRA["qtde"]+=diff-1
                GHOST["qtde"]+=diff

            if progress==4:
                progress=0
            print("progress= ",progress)

            
            #drop de itens  
            item=choice(list(item_pool.keys()))
            ITEM=Sprite(item_pool[item][2])
            ITEM.x=janela.width/2-ITEM.width/2
            ITEM.y=janela.height/2-ITEM.height/2
            item_list.append([ITEM,item])
            item_clock1=time.time()
                
        
        #drop de itens
        for drop in boss_item_list:
            drop[0].draw()
        for drop in boss_item_list:
            if Collision.collided(player,drop[0]):
                print("pegou item")
                if drop[1]=="vida_max":
                    PLAYER["vida_max"]+=1
                    print("vida maxima aumentada: ",PLAYER["vida_max"])
                elif drop[1]=="dano":
                    PLAYER["dano"]+=2
                    print("dano aumentado: ",PLAYER["dano"])
                elif drop[1]=="velocidade":
                    PLAYER["velocidade"]+= PLAYER["velocidade"]*0.2
                    print("velocidade aumentada: ",PLAYER["velocidade"])
                elif drop[1]=="cadencia":
                    PLAYER["charge_time"]-= PLAYER["charge_time"]*0.2
                    print("cadencia aumentada: ",PLAYER["charge_time"])
                elif drop[1]=="vida":
                    PLAYER["vida"]+=1
                    print("vida aumentada: ",PLAYER["vida"])
                boss_item_list.remove(drop)


        for drop in item_list:
            drop[0].draw()
        for drop in item_list:
            if Collision.collided(player,drop[0]):
                print("pegou item")
                if drop[1]=="vida_max":
                    PLAYER["vida_max"]+=1
                    print("vida maxima aumentada: ",PLAYER["vida_max"])
                elif drop[1]=="dano":
                    PLAYER["dano"]+=2
                    print("dano aumentado: ",PLAYER["dano"])
                elif drop[1]=="velocidade":
                    PLAYER["velocidade"]+= PLAYER["velocidade"]*0.2
                    print("velocidade aumentada: ",PLAYER["velocidade"])
                elif drop[1]=="cadencia":
                    PLAYER["charge_time"]-= PLAYER["charge_time"]*0.2
                    print("cadencia aumentada: ",PLAYER["charge_time"])
                elif drop[1]=="velocidade_flecha":
                    FLECHA["velocidade"]+= FLECHA["velocidade"]*0.2
                    print("velocidade da flecha aumentada: ",FLECHA["velocidade"])
        
                item_list.remove(drop)

        if item_list!=[]:
            item_clock2=time.time()
            item_clock=item_clock2-item_clock1
            if item_clock>10:
                drop=item_list[-1]
                item_list.remove(drop)
                print("item expirado")
                item_clock1=time.time()


        Timer1=time.time()


        if(teclado.key_pressed("ESC")) or (PLAYER["vida"]<=0):
            if PLAYER["vida"]<=0:
                #salvar score
                file=open("rank/score.txt","a")
                texto= str(SCORE["score"])+"\t"+str(N_level)+"\t"+str(SCORE["N_time"])+"\n"
                file.write(texto)
                print(texto)
                file.close()
                print("Game Over")
                time.sleep(0.5)
                janela.set_background_color(RGB)
                
                fundo=GameImage("sprites/pkvocemorreu.png")
                death_sound.play()
                death_sound.set_volume(0.6)
                fundo.x=janela.width/2-fundo.width/2
                fundo.y=janela.height/2-fundo.height/2

                fundo.draw()
                janela.update()
                time.sleep(5)
                
            print("Fim de jogo")
            COBRA["lista"]=[]
            ARANHA["lista"]=[]
            GHOST["lista"]=[]
            GHOST_tiro["lista"]=[]
            BOSS["lista"]=[]
            BOSS_tiro["lista"]=[]
            fundo=[]
            FLECHA["up"]=[]
            FLECHA["down"]=[]
            FLECHA["left"]=[]
            FLECHA["right"]=[]
            janela.update()
            return
        janela.update()
        
        