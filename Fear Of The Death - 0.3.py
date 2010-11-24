import pygame, os, random
from pygame.locals import *

fps = pygame.time.Clock()
pygame.init()

background = pygame.display.set_mode((608,672), 0, 32)
pygame.display.set_caption("Fear Of The Death")

##--- INICIANDO SONS
sndGrana    = {}
sndGrana[0] = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"grana1.wav")
sndGrana[1] = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"grana2.wav")

##-- FONTES
fonteGta1 = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'fonteGta1.ttf',20,bold = False)
fonteNome = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'numeros.ttf',30,bold = False)

#fundo = pygame.image.load("data"+os.sep+"tiles"+os.sep+"fundo.jpg")

##class Menu:
##
##    def run(this):
##        while True:
##            for event in pygame.event.get(): 
##                if event.type == QUIT: 
##                    pygame.quit()
##                if event.type == KEYDOWN:
##                    if event.key == K_ESCAPE:
##                        pygame.quit()
##                    if event.key == K_RETURN:
##                        coisas()
##            
##            background.fill((255,255,255))
##            pygame.display.update()
                        
            
        
class Jogo:

    def __init__ (this):
        this.nivel        = 0
        this.score        = 0
        this.vidas        = 3
        this.modo         = 0
        this.tempoModo    = 0
        this.posicaoPixel = (0, 0)
        this.proximoTile  = (0, 0)
        this.deslocamento = (0, 0)
        
        this.setModo(4)
                
        this.qtdTilesTela = (21, 19)
        this.tamanhoTela = (this.qtdTilesTela[1] * 32, this.qtdTilesTela[0] * 32)

    def pontos(this, pontos):
        this.score += pontos
        
    def printPontuacao(this):
        this.texto = fonteGta1.render("SCORE: ", True, (0,0,255))
        this.pontuacao = fonteGta1.render(str(this.score), True, (0,255,0))
        background.blit(this.texto, (100,650))
        background.blit(this.pontuacao, (165, 650))

    def printVidas(this):
        this.texto = fonteGta1.render("VIDAS: " + (str(1)*this.vidas), True, (255,0,0))
        background.blit(this.texto, (5,650))
        
    def novoJogo(this):
        this.nivel = 1
        this.score = 0
        this.vidas = 3
        this.setModo(1)
        nivel.loadNivel(jogo.getNivel())
        
    def getNivel(this):
        return this.nivel
        
    def proximoNivel(this):
        this.nivel += 1
        this.setModo(1)
        nivel.loadNivel(jogo.getNivel())
        claude.velX = 0
        claude.velY = 0
        claude.images = claude.direita
        
    def setModo (this, newMode):
        this.modo = newMode
        this.tempoModo = 0


class Claude:
    
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
        
        if not nivel.verificaParede((this.x + this.velX, this.y + this.velY), (this.proxLinha, this.proxColuna)):
            this.x += this.velX
            this.y += this.velY
            #nivel.matrizCampo[this.proxLinha][this.proxColuna] = 4
            #nivel.matrizCampo[this.proxLinha-1][this.proxColuna-1] = 0
            #print nivel.matrizCampo
            nivel.comida((this.x, this.y), (this.proxLinha, this.proxColuna))  ##-- REMOVE AS NOTAS E PLAY SOM
            nivel.portais((this.x, this.y), (this.proxLinha, this.proxColuna)) ##-- PERMITE A PASSAGEM NOS PORTAIS

        else:
            this.velX = 0
            this.velY = 0
        
    def printClaude(this):
        #print nivel.mapa
        if jogo.modo == 3:
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
            
        background.blit (this.images[int(this.animaClaude)], (this.x - jogo.posicaoPixel[0], this.y - jogo.posicaoPixel[1]))
        
        if jogo.modo == 1:
            if not this.velX == 0 or not this.velY == 0:
                this.animaClaude += 0.3
            if int(this.animaClaude) == 6:
                this.animaClaude = 0

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

            if this.y < claude.y:
                this.velX = 0
                this.velY = this.velocidade
            elif this.y > claude.y:
                this.velX = 0
                this.velY = -this.velocidade
            elif this.x < claude.x:
                this.velX = this.velocidade
                this.velY = 0
            elif this.x > claude.x:
                this.velX = -this.velocidade
                this.velY = 0
            
        this.proxLinha = int(((this.y + 16) / 32))
        this.proxColuna = int(((this.x + 16) / 32))
        
        while nivel.verificaParede((this.x + this.velX, this.y + this.velY), (this.proxLinha, this.proxColuna)):# \
