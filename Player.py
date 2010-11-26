import pygame
import os
import Objetos

class Sonic:
    
    def __init__ (this):
        this.direcao      = "direita"
        this.x            = 0
        this.y            = 0
        this.velX         = 0
        this.velY         = 0
        this.velocidade   = 2
        this.proxLinha    = 0
        this.proxColuna   = 0
        this.homeX        = 0
        this.homeY        = 0
        this.images       = {}
            
        this.sndGranaNum = 0
        
    def andar(this):
        
        this.proxLinha = int(((this.y + 19) / 32))
        this.proxColuna = int(((this.x + 19) / 32))
        
        if not Objetos.nivel.verificaParede((this.x + this.velX, this.y + this.velY), (this.proxLinha, this.proxColuna)):
            this.x += this.velX
            this.y += this.velY
            
            Objetos.nivel.comida((this.x, this.y), (this.proxLinha, this.proxColuna))  ##-- REMOVE AS NOTAS E PLAY SOM
            Objetos.nivel.portais((this.x, this.y), (this.proxLinha, this.proxColuna)) ##-- PERMITE A PASSAGEM NOS PORTAIS

        else:
            this.velX = 0
            this.velY = 0
        
    def printSonic(this):
        #print nivel.mapa
        if Objetos.jogo.modo == 3:
            return False
        
        if this.velX > 0:
            this.images = Objetos.sonicD
        elif this.velX < 0:
            this.images = Objetos.sonicE
        elif this.velY > 0:
            this.images = Objetos.sonicB
        elif this.velY < 0:
            this.images = Objetos.sonicC
        else:
            this.animaSonic = 0
            if this.direcao == "direita":
                this.images = Objetos.sonicD
            elif this.direcao == "esquerda":
                this.images = Objetos.sonicE
            elif this.direcao == "cima":
                this.images = Objetos.sonicC
            elif this.direcao == "baixo":
                this.images = Objetos.sonicB
            
        Objetos.background.blit (this.images[int(this.animaSonic)], (this.x - Objetos.jogo.posicaoPixel[0], this.y - Objetos.jogo.posicaoPixel[1]))
        
        if Objetos.jogo.modo == 1:
            if not this.velX == 0 or not this.velY == 0:
                this.animaSonic += 0.3
            if int(this.animaSonic) == 3:
                this.animaSonic = 0
