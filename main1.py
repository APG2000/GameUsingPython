from cProfile import run
from pickle import FALSE, TRUE
import pygame 
import sys
import random
import time
import math
from pygame import mixer 
pygame.init()


screnn=pygame.display.set_mode((800,600))





background=pygame.image.load('./images/space.png')
#player
playerImg=pygame.image.load('./images/sprit.png')

playerX=370
playery=530
playerX_change=0
playerY_change=0
#enimy
#enimyimg=pygame.image.load("enimy3.png").convert()


ra="enimy"+str(random.randint(1,3))



enimyimg=pygame.image.load("./images/"+ra+".png")

enimyx=random.randint(0,800)
enimyy=random.randint(5,150)
enimyx_change=0.6
enimyy_change=0.6






balaimg=pygame.image.load("./images/fugi.png")

balax=enimyx
balay=5

balax_change=0
balay_change=0.7
bala_state="ready"













#bala
buletimg=pygame.image.load("./images/bullet.png")
buletx=0
bulety=480

buletx_change=0
bulety_change=2
bulet_state="ready"
# bala inimiga

balaimg=pygame.image.load("./images/fugi.png")
balax=enimyx
balay=enimyy

balax_change=0
balay_change=1
bulet_state="ready"
#game settings 

pontos_value=0
font=pygame.font.Font("font.otf",32)
textX=10
textY=10

mixer.music.load("./sounds/sound-god.wav")
mixer.music.play(-1)

vida_value=10
vidax=10
viday=40

vidainimigo_value=4
vidainimigax=10
vidainimigay=70



def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 64)

    gameSurf = gameOverFont.render('Game Over', True, "red")





    screnn.blit(gameSurf, (250,250))




    pygame.display.update()

    pygame.time.wait(500)











def gameover():
    
    over_font=pygame.font.Font("font.otf",64)
    over_text=font.render("Game OVer ",True,("red"))
    time.sleep(1)
    s=mixer.Sound("./sounds/sound-gameover.wav")
    s.play()
    time.sleep(1)
    screnn.blit(over_text,(250,250))
  
def mostrarvida(x,y):
    vida=font.render("Vida: "+str(vida_value),True,("green"))
    screnn.blit(vida,(x,y))
    
def mostrarvidainimiga(x,y):
    vidainimiga=font.render("Boss: "+str(vidainimigo_value),True,("red"))
    screnn.blit(vidainimiga,(x,y))
    
def mostrarpontos(x,y):
    pontos=font.render("Pontos: "+str(pontos_value),True,(255,255,255))
    screnn.blit(pontos,(x,y))




def atirar(x,y):
    global bulet_state
    bulet_state="fire"
    screnn.blit(buletimg,(x+20,y+20))


def atirar2(x,y):
    global bala_state
    bala_state="fire"
    screnn.blit(balaimg,(x+16,y+16))




def iscollision(enimyx,enimyy,buletx,bulety):
    distance=math.sqrt((math.pow(enimyx-buletx,2))+(math.pow(enimyy-bulety,2)))
    if distance<27:
        return True
    else:
        return False




def player(x,y):
    screnn.blit(playerImg,(playerX,playery))

def enimy(x,y):
    
    
    
    screnn.blit(enimyimg,(enimyx,enimyy))
    
running=True

# game Loop
counter=5
while running:
    screnn.fill(("black"))
    #backgroundimage
    screnn.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LEFT or event.key==ord("a"):
                playerX_change=-0.5
            if event.key==pygame.K_RIGHT or event.key==ord("d"):
                playerX_change=0.5
                
            if event.key==pygame.K_UP or event.key==ord("w"):

                playerY_change=-0.5
            if event.key==pygame.K_DOWN or event.key==ord("s"):

                playerY_change=0.5
            
            
            if event.key==pygame.K_SPACE:
                if bulet_state =="ready":
                    somdetiro=mixer.Sound("./sounds/sound-tiro.wav")
                    somdetiro.play()
                    buletx=playerX
                    atirar(buletx,bulety)
            if event.key==ord("p"):
                if bala_state is "ready":
                    balay=enimyy
                    balax=enimyx
                    atirar2(balax,balay)
            if event.key==ord("t"):
                print("INIMIgo modo turbo ativado")
                balay_change+=0.2
            if event.key==ord("l"):
                print("Loser MODE")
                balay_change=0.9
                bulety_change=3
            if event.key==ord("r"):
                print("Setting reseted")
                balay_change=0.7
                bulety_change=1.5
            if event.key==ord("y"):
                print("change music")
                mixer.music.stop()

                
                
                a=mixer.Sound("./sounds/paredao.wav")
                print(a)
                a.play()


        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN or event.key==pygame.K_UP or event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==ord("a") or event.key==ord("d") or event.key==ord("w")or event.key==ord("s"):
                playerX_change=0
                playerY_change=0
                
    a=random.randint(0,900)
    if a==2:
        if bala_state is "ready":
            balay=enimyy
            balax=enimyx
            atirar2(balax,balay)


    playerX+=playerX_change
    playery+=playerY_change
    
    if playerX <=0:
        playerX=0
    elif playerX>=736:
        playerX=736
        
    if playery<=407:
        playery=407
    
    elif playery>=530:
        playery=530
    #enimy movimento
    
    enimyx+=enimyx_change
    enimyy+=enimyx_change
    if enimyx <=0:
        enimyx_change=0.6
    elif enimyx>=736:
        enimyx_change=-0.6
        
    if enimyy >=200:
        enimyy=200
        enimyy_change=-0.6
    if enimyy<5:
        enimyy=5
    collision=iscollision(enimyx,enimyy,buletx,bulety) # colisom entre bala atirada do jogador e o inimigo
    collision2=iscollision(playerX,playery,balax,balay)
    if collision:
        bulety=0
        bulet_state="ready"
        pontos_value+=5
        enimyx_change=4
        enimyy_change=4
        isa=random.randint(1,5)
        isa=str(isa)
        a="./sounds/"+isa+".wav"

        enimy(enimyx,enimyy,)
       
      
        if vidainimigo_value>=1:
            vidainimigo_value-=1
        if vidainimigo_value==0:
            counter=counter*2
            mixer.music.stop()
            #somenemigo=mixer.Sound("6.wav")
            #somenemigo.play()
            a=mixer.Sound("./sounds/winsound.wav")
        
            a.play()
            
        # showGameOverScreen()
           
            over_font=pygame.font.Font("font.otf",64)
            over_text=font.render("Prosima Fase ",True,("red"))
            vidainimigo_value=counter
            balay_change+=0.4

            #running=False
        else:
            somenemigo=mixer.Sound(a)
            somenemigo.play()
    if collision2:
        balay=enimyy
        bala_state="ready"
        vida_value-=1
        if vida_value==0:
            a=mixer.Sound("./sounds/sound-gameover.wav")
        
            a.play()

            time.sleep(4)
            showGameOverScreen()
            running=False

#game over

        # this is to stop the bug song poor solutinon but im going to correct it soon
    #bullet movement
    if bulety<=0:
        bulety=480
        bulet_state="ready"
        somdetiro.stop()
    if bulet_state is "fire":
        atirar(buletx,bulety)
        bulety-=bulety_change
        
    #bala do inimigo
    if balay>=600:
        balay=enimyy
        bala_state="ready"
    if bala_state is "fire":
        atirar2(balax,balay)
        balay+=balay_change
        

    player(playerX,playery)
    enimy(enimyx,enimyy)
   
    mostrarpontos(textX,textY)
    mostrarvida(vidax,viday)
    mostrarvidainimiga(vidainimigax,vidainimigay)
    pygame.display.update()