##           and not nivel.GetMapTile((this.proxLinha,this.proxColuna))==20 \
##           and not nivel.GetMapTile((this.proxLinha,this.proxColuna))==21:
            rand = random.randint(1,4)
            if rand == 1:
                this.velX = -fantasma.velocidade
                this.velY = 0
                    
            elif rand == 2:
                this.velX = fantasma.velocidade
                this.velY = 0
                    
            elif rand == 3:
                this.velX = 0
                this.velY = -fantasma.velocidade
                    
            elif rand == 4:
                this.velX = 0
                this.velY = fantasma.velocidade
        else:
            this.x += this.velX
            this.y += this.velY

        
    def printFantasma(this):
        
        background.blit (this.image, (this.x, this.y))

    def colisao(this):
        if claude.x - 16 <= this.x <= claude.x + 16 and claude.y - 16 <= this.y <= claude.y + 16:
            jogo.setModo(2)

##class Colete:
##
##    def __init__(this):
##        
##        this.animaColete = 0
##
##    def printColete(this):
##        
##        this.animaColete += 1
##        
##        if this.animaColete == 116: ##FAZ AS BOLINHAS PISCAREM
##            this.animaColete = 0        
##        
##        for linha in range(-1, jogo.qtdTilesTela[0] +1):
##            for coluna in range(-1, jogo.qtdTilesTela[1] +1):
##
##                tileAtual = nivel.GetMapTile((jogo.proximoTile[0] + linha, jogo.proximoTile[1] + coluna))
##                if not tileAtual == 0 and not tileAtual == 20 and not tileAtual == 21 and not tileAtual == 6: ## NADA and PORTA H and PORTA V
##                    image = pygame.image
##                    
##################### BLITA PROTECAO
##                    if tileAtual == 6 or tileAtual == 7 or tileAtual == 8 or tileAtual == 9: ##ESCUDO PROTETOR
##                        print "colete"
##                        if this.animaColete <= 5:     image = colete[0]
##                        elif this.animaColete <= 10:  image = colete[1]
##                        elif this.animaColete <= 15:  image = colete[2]
##                        elif this.animaColete <= 20:  image = colete[3]
##                        elif this.animaColete <= 25:  image = colete[4]
##                        elif this.animaColete <= 30:  image = colete[5]
##                        elif this.animaColete <= 35:  image = colete[6]
##                        elif this.animaColete <= 40:  image = colete[7]
##                        elif this.animaColete <= 45:  image = colete[8]
##                        elif this.animaColete <= 50:  image = colete[9]
##                        elif this.animaColete <= 55:  image = colete[10]
##                        elif this.animaColete <= 60:  image = colete[11]
##                        elif this.animaColete <= 65:  image = colete[12]
##                        elif this.animaColete <= 70:  image = colete[13]
##                        elif this.animaColete <= 75:  image = colete[14]
##                        elif this.animaColete <= 80:  image = colete[15]
##                        elif this.animaColete <= 85:  image = colete[16]
##                        elif this.animaColete <= 90:  image = colete[17]
##                        elif this.animaColete <= 95:  image = colete[18]
##                        elif this.animaColete <= 100: image = colete[19]
##                        elif this.animaColete <= 105: image = colete[20]
##                        elif this.animaColete <= 110: image = colete[21]
##                        elif this.animaColete <= 115: image = colete[22]
##
##                        background.blit(image, (coluna * 32 - jogo.deslocamento[0], linha * 32 - jogo.deslocamento[1]) )
            
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
                    result = nivel.GetMapTile((liinha, cooluna))

################### REMOCAO DA GRANA       
                    if result == 2: ##-- GRANA
                        nivel.SetMapTile((liinha, cooluna), 0)
                        #nivel.matrizCampo[liinha][cooluna] = 4
                        #nivel.matrizCampo[liinha-1][cooluna] = 0
