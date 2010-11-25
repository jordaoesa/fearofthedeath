import pygame
import Objetos

class Nivel:
    
    def __init__ (this):
        this.qtdTilesX   = 0
        this.qtdTilesY   = 0
        this.mapa        = {}
        this.acumulo     = 0
        this.animaColete = 0
        this.animaGrana  = 0
        
    def SetMapTile (this, (linha, coluna), valor):
        this.mapa[ coluna + (linha * this.qtdTilesX) ] = valor
        
    def GetMapTile (this, (linha, coluna)):
        if linha >= 0 and linha < this.qtdTilesY and coluna >= 0 and coluna < this.qtdTilesX:
            return this.mapa[ coluna + (linha * this.qtdTilesX) ]
        else:
            return 0

    def comida(this, (claudeX, claudeY), (linha, coluna)):
    
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
            
                if  (claudeX - (cooluna * 32) < 32) and (claudeX - (cooluna * 32) > -32) and (claudeY - (liinha * 32) < 32) and (claudeY - (liinha * 32) > -32):
                    result = Objetos.nivel.GetMapTile((liinha, cooluna))

################### REMOCAO DA GRANA       
                    if result == 2: ##-- GRANA
                        Objetos.nivel.SetMapTile((liinha, cooluna), 0)
                        #nivel.matrizCampo[liinha][cooluna] = 4
                        #nivel.matrizCampo[liinha-1][cooluna] = 0
##                        print nivel.mapa
                        #sndGrana[claude.sndGranaNum].play()
                        #claude.sndGranaNum = 1 - claude.sndGranaNum
                        
                        Objetos.nivel.acumulo -= 1
                        Objetos.jogo.pontos(10)
                        if Objetos.nivel.acumulo == 0:
                            Objetos.jogo.setModo( 4 )
                            
################### REMOCAO DO ESCUDO                       
                    elif result == 7: ##ESCUDO PROTETOR
                        Objetos.nivel.SetMapTile((liinha, cooluna), 0)
                        #snd_powerpellet.play()
                        Objetos.jogo.pontos(100)

### PORTAS HORIZONTAIS E VERTICAIS

    def portais(this, (claudeX, claudeY), (linha, coluna)):
        
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
                
                if  (claudeX - (cooluna * 32) < 32) and (claudeX - (cooluna * 32) > -32) and (claudeY - (liinha * 32) < 32) and (claudeY - (liinha * 32) > -32):
                # check the offending tile ID
                    result = Objetos.nivel.GetMapTile((liinha, cooluna))
                
                    if result == 20: ##PORTA HORIZONTAL
                        for i in range(0, Objetos.nivel.qtdTilesX):
                            if not i == cooluna:
                                if Objetos.nivel.GetMapTile((liinha, i)) == 20: ##PORTA HORIZONTAL
                                    Objetos.claude.x = i * 32
                                    
                                    if Objetos.claude.velX > 0:
                                        Objetos.claude.x += 32
                                    else:
                                        Objetos.claude.x -= 32
                                        
                    elif result == 21: ##PORTA VERTICAL
                        for i in range(0, Objetos.nivel.qtdTilesY):
                            if not i == liinha:
                                if Objetos.nivel.GetMapTile((i, cooluna)) == 21: ##PORTA VERTICAL
                                    Objetos.claude.y = i * 32
                                    
                                    if Objetos.claude.velY > 0:
                                        Objetos.claude.y += 32
                                    else:
                                        Objetos.claude.y -= 32

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
        this.animaGrana += 1
        
        if this.animaColete == 116: ##FAZ AS BOLINHAS PISCAREM
            this.animaColete = 0
            
        if this.animaGrana == 181:
            this.animaGrana = 0
        
        
        for linha in range(-1, Objetos.jogo.qtdTilesTela[0] +1):
            for coluna in range(-1, Objetos.jogo.qtdTilesTela[1] +1):

                tileAtual = this.GetMapTile((Objetos.jogo.proximoTile[0] + linha, Objetos.jogo.proximoTile[1] + coluna))
                if not tileAtual == 0 and not tileAtual == 20 and not tileAtual == 21 and not tileAtual == 6: ## NADA and PORTA H and PORTA V
                    image = pygame.image
                    
################### BLITA PROTECAO
                    if tileAtual == 7: ##ESCUDO PROTETOR
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
                        
