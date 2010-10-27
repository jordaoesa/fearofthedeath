import pygame, os, time
from pygame.locals import *
from sys import exit

altura = 480
largura  = 640
background = pygame.display.set_mode((largura, altura),0,32)


fundo = pygame.image.load("fundo3.png").convert()

parede = pygame.sprite.Sprite()
parede.image = pygame.image.load("parede3.png").convert_alpha()
parede.rect = parede.image.get_size()

bomb = pygame.sprite.Sprite()
bomb.image = pygame.image.load("images/bomb.png").convert_alpha()


pacCim, pacBai, pacEsq, pacDir = [], [], [], []
for i in range(4):
    pacCim.insert(i, pygame.sprite.Sprite())
    pacCim[i].image = pygame.image.load("images" + os.sep + "paccim"+str(i+1) + ".png").convert_alpha()
    pacCim[i].rect = pacCim[i].image.get_size()

    pacBai.insert(i, pygame.sprite.Sprite())
    pacBai[i].image = pygame.image.load("images" + os.sep + "pacbai"+str(i+1) + ".png").convert_alpha()
    pacBai[i].rect = pacBai[i].image.get_size()

    pacEsq.insert(i, pygame.sprite.Sprite())
    pacEsq[i].image = pygame.image.load("images" + os.sep + "pacesq"+str(i+1) + ".png").convert_alpha()
    pacEsq[i].rect = pacEsq[i].image.get_size()

    pacDir.insert(i, pygame.sprite.Sprite())
    pacDir[i].image = pygame.image.load("images" + os.sep + "pacdir"+str(i+1) + ".png").convert_alpha()
    pacDir[i].rect = pacDir[i].image.get_size()


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
image = pacDir[0].image
framesPorSegundo = 10
fps = pygame.time.Clock()
pos = [1,1]
podeAndar = [0,3]
vR, vL, vD, vU = False, False, False, False
while True:

    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()


    background.blit(fundo, (0,0))

    ##Update sprite a posicao
    cont += 1
    
    if pressed_keys[K_RIGHT]:
        vR, vL, vD, vU = True, False, False, False
    if pressed_keys[K_LEFT]:
        vR, vL, vD, vU = False, True, False, False
    if pressed_keys[K_DOWN]:
        vR, vL, vD, vU = False, False, True, False
    if pressed_keys[K_UP]:
        vR, vL, vD, vU = False, False, False, True

    if vR:
        if cont <= 5: image = pacDir[0].image
        elif 5 < cont <= 10: image = pacDir[1].image
        elif 10 < cont <= 15: image = pacDir[2].image
        elif 15 < cont <= 20: image = pacDir[3].image

        if matrizCampo[pos[0]+1][pos[1]] in podeAndar:
            matrizCampo[pos[0]+1][pos[1]] = 2
            matrizCampo[pos[0]][pos[1]] = 3
            pos[0]+=1

    
    if vL:        
        if cont <= 5: image = pacEsq[0].image
        elif 5 < cont <= 10: image = pacEsq[1].image
        elif 10 < cont <= 15: image = pacEsq[2].image
        elif 15 < cont <= 20: image = pacEsq[3].image

        if matrizCampo[pos[0]-1][pos[1]] in podeAndar:
            matrizCampo[pos[0]-1][pos[1]] = 2
            matrizCampo[pos[0]][pos[1]] = 3
            pos[0]-=1

    
    if vD:
        if cont <= 5: image = pacBai[0].image
        elif 5 < cont <= 10: image = pacBai[1].image
        elif 10 < cont <= 15: image = pacBai[2].image
        elif 15 < cont <= 20: image = pacBai[3].image

        if matrizCampo[pos[0]][pos[1]+1] in podeAndar:
            matrizCampo[pos[0]][pos[1]+1] = 2
            matrizCampo[pos[0]][pos[1]] = 3
            pos[1]+=1

    
    if vU:
        if cont <= 5: image = pacCim[0].image
        elif 5 < cont <= 10: image = pacCim[1].image
        elif 10 < cont <= 15: image = pacCim[2].image
        elif 15 < cont <= 20: image = pacCim[3].image

        if matrizCampo[pos[0]][pos[1]-1] in podeAndar:
            matrizCampo[pos[0]][pos[1]-1] = 2
            matrizCampo[pos[0]][pos[1]] = 3
            pos[1]-=1

    if cont == 20: cont = 0


    for i in range(len(matrizCampo)):
        for j in range(len(matrizCampo[i])):
            if matrizCampo[i][j] == 1:
                background.blit(parede.image, (i*20,j*20))
            if matrizCampo[i][j] == 0:
                background.blit(bomb.image, (i*20,j*20))
            if matrizCampo[i][j] == 2:
                background.blit(image, (pos[0]*20, pos[1]*20))


    #background.blit(image,(posX, posY))
    fps.tick(framesPorSegundo)
    pygame.display.update()