##                        print nivel.mapa
                        #sndGrana[claude.sndGranaNum].play()
                        #claude.sndGranaNum = 1 - claude.sndGranaNum
                        
                        nivel.acumulo -= 1
                        jogo.pontos(10)
                        if nivel.acumulo == 0:
                            jogo.setModo( 4 )
                            
################### REMOCAO DO ESCUDO                       
                    elif result == 7: ##ESCUDO PROTETOR
                        nivel.SetMapTile((liinha, cooluna), 0)
                        #snd_powerpellet.play()
                        jogo.pontos(100)

### PORTAS HORIZONTAIS E VERTICAIS

    def portais(this, (claudeX, claudeY), (linha, coluna)):
        
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
                
                if  (claudeX - (cooluna * 32) < 32) and (claudeX - (cooluna * 32) > -32) and (claudeY - (liinha * 32) < 32) and (claudeY - (liinha * 32) > -32):
                # check the offending tile ID
                    result = nivel.GetMapTile((liinha, cooluna))
                
                    if result == 20: ##PORTA HORIZONTAL
                        for i in range(0, nivel.qtdTilesX):
                            if not i == cooluna:
                                if nivel.GetMapTile((liinha, i)) == 20: ##PORTA HORIZONTAL
                                    claude.x = i * 32
                                    
                                    if claude.velX > 0:
                                        claude.x += 32
                                    else:
                                        claude.x -= 32
                                        
                    elif result == 21: ##PORTA VERTICAL
                        for i in range(0, nivel.qtdTilesY):
                            if not i == liinha:
                                if nivel.GetMapTile((i, cooluna)) == 21: ##PORTA VERTICAL
                                    claude.y = i * 32
                                    
                                    if claude.velY > 0:
                                        claude.y += 32
                                    else:
                                        claude.y -= 32

### PORTAS HORIZONTAIS E VERTICAIS PARA OS FANTASMAS
    def portaisF(this, (fX, fY), (linha, coluna), fant):
        
        for liinha in range(linha - 1, linha + 2):
            for cooluna in range(coluna - 1, coluna + 2):
                
                if  (fX - (cooluna * 32) < 32) and (fX - (cooluna * 32) > -32) and (fY - (liinha * 32) < 32) and (fY - (liinha * 32) > -32):
                # check the offending tile ID
                    result = nivel.GetMapTile((liinha, cooluna))
                
                    if result == 20: ##PORTA HORIZONTAL
                        for i in range(0, nivel.qtdTilesX):
                            if not i == cooluna:
                                if nivel.GetMapTile((liinha, i)) == 20: ##PORTA HORIZONTAL
                                    fant.x = i * 32
                                    
                                    if fant.velX > 0:
                                        fant.x += 32
                                    else:
                                        fant.x -= 32
                                        
                    elif result == 21: ##PORTA VERTICAL
                        for i in range(0, nivel.qtdTilesY):
                            if not i == liinha:
                                if nivel.GetMapTile((i, cooluna)) == 21: ##PORTA VERTICAL
                                    fant.y = i * 32
                                    
                                    if fant.velY > 0:
                                        fant.y += 32
                                    else:
                                        fant.y -= 32

### VERIFICA SE EH PAREDE
    def parede(this, (linha, coluna)):

        celula = nivel.GetMapTile((linha, coluna))
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
        
        
        for linha in range(-1, jogo.qtdTilesTela[0] +1, 1):
            for coluna in range(-1, jogo.qtdTilesTela[1] +1, 1):

                tileAtual = this.GetMapTile((jogo.proximoTile[0] + linha, jogo.proximoTile[1] + coluna))
                if not tileAtual == 0 and not tileAtual == 20 and not tileAtual == 21 and not tileAtual == 6: ## NADA and PORTA H and PORTA V
                    image = pygame.image
                    
