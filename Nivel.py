import pygame
import Objetos

class Nivel:
    
    def __init__ (this):
        this.qtdTilesX   = 0
        this.qtdTilesY   = 0
        this.mapa        = {}
        this.acumulo     = 0
        this.animaTurbo  = 0
        this.animaRoda   = 0

    ##--- DEFINE O TILE NA POSICAO EM QUESTAO
    def SetMapTile (this, (linha, coluna), valor):
        this.mapa[ coluna + (linha * this.qtdTilesX) ] = valor

    ##--- RETORNA O TILE DA POSICAO EM QUESTAO
    def GetMapTile (this, (linha, coluna)):
        if linha >= 0 and linha < this.qtdTilesY and coluna >= 0 and coluna < this.qtdTilesX:
            return this.mapa[ coluna + (linha * this.qtdTilesX) ]
        else:
            return 0

    ##--- MOEDAS
    def comida(this, (sonicX, sonicY), (linha, coluna)):
    
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
            
                if  (sonicX - (cooluna * 32) < 32) and (sonicX - (cooluna * 32) > -32) and (sonicY - (liinha * 32) < 32) and (sonicY - (liinha * 32) > -32):
                    result = Objetos.nivel.GetMapTile((liinha, cooluna))

                    ##--- REMOCAO DAS MOEDAS      
                    if result == 2:
                        Objetos.nivel.SetMapTile((liinha, cooluna), 0)
                        Objetos.sndMoeda.play()
                        Objetos.nivel.acumulo -= 1
                        Objetos.jogo.pontos(10)
                        if Objetos.nivel.acumulo == 0:
                            Objetos.jogo.setModo(3)
                            
                    ##--- REMOCAO DO SUPER BOOSTER                       
                    elif result == 7:
                        Objetos.nivel.SetMapTile((liinha, cooluna), 0)
                        Objetos.sonic.limiteEscudo += 500
                        Objetos.jogo.pontos(100)

    ##--- PORTAIS HORIZONTAIS E VERTICAIS
    def portais(this, (sonicX, sonicY), (linha, coluna)):
        
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
                
                if  (sonicX - (cooluna * 32) < 32) and (sonicX - (cooluna * 32) > -32) and (sonicY - (liinha * 32) < 32) and (sonicY - (liinha * 32) > -32):
                    
                    result = Objetos.nivel.GetMapTile((liinha, cooluna))

                    ##--- PORTA HORIZONTAL
                    if result == 20: 
                        for i in range(0, Objetos.nivel.qtdTilesX):
                            if not i == cooluna:
                                if Objetos.nivel.GetMapTile((liinha, i)) == 20:
                                    Objetos.sonic.x = i * 32
                                    
                                    if Objetos.sonic.velX > 0:
                                        Objetos.sonic.x += 32
                                    else:
                                        Objetos.sonic.x -= 32
                    ##--- PORTA VERTICAL  
                    elif result == 21:
                        for i in range(0, Objetos.nivel.qtdTilesY):
                            if not i == liinha:
                                if Objetos.nivel.GetMapTile((i, cooluna)) == 21:
                                    Objetos.sonic.y = i * 32
                                    
                                    if Objetos.sonic.velY > 0:
                                        Objetos.sonic.y += 32
                                    else:
                                        Objetos.sonic.y -= 32

    ##--- PORTAIS HORIZONTAIS E VERTICAIS PARA OS FANTASMAS
    def portaisF(this, (fX, fY), (linha, coluna), fant):
        
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
                
                if  (fX - (cooluna * 32) < 32) and (fX - (cooluna * 32) > -32) and (fY - (liinha * 32) < 32) and (fY - (liinha * 32) > -32):

                    result = Objetos.nivel.GetMapTile((liinha, cooluna))
                    
                    ##--- PORTA HORIZONTAL
                    if result == 20: 
                        for i in range(0, Objetos.nivel.qtdTilesX):
                            if not i == cooluna:
                                if Objetos.nivel.GetMapTile((liinha, i)) == 20:
                                    fant.x = i * 32
                                    
                                    if fant.velX > 0:
                                        fant.x += 32
                                    else:
                                        fant.x -= 32
                                        
                    ##--- PORTA VERTICAL 
                    elif result == 21: 
                        for i in range(0, Objetos.nivel.qtdTilesY):
                            if not i == liinha:
                                if Objetos.nivel.GetMapTile((i, cooluna)) == 21:
                                    fant.y = i * 32
                                    
                                    if fant.velY > 0:
                                        fant.y += 32
                                    else:
                                        fant.y -= 32

    ##--- VERIFICA SE EH PAREDE
    def parede(this, (linha, coluna)):

        celula = Objetos.nivel.GetMapTile((linha, coluna))
        if celula == 1:
            return True
        else:
            return False

    ##--- VERIFICA SE VAI BATER NA PAREDE
    def verificaParede(this, (posX, posY), (linha, coluna)):
        
        for liinha in range(linha-1, linha+2):
            for cooluna in range(coluna-1, coluna+2):
                if  (posX - (cooluna * 32) < 32) and (posX - (cooluna * 32) > -32) and (posY - (liinha * 32) < 32) and (posY - (liinha * 32) > -32):
                    if this.parede((liinha, cooluna)):
                        return True
        return False

    ##--- PRINTA O CENARIO
    def printMapa (this):
        
        this.animaTurbo += 1
        this.animaRoda += 1
        
        if this.animaTurbo >= 181:
            this.animaTurbo = 0
            
        if this.animaRoda == 20:
            this.animaRoda = 0
        
        
        for linha in range(-1, Objetos.jogo.qtdTilesTela[0] +1):
            for coluna in range(-1, Objetos.jogo.qtdTilesTela[1] +1):

                tileAtual = this.GetMapTile((linha, coluna))
                if not tileAtual == 0 and not tileAtual == 20 and not tileAtual == 21:
                    image = pygame.image

                    if tileAtual != 1:
                        Objetos.background.blit(Objetos.grama, (coluna * 32, linha * 32) )
                    
                    ##--- BLITA SUPER BOOSTER
                    if tileAtual == 7:
                        if this.animaTurbo <= 5:     image = Objetos.turbo[0]
                        elif this.animaTurbo <= 10:  image = Objetos.turbo[1]
                        elif this.animaTurbo <= 15:  image = Objetos.turbo[2]
                        elif this.animaTurbo <= 20:  image = Objetos.turbo[3]
                        elif this.animaTurbo <= 25:  image = Objetos.turbo[4]
                        elif this.animaTurbo <= 30:  image = Objetos.turbo[5]
                        elif this.animaTurbo <= 35:  image = Objetos.turbo[6]
                        elif this.animaTurbo <= 40:  image = Objetos.turbo[7]
                        elif this.animaTurbo <= 45:  image = Objetos.turbo[8]
                        elif this.animaTurbo <= 50:  image = Objetos.turbo[9]
                        elif this.animaTurbo <= 55:  image = Objetos.turbo[10]
                        elif this.animaTurbo <= 60:  image = Objetos.turbo[11]
                        elif this.animaTurbo <= 65:  image = Objetos.turbo[12]
                        elif this.animaTurbo <= 70:  image = Objetos.turbo[13]
                        elif this.animaTurbo <= 75:  image = Objetos.turbo[14]
                        elif this.animaTurbo <= 80:  image = Objetos.turbo[15]
                        elif this.animaTurbo <= 85:  image = Objetos.turbo[16]
                        elif this.animaTurbo <= 90:  image = Objetos.turbo[17]
                        elif this.animaTurbo <= 95:  image = Objetos.turbo[18]
                        elif this.animaTurbo <= 100: image = Objetos.turbo[19]
                        elif this.animaTurbo <= 105: image = Objetos.turbo[20]
                        elif this.animaTurbo <= 110: image = Objetos.turbo[21]
                        elif this.animaTurbo <= 115: image = Objetos.turbo[22]
                        elif this.animaTurbo <= 120: image = Objetos.turbo[23]
                        elif this.animaTurbo <= 125: image = Objetos.turbo[24]
                        elif this.animaTurbo <= 130: image = Objetos.turbo[25]
                        elif this.animaTurbo <= 135: image = Objetos.turbo[26]
                        elif this.animaTurbo <= 140: image = Objetos.turbo[27]
                        elif this.animaTurbo <= 145: image = Objetos.turbo[28]
                        elif this.animaTurbo <= 150: image = Objetos.turbo[29]
                        elif this.animaTurbo <= 155: image = Objetos.turbo[30]
                        elif this.animaTurbo <= 160: image = Objetos.turbo[31]
                        elif this.animaTurbo <= 165: image = Objetos.turbo[32]
                        elif this.animaTurbo <= 170: image = Objetos.turbo[33]
                        elif this.animaTurbo <= 175: image = Objetos.turbo[34]
                        elif this.animaTurbo <= 180: image = Objetos.turbo[35]
                        
                        Objetos.background.blit(image, (coluna * 32, linha * 32) )
                        
                    ##--- BLITA MOEDA
                    if tileAtual == 2:
                        if this.animaRoda <= 5: image    = Objetos.roda[0]
                        elif this.animaRoda <= 10: image = Objetos.roda[1]
                        elif this.animaRoda <= 15: image = Objetos.roda[2]
                        elif this.animaRoda <= 20: image = Objetos.roda[3]

                        Objetos.background.blit(image, (coluna * 32, linha * 32) )
                    ##--- BLITA AS PAREDES
                    if tileAtual == 1:
                        Objetos.background.blit(Objetos.parede[ Objetos.jogo.getNivel() ], (coluna * 32, linha * 32) )

    ##--- CARREGA UM NOVO NIVEL DE ACORDO COM O nivelNum
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

    ##--- RESETA AS VARIAVEIS PRINCIPAIS DO JOGO
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
