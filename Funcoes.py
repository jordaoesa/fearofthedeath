import pygame
from pygame.locals import *
import Objetos

def verificaTeclas():

    pressed = pygame.key.get_pressed()
    
    ##--- CHECA SAIDA
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Objetos.start.stopMusicas()
                Objetos.grava.clearUser()
                Objetos.nivel.reiniciar()
                Objetos.menu.__init__()
                Objetos.menu.run()
                
    ##--- CHECA MOVIMENTOS
    if Objetos.jogo.modo == 1:
        if pressed[K_RIGHT]:
            if not Objetos.nivel.verificaParede((Objetos.sonic.x + Objetos.sonic.velocidade, Objetos.sonic.y), (Objetos.sonic.proxLinha, Objetos.sonic.proxColuna)): 
                Objetos.sonic.velX = Objetos.sonic.velocidade
                Objetos.sonic.velY = 0
                Objetos.sonic.direcao = "direita"
                
        elif pressed[K_LEFT]:
            if not Objetos.nivel.verificaParede((Objetos.sonic.x - Objetos.sonic.velocidade, Objetos.sonic.y), (Objetos.sonic.proxLinha, Objetos.sonic.proxColuna)): 
                Objetos.sonic.velX = -Objetos.sonic.velocidade
                Objetos.sonic.velY = 0
                Objetos.sonic.direcao = "esquerda"
            
        elif pressed[K_DOWN]:
            if not Objetos.nivel.verificaParede((Objetos.sonic.x, Objetos.sonic.y + Objetos.sonic.velocidade), (Objetos.sonic.proxLinha, Objetos.sonic.proxColuna)): 
                Objetos.sonic.velX = 0
                Objetos.sonic.velY = Objetos.sonic.velocidade
                Objetos.sonic.direcao = "baixo"
            
        elif pressed[K_UP]:
            if not Objetos.nivel.verificaParede((Objetos.sonic.x, Objetos.sonic.y - Objetos.sonic.velocidade), (Objetos.sonic.proxLinha, Objetos.sonic.proxColuna)):
                Objetos.sonic.velX = 0
                Objetos.sonic.velY = -Objetos.sonic.velocidade
                Objetos.sonic.direcao = "cima"