################### BLITA PROTECAO
                    if tileAtual == 7: ##ESCUDO PROTETOR
                        if this.animaColete <= 5:     image = colete[0]
                        elif this.animaColete <= 10:  image = colete[1]
                        elif this.animaColete <= 15:  image = colete[2]
                        elif this.animaColete <= 20:  image = colete[3]
                        elif this.animaColete <= 25:  image = colete[4]
                        elif this.animaColete <= 30:  image = colete[5]
                        elif this.animaColete <= 35:  image = colete[6]
                        elif this.animaColete <= 40:  image = colete[7]
                        elif this.animaColete <= 45:  image = colete[8]
                        elif this.animaColete <= 50:  image = colete[9]
                        elif this.animaColete <= 55:  image = colete[10]
                        elif this.animaColete <= 60:  image = colete[11]
                        elif this.animaColete <= 65:  image = colete[12]
                        elif this.animaColete <= 70:  image = colete[13]
                        elif this.animaColete <= 75:  image = colete[14]
                        elif this.animaColete <= 80:  image = colete[15]
                        elif this.animaColete <= 85:  image = colete[16]
                        elif this.animaColete <= 90:  image = colete[17]
                        elif this.animaColete <= 95:  image = colete[18]
                        elif this.animaColete <= 100: image = colete[19]
                        elif this.animaColete <= 105: image = colete[20]
                        elif this.animaColete <= 110: image = colete[21]
                        elif this.animaColete <= 115: image = colete[22]

                        background.blit(image, (coluna * 32 - jogo.deslocamento[0], linha * 32 - jogo.deslocamento[1]) )
                        
################### BLITA GRANA
                    elif tileAtual == 2:
                        if this.animaGrana <= 5:     image = grana[0]
                        elif this.animaGrana <= 10:  image = grana[1]
                        elif this.animaGrana <= 15:  image = grana[2]
                        elif this.animaGrana <= 20:  image = grana[3]
                        elif this.animaGrana <= 25:  image = grana[4]
                        elif this.animaGrana <= 30:  image = grana[5]
                        elif this.animaGrana <= 35:  image = grana[6]
                        elif this.animaGrana <= 40:  image = grana[7]
                        elif this.animaGrana <= 45:  image = grana[8]
                        elif this.animaGrana <= 50:  image = grana[9]
                        elif this.animaGrana <= 55:  image = grana[10]
                        elif this.animaGrana <= 60:  image = grana[11]
                        elif this.animaGrana <= 65:  image = grana[12]
                        elif this.animaGrana <= 70:  image = grana[13]
                        elif this.animaGrana <= 75:  image = grana[14]
                        elif this.animaGrana <= 80:  image = grana[15]
                        elif this.animaGrana <= 85:  image = grana[16]
                        elif this.animaGrana <= 90:  image = grana[17]
                        elif this.animaGrana <= 95:  image = grana[18]
                        elif this.animaGrana <= 100: image = grana[19]
                        elif this.animaGrana <= 105: image = grana[20]
                        elif this.animaGrana <= 110: image = grana[21]
                        elif this.animaGrana <= 115: image = grana[22]
                        elif this.animaGrana <= 120: image = grana[23]
                        elif this.animaGrana <= 125: image = grana[24]
                        elif this.animaGrana <= 130: image = grana[25]
                        elif this.animaGrana <= 135: image = grana[26]
                        elif this.animaGrana <= 140: image = grana[27]
                        elif this.animaGrana <= 145: image = grana[28]
                        elif this.animaGrana <= 150: image = grana[29]
                        elif this.animaGrana <= 155: image = grana[30]
                        elif this.animaGrana <= 160: image = grana[31]
                        elif this.animaGrana <= 165: image = grana[32]
                        elif this.animaGrana <= 170: image = grana[33]
                        elif this.animaGrana <= 175: image = grana[34]
                        elif this.animaGrana <= 180: image = grana[35]

                        background.blit(image, (coluna * 32 - jogo.deslocamento[0], linha * 32 - jogo.deslocamento[1]) )
