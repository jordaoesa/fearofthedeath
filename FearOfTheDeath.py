import pygame, os, time, sys
from pygame.locals import *

altura = 550
largura  = 820
background = pygame.display.set_mode((largura, altura),0,32)
pygame.display.set_caption("Fear Of The Death")
icon = pygame.image.load("images"+os.sep+"05 .png").convert_alpha()
pygame.display.set_icon(icon)

parede = pygame.sprite.Sprite()
parede.image = pygame.image.load("images"+os.sep+"block.png").convert_alpha()
parede.rect = parede.image.get_size()

bomb = pygame.sprite.Sprite()
bomb.image = pygame.image.load("images"+os.sep+"bomb1.png").convert_alpha()

pygame.font.init()
fonte = pygame.font.Font('images' + os.sep + 'FonteMenu.ttf',13,bold = False)
fonte2 = pygame.font.Font('images' + os.sep + 'FonteMenu2.ttf',13,bold = False)
fonte3 = pygame.font.Font('images' + os.sep + 'FonteMenu3.ttf',40,bold = False)
fonte4 = pygame.font.Font('images' + os.sep + 'FonteMenu4.ttf',15,bold = False)
fonteNum = pygame.font.Font('images' + os.sep + 'Numeros.ttf',18,bold = False)

sonic = []
for i in range(9):
    sonic.insert(i, pygame.sprite.Sprite())
    sonic[i].image = pygame.image.load("images"+os.sep+"sonic"+os.sep+"0"+str(i+1)+".png").convert_alpha()
    sonic[i].rect = sonic[i].image.get_size()
for i in range(9,32):
    sonic.insert(i, pygame.sprite.Sprite())
    sonic[i].image = pygame.image.load("images"+os.sep+"sonic"+os.sep+str(i+1)+".png").convert_alpha()
    sonic[i].rect = sonic[i].image.get_size()

