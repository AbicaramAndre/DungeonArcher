from PPlay.gameimage import GameImage
from PPlay.window import*
from PPlay.sprite import *



def le_arq(txt):
    file=open(txt,"r")
    line=file.readline()
    lista=[]
    while line:
        lista.append(line.split())
        line=file.readline()
    file.close()
    return lista

def ordenaRank(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if int(lista[i][0])>int(lista[j][0]):
                lista[i],lista[j]=lista[j],lista[i]
    return lista

def escreveRank(lista):
    file=open("rank/score.txt","w")
    for i in range(5):
        file.write(lista[i][0]+"\t"+lista[i][1]+"\t"+lista[i][2]+"\n")
    file.close()


def rank(janela):

    RGB=(0,0,0)
    janela.set_background_color(RGB)
    teclado = Window.get_keyboard() 
    mouse=Window.get_mouse()
    texto=le_arq("rank/score.txt")
    #print(texto)
    texto=ordenaRank(texto)
    #print(texto)
    if len(texto)<5:
        for i in range(5-len(texto)):
            texto.append(["0","0","0"])
    escreveRank(texto)
    for i in range(len(texto)):
        print(texto[i][2])
        temp=   str(round(float(texto[i][2])//60))+":"+str(round(float(texto[i][2])%60))+" minutos"
        print(temp)
        texto[i][2]=temp
    
    img=GameImage("sprites/Rmenu.png")
        
    
    #janela.draw_text("Ranking (Top 5):",janela.width/2-100,0,30,(255,255,255))
    while(True):
        img.draw()
        for i in range(5):
            var=str(i+1)+"- Score:"+texto[i][0]+" | "+"Level:"+texto[i][1]+" | "+"tempo "+str(texto[i][2])  
            janela.draw_text(var,20,100+i*55,30,(0,0,0))

        if teclado.key_pressed("ESC"):
            return
        janela.update()