################### BLITA AS PAREDES
                    else:
                        background.blit(parede[ jogo.getNivel() ], (coluna * 32 - jogo.deslocamento[0], linha * 32 - jogo.deslocamento[1]) )
        
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
                    claude.homeX = k * 32
                    claude.homeY = this.numLinha * 32
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
                    fantasma.homeX = k * 32
                    fantasma.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 11:# and thisID <= 13:
                    fantasma1.homeX = k * 32
                    fantasma1.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 12:# and thisID <= 13:
                    fantasma2.homeX = k * 32
                    fantasma2.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 13:# and thisID <= 13:
                    fantasma3.homeX = k * 32
                    fantasma3.homeY = this.numLinha * 32
                    this.SetMapTile((this.numLinha, k), 0 )
                elif thisID == 2:
                    nivel.acumulo += 1
            this.numLinha += 1
        #print this.mapa

        this.reiniciar()
        
    def reiniciar(this):
        
        fantasma.x         = fantasma.homeX
        fantasma.y         = fantasma.homeY
        fantasma.velX      = 2
        fantasma.velY      = 0

        fantasma1.x        = fantasma1.homeX
        fantasma1.y        = fantasma1.homeY
        fantasma1.velX     = -2
        fantasma1.velY     = 0

        fantasma2.x        = fantasma2.homeX
        fantasma2.y        = fantasma2.homeY
        fantasma2.velX     = 0
        fantasma2.velY     = 2

        fantasma3.x        = fantasma3.homeX
        fantasma3.y        = fantasma3.homeY
        fantasma3.velX     = 0
        fantasma3.velY     = -2

        claude.x           = claude.homeX
        claude.y           = claude.homeY
        claude.velX        = 0
        claude.velY        = 0
        claude.images      = claude.direita
        claude.animaClaude = 0

class NomeUser:

    def __init__(this):
        this.user   = ""

    def gravarHiscore(this):

        dados  = []
        
        try:
            ler = open("data" + os.sep + "hiscore.txt", "r")
            #print "passou do ler dados"
            lerDados = ler.readlines()
            ler.close()
            for dado in lerDados:
                dados.append(dado.strip())
        except:
            criar = open("data" + os.sep + "hiscore.txt", "w")
            #print "entrou no except e crou o arquivo"
        try:
            if not this.user + " " + str(jogo.score) in dados:
                
                gravar = open("data" + os.sep + "hiscore.txt", "a")
                gravar.write(this.user + " " + str(jogo.score) + "\n")
                gravar.close()
                print "gravou a bagaca"
        except:
            pass

    def screenName(this):

        while True:

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                    
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE: pygame.quit()
                    if event.key == K_KP_ENTER:
                        this.gravarHiscore()
                        return "gravado"
                    if event.key == K_RETURN:
                        this.gravarHiscore()
                        return "gravado"
                    if event.key == K_BACKSPACE: this.user = this.user[:-1]
                    if event.key == K_SPACE: this.user += " "
                    if event.key == K_EXCLAIM: this.user += "!"
                    if event.key == K_QUOTEDBL: this.user += "\""
                    if event.key == K_HASH: this.user += "#"
                    if event.key == K_DOLLAR: this.user += " "
                    if event.key == K_AMPERSAND: this.user += "&"
                    if event.key == K_LEFTPAREN: this.user += "("
                    if event.key == K_RIGHTPAREN: this.user += ")"
                    if event.key == K_ASTERISK: this.user += "*"
                    if event.key == K_PLUS: this.user += "+"
                    if event.key == K_COMMA: this.user += ","
                    if event.key == K_MINUS: this.user += "-"
                    if event.key == K_PERIOD: this.user += "."
                    if event.key == K_SLASH: this.user += "/"
                    if event.key == K_0: this.user += "0"
                    if event.key == K_1: this.user += "1"
                    if event.key == K_2: this.user += "2"
                    if event.key == K_3: this.user += "3"
                    if event.key == K_4: this.user += "4"
                    if event.key == K_5: this.user += "5"
                    if event.key == K_6: this.user += "6"
                    if event.key == K_7: this.user += "7"
                    if event.key == K_8: this.user += "8"
                    if event.key == K_9: this.user += "9"
                    if event.key == K_COLON: this.user += ":"
                    if event.key == K_SEMICOLON: this.user += ";"
                    if event.key == K_LESS: this.user += "<"
                    if event.key == K_EQUALS: this.user += "="
                    if event.key == K_GREATER: this.user += ">"
                    if event.key == K_QUESTION: this.user += "?"
                    if event.key == K_AT: this.user += "@"
                    if event.key == K_LEFTBRACKET: this.user += "["
                    if event.key == K_BACKSLASH: this.user += "\\"
                    if event.key == K_RIGHTBRACKET: this.user += "]"
                    if event.key == K_UNDERSCORE: this.user += "_"
                    if event.key == K_BACKQUOTE: this.user += "'"
                    if event.key == K_a: this.user += "A"
                    if event.key == K_b: this.user += "B"
                    if event.key == K_c: this.user += "C"
                    if event.key == K_d: this.user += "D"
                    if event.key == K_e: this.user += "E"
                    if event.key == K_f: this.user += "F"
                    if event.key == K_g: this.user += "G"
                    if event.key == K_h: this.user += "H"
                    if event.key == K_i: this.user += "I"
                    if event.key == K_j: this.user += "J"
                    if event.key == K_k: this.user += "K"
                    if event.key == K_l: this.user += "L"
                    if event.key == K_m: this.user += "M"
                    if event.key == K_n: this.user += "N"
                    if event.key == K_o: this.user += "O"
                    if event.key == K_p: this.user += "P"
                    if event.key == K_q: this.user += "Q"
                    if event.key == K_r: this.user += "R"
                    if event.key == K_s: this.user += "S"
                    if event.key == K_t: this.user += "T"
                    if event.key == K_u: this.user += "U"
                    if event.key == K_v: this.user += "V"
                    if event.key == K_w: this.user += "W"
                    if event.key == K_x: this.user += "X"
                    if event.key == K_y: this.user += "Y"
                    if event.key == K_z: this.user += "Z"
                    if event.key == K_KP0: this.user += "0"
                    if event.key == K_KP1: this.user += "1"
                    if event.key == K_KP2: this.user += "2"
                    if event.key == K_KP3: this.user += "3"
                    if event.key == K_KP4: this.user += "4"
                    if event.key == K_KP5: this.user += "5"
                    if event.key == K_KP6: this.user += "6"
                    if event.key == K_KP7: this.user += "7"
                    if event.key == K_KP8: this.user += "8"
                    if event.key == K_KP9: this.user += "9"
                    if event.key == K_KP_PERIOD: this.user += "."
                    if event.key == K_KP_DIVIDE: this.user += "/"
                    if event.key == K_KP_MULTIPLY: this.user += "*"
                    if event.key == K_KP_MINUS: this.user += "-"
                    if event.key == K_KP_PLUS: this.user += "+"
                    if event.key == K_KP_EQUALS: this.user += "="

            print this.user
            this.texto = fonteNome.render("DIGITE SEU NOME", True, (0,0,0))
            this.nome = fonteNome.render(this.user, True, (0,0,0))

            background.fill((255,255,255))
            background.blit(this.texto, (100,300))
            background.blit(this.nome, (100, 350))
            pygame.display.update()
        

