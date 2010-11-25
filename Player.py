import pygame, os
from pygame.locals import *
import Objetos

class Claude:
    
    def __init__ (this):
        this.direcao      = "direita"
        this.x            = 0
        this.y            = 0
        this.velX         = 0
        this.velY         = 0
        this.velocidade   = 4
        this.proxLinha    = 0
        this.proxColuna   = 0
        this.homeX        = 0
        this.homeY        = 0
        this.esquerda     = {}
        this.direita      = {}
        this.cima         = {}
        this.baixo        = {}
        this.images       = {}
        
        for i in range(0, 6):
            this.esquerda[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"gtaMini"+os.sep+"1" + str(i) + ".png").convert_alpha()
            this.direita[i]  = pygame.image.load("data"+os.sep+"sprites"+os.sep+"gtaMini"+os.sep+"0" + str(i) + ".png").convert_alpha()
            this.cima[i]     = pygame.image.load("data"+os.sep+"sprites"+os.sep+"gtaMini"+os.sep+"2" + str(i) + ".png").convert_alpha()
            this.baixo[i]    = pygame.image.load("data"+os.sep+"sprites"+os.sep+"gtaMini"+os.sep+"3" + str(i) + ".png").convert_alpha()
            
        this.sndGranaNum = 0
        
    def andar(this):
        
        this.proxLinha = int(((this.y + 16) / 32))
        this.proxColuna = int(((this.x + 16) / 32))
        
        if not Objetos.nivel.verificaParede((this.x + this.velX, this.y + this.velY), (this.proxLinha, this.proxColuna)):
            this.x += this.velX
            this.y += this.velY
            #nivel.matrizCampo[this.proxLinha][this.proxColuna] = 4
            #nivel.matrizCampo[this.proxLinha-1][this.proxColuna-1] = 0
            #print nivel.matrizCampo
            Objetos.nivel.comida((this.x, this.y), (this.proxLinha, this.proxColuna))  ##-- REMOVE AS NOTAS E PLAY SOM
            Objetos.nivel.portais((this.x, this.y), (this.proxLinha, this.proxColuna)) ##-- PERMITE A PASSAGEM NOS PORTAIS

        else:
            this.velX = 0
            this.velY = 0
        
    def printClaude(this):
        #print nivel.mapa
        if Objetos.jogo.modo == 3:
            return False
        
        if this.velX > 0:
            this.images = this.direita
        elif this.velX < 0:
            this.images = this.esquerda
        elif this.velY > 0:
            this.images = this.baixo
        elif this.velY < 0:
            this.images = this.cima
        else:
            this.animaClaude = 0
            if this.direcao == "direita":
                this.images = this.direita
            elif this.direcao == "esquerda":
                this.images = this.esquerda
            elif this.direcao == "cima":
                this.images = this.cima
            elif this.direcao == "baixo":
                this.images = this.baixo
            
        Objetos.background.blit (this.images[int(this.animaClaude)], (this.x - Objetos.jogo.posicaoPixel[0], this.y - Objetos.jogo.posicaoPixel[1]))
        
        if Objetos.jogo.modo == 1:
            if not this.velX == 0 or not this.velY == 0:
                this.animaClaude += 0.3
            if int(this.animaClaude) == 6:
                this.animaClaude = 0
