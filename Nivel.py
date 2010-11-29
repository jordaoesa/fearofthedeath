import pygame
import Objetos

class Nivel:
    
    def __init__ (this):
        this.qtdTilesX   = 0
        this.qtdTilesY   = 0
        this.mapa        = {}
        this.acumulo     = 0
        this.animaColete = 0
        this.animaRoda  = 0
        
    def SetMapTile (this, (linha, coluna), valor):
        this.mapa[ coluna + (linha * this.qtdTilesX) ] = valor
        
    def GetMapTile (this, (linha, coluna)):
        if linha >= 0 and linha < this.qtdTilesY and coluna >= 0 and coluna < this.qtdTilesX:
            return this.mapa[ coluna + (linha * this.qtdTilesX) ]
        else:
            return 0

    def comida(this, (sonicX, sonicY), (linha, coluna)):
    
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
            
                if  (sonicX - (cooluna * 32) < 32) and (sonicX - (cooluna * 32) > -32) and (sonicY - (liinha * 32) < 32) and (sonicY - (liinha * 32) > -32):
                    result = Objetos.nivel.GetMapTile((liinha, cooluna))

################### REMOCAO DA GRANA       
                    if result == 2: ##-- GRANA
                        Objetos.nivel.SetMapTile((liinha, cooluna), 0)
                        Objetos.sndMoeda.play() ##--PLAY SOM                        
                        Objetos.nivel.acumulo -= 1
                        Objetos.jogo.pontos(10)
                        if Objetos.nivel.acumulo == 0:
                            Objetos.jogo.setModo( 4 )
                            
################### REMOCAO DO ESCUDO                       
                    elif result == 7 or result == 6: ##ESCUDO PROTETOR
                        Objetos.nivel.SetMapTile((liinha, cooluna), 0)
                        #Objetos.player.escudo = True
                        Objetos.sonic.escudo +=1 ##-- PROTECAO
                        Objetos.sonic.limiteEscudo += 500 ##-- MAIOR VELOCIDADE
                        Objetos.jogo.pontos(100)

### PORTAS HORIZONTAIS E VERTICAIS

    def portais(this, (sonicX, sonicY), (linha, coluna)):
        
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
                
                if  (sonicX - (cooluna * 32) < 32) and (sonicX - (cooluna * 32) > -32) and (sonicY - (liinha * 32) < 32) and (sonicY - (liinha * 32) > -32):
                # check the offending tile ID
                    result = Objetos.nivel.GetMapTile((liinha, cooluna))
                
                    if result == 20: ##PORTA HORIZONTAL
                        for i in range(0, Objetos.nivel.qtdTilesX):
                            if not i == cooluna:
                                if Objetos.nivel.GetMapTile((liinha, i)) == 20: ##PORTA HORIZONTAL
                                    Objetos.sonic.x = i * 32
                                    
                                    if Objetos.sonic.velX > 0:
                                        Objetos.sonic.x += 32
                                    else:
                                        Objetos.sonic.x -= 32
                                        
                    elif result == 21: ##PORTA VERTICAL
                        for i in range(0, Objetos.nivel.qtdTilesY):
                            if not i == liinha:
                                if Objetos.nivel.GetMapTile((i, cooluna)) == 21: ##PORTA VERTICAL
                                    Objetos.sonic.y = i * 32
                                    
                                    if Objetos.sonic.velY > 0:
                                        Objetos.sonic.y += 32
                                    else:
                                        Objetos.sonic.y -= 32

### PORTAS HORIZONTAIS E VERTICAIS PARA OS FANTASMAS
    def portaisF(this, (fX, fY), (linha, coluna), fant):
        
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
                
                if  (fX - (cooluna * 32) < 32) and (fX - (cooluna * 32) > -32) and (fY - (liinha * 32) < 32) and (fY - (liinha * 32) > -32):
                # check the offending tile ID
                    result = Objetos.nivel.GetMapTile((liinha, cooluna))
                
                    if result == 20: ##PORTA HORIZONTAL
                        for i in range(0, Objetos.nivel.qtdTilesX):
                            if not i == cooluna:
                                if Objetos.nivel.GetMapTile((liinha, i)) == 20: ##PORTA HORIZONTAL
                                    fant.x = i * 32
                                    
                                    if fant.velX > 0:
                                        fant.x += 32
                                    else:
                                        fant.x -= 32
                                        
                    elif result == 21: ##PORTA VERTICAL
                        for i in range(0, Objetos.nivel.qtdTilesY):
                            if not i == liinha:
                                if Objetos.nivel.GetMapTile((i, cooluna)) == 21: ##PORTA VERTICAL
                                    fant.y = i * 32
                                    
                                    if fant.velY > 0:
                                        fant.y += 32
                                    else:
                                        fant.y -= 32