matrizCampo = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,1,1,1,1,1,0,1,1,1,1,1,1],
               [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
               [1,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
               [1,0,1,0,1,0,0,1,0,0,0,1,1,0,1],
               [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
               [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
               [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#0 - bomba
#1 - Parede
#2 - player
#3 - nada

cont = 0
image = sonic[24].image
posX, posY = 180, 180
framesPorSegundo = 20
fps = pygame.time.Clock()
pos = [1,1]
podeAndar = [0,3]

vR, vL, vD, vU= False, False, False, False
score = 0

def sair():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

def terminou():
    while True:
        sair()
        for i in range(len(matrizCampo)):
            for j in range(len(matrizCampo[i])):
                if matrizCampo[i][j] == 1:
                    background.blit(parede.image, (i*41,j*35))
                if matrizCampo[i][j] == 0:
                    background.blit(bomb.image, (i*41,j*35))
                if matrizCampo[i][j] == 2:
                    background.blit(image, (pos[0]*41, pos[1]*35))

        fim = fonte3.render("YOU WIN", True, (255,255,255))
        fim2 = fonte3.render("SEU SCORE :", True, (255,255,255))
        fim3 = fonte3.render(str(score), True, (255,255,255))

        background.blit(fim, (350,200))
        background.blit(fim2, (340,250))
        background.blit(fim3, (360,300))
        
        background.blit(frase, (680,530))
        background.blit(numScore, (750,530))
        background.blit(vidas, (550,530))
        
        pygame.display.update()


while True:
    
    pressed_keys = pygame.key.get_pressed()
    sair()

    background.fill((0,0,0))

    ##FIM
    celulas = []
    for i in range(len(matrizCampo)):
        for j in range(len(matrizCampo[i])):
            if matrizCampo[i][j] == 0:
                celulas.append(matrizCampo[i][j])
                
    if len(celulas) == 0:
        terminou()
        #time.sleep(3)
        
    cont += 1
    if pressed_keys[K_RIGHT]:
        vR, vL, vD, vU= True, False, False, False
    if pressed_keys[K_LEFT]:
        vR, vL, vD, vU = False, True, False, False
    if pressed_keys[K_DOWN]:
        vR, vL, vD, vU = False, False, True, False
    if pressed_keys[K_UP]:
        vR, vL, vD, vU= False, False, False, True

    if vR:
        
        if cont <= 5: image = sonic[24].image
        elif 5 < cont <= 10: image = sonic[25].image
        elif 10 < cont <= 15: image = sonic[26].image
        elif 15 < cont <= 20: image = sonic[27].image
        elif 20 < cont <= 25: image = sonic[28].image
        elif 25 < cont <= 30: image = sonic[29].image
        elif 30 < cont <= 35: image = sonic[30].image
        elif 35 < cont <= 40: image = sonic[31].image
        
        if matrizCampo[int(pos[0]+1)][int(pos[1])] == 0:
            score += 30
##        elif matrizCampo[int(pos[0]+1)][int(pos[1])] == 3:
##            score -= 2
        if matrizCampo[int(pos[0]+1)][int(pos[1])] in podeAndar:
            matrizCampo[int(pos[0]+1)][int(pos[1])] = 2
            matrizCampo[int(pos[0])][int(pos[1])] = 3
            pos[0]+=1
    
    if vL:
        
        if cont <= 5: image = sonic[16].image
        elif 5 < cont <= 10: image = sonic[17].image
        elif 10 < cont <= 15: image = sonic[18].image
        elif 15 < cont <= 20: image = sonic[19].image
        elif 20 < cont <= 25: image = sonic[20].image
        elif 25 < cont <= 30: image = sonic[21].image
        elif 30 < cont <= 35: image = sonic[22].image
        elif 35 < cont <= 40: image = sonic[23].image

        if matrizCampo[int(pos[0]-1)][int(pos[1])] == 0:
            score += 30
##        elif matrizCampo[int(pos[0]-1)][int(pos[1])] == 3:
##            score -= 2
        if matrizCampo[int(pos[0]-1)][int(pos[1])] in podeAndar:
            matrizCampo[int(pos[0]-1)][int(pos[1])] = 2
            matrizCampo[int(pos[0])][int(pos[1])] = 3
            pos[0]-=1
    
    if vD:

        if cont <= 5: image = sonic[0].image
        elif 5 < cont <= 10: image = sonic[1].image
        elif 10 < cont <= 15: image = sonic[2].image
        elif 15 < cont <= 20: image = sonic[3].image
        elif 20 < cont <= 25: image = sonic[4].image
        elif 25 < cont <= 30: image = sonic[5].image
        elif 30 < cont <= 35: image = sonic[6].image
        elif 35 < cont <= 40: image = sonic[7].image
        
        if matrizCampo[int(pos[0])][int(pos[1]+1)] == 0:
            score += 30
##        elif matrizCampo[int(pos[0])][int(pos[1]+1)] == 3:
##            score -= 2
        if matrizCampo[int(pos[0])][int(pos[1]+1)] in podeAndar:
            matrizCampo[int(pos[0])][int(pos[1]+1)] = 2
            matrizCampo[int(pos[0])][int(pos[1])] = 3
            pos[1]+=1
    
    if vU:

        if cont <= 5: image = sonic[8].image
        elif 5 < cont <= 10: image = sonic[9].image
        elif 10 < cont <= 15: image = sonic[10].image
        elif 15 < cont <= 20: image = sonic[11].image
        elif 20 < cont <= 25: image = sonic[12].image
        elif 25 < cont <= 30: image = sonic[13].image
        elif 30 < cont <= 35: image = sonic[14].image
        elif 35 < cont <= 40: image = sonic[15].image
        
        if matrizCampo[int(pos[0])][int(pos[1]-1)] == 0:
            score += 30
##        elif matrizCampo[int(pos[0])][int(pos[1]-1)] == 3:
##            score -= 2
        if matrizCampo[int(pos[0])][int(pos[1]-1)] in podeAndar:
            matrizCampo[int(pos[0])][int(pos[1]-1)] = 2
            matrizCampo[int(pos[0])][int(pos[1])] = 3
            pos[1]-=1

    if cont == 40: cont = 0


    for i in range(len(matrizCampo)):
        for j in range(len(matrizCampo[i])):
        
            if matrizCampo[i][j] == 1:
                background.blit(parede.image, (i*41,j*35))
            if matrizCampo[i][j] == 0:
                background.blit(bomb.image, (i*41,j*35))
            if matrizCampo[i][j] == 2:
                background.blit(image, (pos[0]*41, pos[1]*35))

    vida = 111 #DEFINE 3 VIDAS PARA O USUARIO
    frase = fonte.render("Score: ",True,(255,255,255))
    numScore = fonteNum.render(str(score), True, (255,255,255))
    vidas = fonte.render("Vidas: "+str(vida),True,(255,255,255))
    background.blit(frase, (680,530))
    background.blit(numScore, (750,530))
    background.blit(vidas, (550,530))
    fps.tick(framesPorSegundo)
    pygame.display.update()