def verificaTeclas():

    pressed = pygame.key.get_pressed()
    
### CHECA SAIDA
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                
### CHECA MOVIMENTOS
    if jogo.modo == 1:
        if pressed[K_RIGHT]:
            if not nivel.verificaParede((claude.x + claude.velocidade, claude.y), (claude.proxLinha, claude.proxColuna)): 
                claude.velX = claude.velocidade
                claude.velY = 0
                claude.direcao = "direita"
                
        elif pressed[K_LEFT]:
            if not nivel.verificaParede((claude.x - claude.velocidade, claude.y), (claude.proxLinha, claude.proxColuna)): 
                claude.velX = -claude.velocidade
                claude.velY = 0
                claude.direcao = "esquerda"
            
        elif pressed[K_DOWN]:
            if not nivel.verificaParede((claude.x, claude.y + claude.velocidade), (claude.proxLinha, claude.proxColuna)): 
                claude.velX = 0
                claude.velY = claude.velocidade
                claude.direcao = "baixo"
            
        elif pressed[K_UP]:
            if not nivel.verificaParede((claude.x, claude.y - claude.velocidade), (claude.proxLinha, claude.proxColuna)):
                claude.velX = 0
                claude.velY = -claude.velocidade
                claude.direcao = "cima"

    if jogo.modo == 4: #or jogo.modo == 5:
        if pressed[K_RETURN]:
            if jogo.getNivel() == 3:
                print "FIM DO JOGO"
                pygame.quit()
            else:
                jogo.proximoNivel()
                
    if jogo.modo == 5:
        if pressed[K_RETURN]:
            nivel.loadNivel(0)

