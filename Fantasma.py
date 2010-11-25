import pygame
import os
import random
import Objetos

class Fantasma:

    def __init__ (this):
        this.x            = 0
        this.y            = 0
        this.velX         = 0
        this.velY         = 0
        this.velocidade   = 2
        this.proxLinha    = 0
        this.proxColuna   = 0
        this.homeX        = 0
        this.homeY        = 0
        this.image        = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fantasmas"+os.sep+"1.png").convert_alpha()
                
    def andar(this):
        
        if this.x%32 == 0 and this.y%32 == 0:

            if this.y < Objetos.claude.y:
                this.velX = 0
                this.velY = this.velocidade
            elif this.y > Objetos.claude.y:
                this.velX = 0
                this.velY = -this.velocidade
            elif this.x < Objetos.claude.x:
                this.velX = this.velocidade
                this.velY = 0
            elif this.x > Objetos.claude.x:
                this.velX = -this.velocidade
                this.velY = 0
            
        this.proxLinha = int(((this.y + 16) / 32))
        this.proxColuna = int(((this.x + 16) / 32))
        
        while Objetos.nivel.verificaParede((this.x + this.velX, this.y + this.velY), (this.proxLinha, this.proxColuna)):# \
##           and not nivel.GetMapTile((this.proxLinha,this.proxColuna))==20 \
##           and not nivel.GetMapTile((this.proxLinha,this.proxColuna))==21:
            rand = random.randint(1,4)
            if rand == 1:
                this.velX = -this.velocidade
                this.velY = 0
                    
            elif rand == 2:
                this.velX = this.velocidade
                this.velY = 0
                    
            elif rand == 3:
                this.velX = 0
                this.velY = -this.velocidade
                    
            elif rand == 4:
                this.velX = 0
                this.velY = this.velocidade
        else:
            this.x += this.velX
            this.y += this.velY

        
    def printFantasma(this):
        
        Objetos.background.blit (this.image, (this.x, this.y))

    def colisao(this):
        if Objetos.claude.x - 16 <= this.x <= Objetos.claude.x + 16 and Objetos.claude.y - 16 <= this.y <= Objetos.claude.y + 16:
            Objetos.jogo.setModo(2)