### VERIFICA SE EH PAREDE
    def parede(this, (linha, coluna)):

        celula = Objetos.nivel.GetMapTile((linha, coluna))
        if celula == 1:
            return True
        else:
            return False

### VERIFICA SE VAI BATER NA PAREDE
    def verificaParede(this, (posX, posY), (linha, coluna)):
        
        for liinha in range(linha-1, linha+2):
            for cooluna in range(coluna-1, coluna+2):
                if  (posX - (cooluna * 32) < 32) and (posX - (cooluna * 32) > -32) and (posY - (liinha * 32) < 32) and (posY - (liinha * 32) > -32):
                    if this.parede((liinha, cooluna)):
                        return True
        return False

    def printMapa (this):
        
        this.animaColete += 1
        this.animaRoda += 1
        
        if this.animaColete == 116: ##FAZ AS BOLINHAS PISCAREM
            this.animaColete = 0
            
        if this.animaRoda == 20:
            this.animaRoda = 0
        
        
        for linha in range(-1, Objetos.jogo.qtdTilesTela[0] +1):
            for coluna in range(-1, Objetos.jogo.qtdTilesTela[1] +1):

                tileAtual = this.GetMapTile((Objetos.jogo.proximoTile[0] + linha, Objetos.jogo.proximoTile[1] + coluna))
                if not tileAtual == 0 and not tileAtual == 20 and not tileAtual == 21: ## NADA and PORTA H and PORTA V
                    image = pygame.image
                    
################### BLITA PROTECAO
                    if tileAtual == 7 or tileAtual == 6: ##ESCUDO PROTETOR
                        if this.animaColete <= 5:     image = Objetos.colete[0]
                        elif this.animaColete <= 10:  image = Objetos.colete[1]
                        elif this.animaColete <= 15:  image = Objetos.colete[2]
                        elif this.animaColete <= 20:  image = Objetos.colete[3]
                        elif this.animaColete <= 25:  image = Objetos.colete[4]
                        elif this.animaColete <= 30:  image = Objetos.colete[5]
                        elif this.animaColete <= 35:  image = Objetos.colete[6]
                        elif this.animaColete <= 40:  image = Objetos.colete[7]
                        elif this.animaColete <= 45:  image = Objetos.colete[8]
                        elif this.animaColete <= 50:  image = Objetos.colete[9]
                        elif this.animaColete <= 55:  image = Objetos.colete[10]
                        elif this.animaColete <= 60:  image = Objetos.colete[11]
                        elif this.animaColete <= 65:  image = Objetos.colete[12]
                        elif this.animaColete <= 70:  image = Objetos.colete[13]
                        elif this.animaColete <= 75:  image = Objetos.colete[14]
                        elif this.animaColete <= 80:  image = Objetos.colete[15]
                        elif this.animaColete <= 85:  image = Objetos.colete[16]
                        elif this.animaColete <= 90:  image = Objetos.colete[17]
                        elif this.animaColete <= 95:  image = Objetos.colete[18]
                        elif this.animaColete <= 100: image = Objetos.colete[19]
                        elif this.animaColete <= 105: image = Objetos.colete[20]
                        elif this.animaColete <= 110: image = Objetos.colete[21]
                        elif this.animaColete <= 115: image = Objetos.colete[22]

                        Objetos.background.blit(image, (coluna * 32 - Objetos.jogo.deslocamento[0], linha * 32 - Objetos.jogo.deslocamento[1]) )
                        