claude    = Claude() ##-- INSTANCIACAO DE UM OBJETO DE Claude
fantasma  = Fantasma()
fantasma1 = Fantasma()
fantasma2 = Fantasma()
fantasma3 = Fantasma()
##protect   = Colete()
##protect1  = Colete()
##protect2  = Colete()
##protect3  = Colete()
nomeTile  = {}       ##-- ARMAZENA OS NOMES DOS TILES
colete    = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA COLETE
grana     = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA GRANA
parede    = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA PAREDE
jogo      = Jogo()   ##-- INSTANCIACAO DE UM OBJETO DE Jogo
nivel     = Nivel()  ##-- INSTANCIACAO DE UM OBJETO DE Nivel

grava     = NomeUser() ## --- Grava a bagaceira

nivel.loadNivel( jogo.getNivel() )

nomeTile[1]  = "parede"
nomeTile[2]  = "grana"
nomeTile[3]  = "comida2"
nomeTile[4]  = "comida3"
nomeTile[5]  = "comida4"
nomeTile[6]  = "ghost-door"
nomeTile[7]  = "protetor"
nomeTile[20] = "portaHorizontal"
nomeTile[21] = "portaVertical"

for i in range(23):
    colete[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"colete"+os.sep+ "colete"+str(i)+".png").convert_alpha()
for i in range(36):
    grana[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"grana"+os.sep+ "grana"+str(i)+".png").convert_alpha()
for i in range(4):
    parede[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"paredes"+os.sep+ "parede"+str(i)+".jpg").convert_alpha()


##LOOP PRINCIPAL
while True: 

    verificaTeclas()
    if jogo.modo == 1:
        print "entreou no 1"

        verificaTeclas()
        
        fantasma.colisao()
        fantasma1.colisao()
        fantasma2.colisao()
        fantasma3.colisao()
        
        claude.andar()
        fantasma.andar()
        fantasma1.andar()
        fantasma2.andar()
        fantasma3.andar()

        nivel.portaisF((fantasma.x, fantasma.y), (fantasma.proxLinha, fantasma.proxColuna), fantasma)
        nivel.portaisF((fantasma1.x, fantasma1.y), (fantasma1.proxLinha, fantasma1.proxColuna), fantasma1)
        nivel.portaisF((fantasma2.x, fantasma2.y), (fantasma2.proxLinha, fantasma2.proxColuna), fantasma2)
        nivel.portaisF((fantasma3.x, fantasma3.y), (fantasma3.proxLinha, fantasma3.proxColuna), fantasma3)

##### OPCAO DE REINICIO DE FASE APOS A PERDA DE UMA VIDA
    elif jogo.modo == 2:
        print "entrou no 2"
        jogo.tempoModo += 1
        
        if jogo.tempoModo == 90:
            jogo.vidas -= 1
            nivel.reiniciar()
            jogo.setModo(1)
            print jogo.vidas
            
            if jogo.vidas == 0:
                print grava.screenName()
                cont=0
                while cont <= 100:
                    print "PERDEU MANOLO"
                    print "volta pro menu"
                    cont+=1
                jogo.setModo(5)

    elif jogo.modo == 3:
        print "ENTROU NO 3"
        jogo.novoJogo()
        verificaTeclas()

    elif jogo.modo == 4:
        print "entrou no 4"
        if jogo.getNivel() == 3:
            print grava.screenName()
            venceu = fonteGta1.render("VOCE VENCEU!!", True, (255,0,0))
            background.blit(venceu, (100, 100))
        verificaTeclas()

    elif jogo.modo == 5:
        
        #pygame.event.clear()
        nivel.reiniciar()
        jogo.vidas = 3
        jogo.nivel = 0
        nivel.loadNivel(0)
##        if pygame.key.get_pressed()[K_RETURN]:
##            pass
        verificaTeclas()

    background.fill((200, 200, 200))

    ####BLITA MAPA E claude NA TELA
    nivel.printMapa()
    claude.printClaude()

##    protect.printColete()
##    protect1.printColete()
##    protect2.printColete()
##    protect3.printColete()

    fantasma.printFantasma()
    fantasma1.printFantasma()
    fantasma2.printFantasma()
    fantasma3.printFantasma()
    
    jogo.printVidas()
    jogo.printPontuacao()
    pygame.display.update()
    
    fps.tick (60)
##COMENTARIO