################### BLITA GRANA
                    elif tileAtual == 2:
                        if this.animaGrana <= 5:     image = Objetos.grana[0]
                        elif this.animaGrana <= 10:  image = Objetos.grana[1]
                        elif this.animaGrana <= 15:  image = Objetos.grana[2]
                        elif this.animaGrana <= 20:  image = Objetos.grana[3]
                        elif this.animaGrana <= 25:  image = Objetos.grana[4]
                        elif this.animaGrana <= 30:  image = Objetos.grana[5]
                        elif this.animaGrana <= 35:  image = Objetos.grana[6]
                        elif this.animaGrana <= 40:  image = Objetos.grana[7]
                        elif this.animaGrana <= 45:  image = Objetos.grana[8]
                        elif this.animaGrana <= 50:  image = Objetos.grana[9]
                        elif this.animaGrana <= 55:  image = Objetos.grana[10]
                        elif this.animaGrana <= 60:  image = Objetos.grana[11]
                        elif this.animaGrana <= 65:  image = Objetos.grana[12]
                        elif this.animaGrana <= 70:  image = Objetos.grana[13]
                        elif this.animaGrana <= 75:  image = Objetos.grana[14]
                        elif this.animaGrana <= 80:  image = Objetos.grana[15]
                        elif this.animaGrana <= 85:  image = Objetos.grana[16]
                        elif this.animaGrana <= 90:  image = Objetos.grana[17]
                        elif this.animaGrana <= 95:  image = Objetos.grana[18]
                        elif this.animaGrana <= 100: image = Objetos.grana[19]
                        elif this.animaGrana <= 105: image = Objetos.grana[20]
                        elif this.animaGrana <= 110: image = Objetos.grana[21]
                        elif this.animaGrana <= 115: image = Objetos.grana[22]
                        elif this.animaGrana <= 120: image = Objetos.grana[23]
                        elif this.animaGrana <= 125: image = Objetos.grana[24]
                        elif this.animaGrana <= 130: image = Objetos.grana[25]
                        elif this.animaGrana <= 135: image = Objetos.grana[26]
                        elif this.animaGrana <= 140: image = Objetos.grana[27]
                        elif this.animaGrana <= 145: image = Objetos.grana[28]
                        elif this.animaGrana <= 150: image = Objetos.grana[29]
                        elif this.animaGrana <= 155: image = Objetos.grana[30]
                        elif this.animaGrana <= 160: image = Objetos.grana[31]
                        elif this.animaGrana <= 165: image = Objetos.grana[32]
                        elif this.animaGrana <= 170: image = Objetos.grana[33]
                        elif this.animaGrana <= 175: image = Objetos.grana[34]
                        elif this.animaGrana <= 180: image = Objetos.grana[35]

                        Objetos.background.blit(image, (coluna * 32 - Objetos.jogo.deslocamento[0], linha * 32 - Objetos.jogo.deslocamento[1]) )
