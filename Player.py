import pygame
import os
import Objetos

class Sonic:
    
    def __init__ (this):
        this.direcao      = "direita"
        this.x            = 0
        this.y            = 0
        this.velX         = 2
        this.velY         = 0
        this.velocidade   = 2
        this.proxLinha    = 0
        this.proxColuna   = 0
        this.homeX        = 0
        this.homeY        = 0
        this.images       = {}
        #this.escudo       = 0
        this.tempoEscudo  = 0
        this.limiteEscudo = 0
        
    def andar(this):

##        if this.tempoEscudo >= this.limiteEscudo:
##            this.escudo = 0
##            this.tempoEscudo = 0
##        if this.escudo > 0:
##            this.velocidade = 4
##            Objetos.fantasma.velocidade = -1
##            Objetos.fantasma1.velocidade = -1
##            Objetos.fantasma2.velocidade = -1
##            Objetos.fantasma3.velocidade = -1
##        else:
##            this.limiteEscudo = 0
##            this.velocidade = 2
##            Objetos.fantasma.velocidade = 1
##            Objetos.fantasma1.velocidade = 1
##            Objetos.fantasma2.velocidade = 1
##            Objetos.fantasma3.velocidade = 1
        if this.tempoEscudo >= this.limiteEscudo:
            #this.escudo = 0
            this.tempoEscudo = 0
        if this.tempoEscudo > 0:
            this.velocidade = 4
            Objetos.fantasma.velocidade = -1
            Objetos.fantasma1.velocidade = -1
            Objetos.fantasma2.velocidade = -1
            Objetos.fantasma3.velocidade = -1
        else:
            this.limiteEscudo = 0
            this.velocidade = 2
            Objetos.fantasma.velocidade = 1
            Objetos.fantasma1.velocidade = 1
            Objetos.fantasma2.velocidade = 1
            Objetos.fantasma3.velocidade = 1
            
        this.proxLinha = int(((this.y + 14) / 32))
        this.proxColuna = int(((this.x + 14) / 32))
        
        if not Objetos.nivel.verificaParede((this.x + this.velX, this.y + this.velY), (this.proxLinha, this.proxColuna)):
            this.x += this.velX
            this.y += this.velY
            
            Objetos.nivel.comida((this.x, this.y), (this.proxLinha, this.proxColuna))  ##-- REMOVE AS NOTAS E PLAY SOM
            Objetos.nivel.portais((this.x, this.y), (this.proxLinha, this.proxColuna)) ##-- PERMITE A PASSAGEM NOS PORTAIS

        else:
            this.velX = 0
            this.velY = 0
        
    def printSonic(this):

        if Objetos.jogo.modo == 3:
            return False

        if this.velX > 0:
            this.images = Objetos.imgPlayer["playerD"]
        elif this.velX < 0:
            this.images = Objetos.imgPlayer["playerE"]
        elif this.velY > 0:
            this.images = Objetos.imgPlayer["playerB"]
        elif this.velY < 0:
            this.images = Objetos.imgPlayer["playerC"]
        else:
            this.animaSonic = 0
            if this.direcao == "direita":
                this.images = Objetos.imgPlayer["playerD"]
            elif this.direcao == "esquerda":
                this.images = Objetos.imgPlayer["playerE"]
            elif this.direcao == "cima":
                this.images = Objetos.imgPlayer["playerC"]
            elif this.direcao == "baixo":
                this.images = Objetos.imgPlayer["playerB"]
            
        Objetos.background.blit (this.images[int(this.animaSonic)], (this.x - Objetos.jogo.posicaoPixel[0], this.y - Objetos.jogo.posicaoPixel[1]))
        
        if Objetos.jogo.modo == 1:
            if not this.velX == 0 or not this.velY == 0:
                this.animaSonic += 0.2
            if int(this.animaSonic) == 3:
                this.animaSonic = 0