################### BLITA RODELA
                    if tileAtual == 2:
                        if this.animaRoda <= 5: image    = Objetos.roda[0]
                        elif this.animaRoda <= 10: image = Objetos.roda[1]
                        elif this.animaRoda <= 15: image = Objetos.roda[2]
                        elif this.animaRoda <= 20: image = Objetos.roda[3]

                        Objetos.background.blit(image, (coluna * 32 - Objetos.jogo.deslocamento[0], linha * 32 - Objetos.jogo.deslocamento[1]) )
################### BLITA AS PAREDES
                    elif tileAtual == 1:
                        Objetos.background.blit(Objetos.parede[ Objetos.jogo.getNivel() ], (coluna * 32 - Objetos.jogo.deslocamento[0], linha * 32 - Objetos.jogo.deslocamento[1]) )
        
    def loadNivel(this, nivelNum):

        this.qtdTilesX   = 19
        this.qtdTilesY   = 21
        this.mapa        = {}
        this.numLinha    = 0
        this.acumulo     = 0
        this.matrizCampo = []
            
        if nivelNum == 1:
            this.matrizCampo = Objetos.matriz1
        elif nivelNum == 2:
            this.matrizCampo = Objetos.matriz2
        elif nivelNum == 3:
            this.matrizCampo = Objetos.matriz3
            

        for l in range(this.qtdTilesY):
            for k in range(this.qtdTilesX):
                this.SetMapTile((this.numLinha, k), this.matrizCampo[l][k])
                
                thisID = this.matrizCampo[l][k]
                if thisID == 4:
                    Objetos.sonic.homeX = k * 32
                    Objetos.sonic.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                    
##                elif thisID == 6:
##                    print "6"
##                    protect.homeX = k * 32
##                    protect.homeY = this.numLinha * 32
##                    this.SetMapTile((this.numLinha, k), 0 )
##                elif thisID == 7:
##                    print "7"
##                    protect1.homeX = k * 32
##                    protect1.homeY = this.numLinha * 32
##                    this.SetMapTile((this.numLinha, k), 0 )
##                elif thisID == 8:
##                    print "8"
##                    protect2.homeX = k * 32
##                    protect2.homeY = this.numLinha * 32
##                    this.SetMapTile((this.numLinha, k), 0 )
##                elif thisID == 9:
##                    print "9"
##                    protect3.homeX = k * 32
##                    protect3.homeY = this.numLinha * 32
##                    this.SetMapTile((this.numLinha, k), 0 )
                    
                elif thisID == 10:
                    Objetos.fantasma.homeX = k * 32
                    Objetos.fantasma.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 11:
                    Objetos.fantasma1.homeX = k * 32
                    Objetos.fantasma1.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 12:
                    Objetos.fantasma2.homeX = k * 32
                    Objetos.fantasma2.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 13:
                    Objetos.fantasma3.homeX = k * 32
                    Objetos.fantasma3.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 2:
                    Objetos.nivel.acumulo += 1
                    
            this.numLinha += 1

        this.reiniciar()
        
    def reiniciar(this):
        
        Objetos.fantasma.x         = Objetos.fantasma.homeX
        Objetos.fantasma.y         = Objetos.fantasma.homeY
        Objetos.fantasma.velX      = 2
        Objetos.fantasma.velY      = 0

        Objetos.fantasma1.x        = Objetos.fantasma1.homeX
        Objetos.fantasma1.y        = Objetos.fantasma1.homeY
        Objetos.fantasma1.velX     = -2
        Objetos.fantasma1.velY     = 0

        Objetos.fantasma2.x        = Objetos.fantasma2.homeX
        Objetos.fantasma2.y        = Objetos.fantasma2.homeY
        Objetos.fantasma2.velX     = 0
        Objetos.fantasma2.velY     = 2

        Objetos.fantasma3.x        = Objetos.fantasma3.homeX
        Objetos.fantasma3.y        = Objetos.fantasma3.homeY
        Objetos.fantasma3.velX     = 0
        Objetos.fantasma3.velY     = -2

        Objetos.sonic.x            = Objetos.sonic.homeX
        Objetos.sonic.y            = Objetos.sonic.homeY
        Objetos.sonic.velX         = 0
        Objetos.sonic.velY         = 0
        Objetos.sonic.images       = Objetos.imgPlayer["playerD"]
        Objetos.sonic.animaSonic   = 0