################### BLITA AS PAREDES
                    else:
                        Objetos.background.blit(Objetos.parede[ Objetos.jogo.getNivel() ], (coluna * 32 - Objetos.jogo.deslocamento[0], linha * 32 - Objetos.jogo.deslocamento[1]) )
        
    def loadNivel(this, nivelNum):

        this.qtdTilesX   = 19
        this.qtdTilesY   = 21
        this.mapa        = {}
        this.numLinha    = 0
        this.acumulo     = 0
        this.matrizCampo = []

        if nivelNum == 0:

            this.matrizCampo = [
            [0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0],
            [0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],
            [0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,1,0,0,0],
            [0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0],
            [0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,1,1,1,1,1,1,0,11,0,0,0,0],
            [0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,1,0,0,0,0,10,0,4,0,0,12,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,0,0,0,0],
            [0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0],
            [0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0],
            [0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0],
            [0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0]
            ]
            
        elif nivelNum == 1:
            
            this.matrizCampo = [
            [1,1,1,1,1,1,1,1,1,21,1,1,1,1,1,1,1,1,1],
            [1,6,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,7,1],
            [1,2,2,2,1,2,2,2,1,2,1,2,2,2,1,2,2,2,1],
            [1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1],
            [1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1],
            [1,2,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,2,1,1,1],
            [1,2,2,2,1,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
            [1,1,2,1,1,1,2,1,1,10,1,1,2,1,1,1,2,1,1],
            [20,2,2,2,2,2,2,2,11,12,13,2,2,2,2,2,2,2,20],
            [1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1],
            [1,2,2,2,1,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
            [1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,2,1,1,1],
            [1,2,2,2,2,2,2,2,2,4,2,2,2,2,2,2,2,2,1],
            [1,1,2,1,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1],
            [1,2,2,2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,1],
            [1,1,2,1,1,1,2,1,1,2,1,1,2,1,1,1,2,1,1],
            [1,1,1,1,1,1,1,1,1,21,1,1,1,1,1,1,1,1,1]
            ]
            
        elif nivelNum == 2:
            
            this.matrizCampo = [
            [1,1,1,1,1,1,1,1,1,21,1,1,1,1,1,1,1,1,1],
            [1,6,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1],
            [1,2,1,2,1,2,2,2,1,2,1,2,2,2,1,2,1,2,1],
            [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
            [1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1],
            [1,2,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1],
            [1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1],
            [1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,2,1,2,1],
            [1,2,2,2,1,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
            [1,1,1,2,1,1,2,1,1,10,1,1,2,1,1,2,1,1,1],
            [20,2,2,2,2,2,2,2,11,12,13,2,2,2,2,2,2,2,20],
            [1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1],
            [1,2,1,2,1,2,2,2,2,4,2,2,2,2,1,2,1,2,1],
            [1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,2,1,2,1],
            [1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1],
            [1,2,1,2,1,2,1,1,2,1,2,1,1,2,1,2,1,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,1],
            [1,1,1,1,1,1,1,1,1,21,1,1,1,1,1,1,1,1,1]
            ]

        elif nivelNum == 3:

            this.matrizCampo = [
            [1,21,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,21,1],
            [1,2,2,1,2,1,2,1,2,2,2,1,2,1,2,1,2,2,1],
            [1,2,1,1,6,1,2,1,2,1,2,1,2,1,7,1,1,2,1],
            [1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1],
            [1,1,1,1,2,1,2,1,1,1,1,1,2,1,2,1,1,1,1],
            [1,2,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,1,1],
            [1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,1,1,1,1,1,2,1,1,10,1,1,2,1,1,1,1,1,1],
            [1,2,2,2,2,1,2,2,11,12,13,2,2,1,2,2,2,2,1],
            [1,1,1,1,2,2,2,1,1,1,1,1,2,2,2,1,1,1,1],
            [20,2,2,2,2,1,2,1,2,2,2,1,2,1,2,2,2,2,20],
            [1,1,1,1,1,1,2,2,2,1,2,2,2,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,1],
            [1,1,2,1,1,1,2,2,2,1,2,2,2,1,1,1,2,1,1],
            [1,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1],
            [1,2,2,2,2,2,2,2,2,4,2,2,2,2,2,2,2,2,1],
            [1,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,2,1,1],
            [1,2,1,8,2,2,2,1,2,1,2,1,2,2,2,9,1,2,1],
            [1,2,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,2,1],
            [1,21,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,21,1]
            ]
            

        for l in range(this.qtdTilesY):
            for k in range(this.qtdTilesX):
                this.SetMapTile((this.numLinha, k), this.matrizCampo[l][k])
                
                thisID = this.matrizCampo[l][k]
                if thisID == 4:
                    Objetos.claude.homeX = k * 32
                    Objetos.claude.homeY = this.numLinha * 32
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
                    
                elif thisID == 10:# and thisID <= 13:
                    Objetos.fantasma.homeX = k * 32
                    Objetos.fantasma.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 11:# and thisID <= 13:
                    Objetos.fantasma1.homeX = k * 32
                    Objetos.fantasma1.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 12:# and thisID <= 13:
                    Objetos.fantasma2.homeX = k * 32
                    Objetos.fantasma2.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 13:# and thisID <= 13:
                    Objetos.fantasma3.homeX = k * 32
                    Objetos.fantasma3.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 2:
                    Objetos.nivel.acumulo += 1
            this.numLinha += 1
        #print this.mapa

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

        Objetos.claude.x           = Objetos.claude.homeX
        Objetos.claude.y           = Objetos.claude.homeY
        Objetos.claude.velX        = 0
        Objetos.claude.velY        = 0
        Objetos.claude.images      = Objetos.claude.direita
        Objetos.claude.animaClaude = 0
