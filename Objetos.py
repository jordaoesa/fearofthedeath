import pygame
import os
import Player
import Fantasma
import Jogo
import NomeUser
import Nivel
import Funcoes
import Menu
import Loop
import EscolhePlayer
import Opcoes
import Instrucoes
import Creditos


fps = pygame.time.Clock()
pygame.init()

background = pygame.display.set_mode((608,672), 0, 32)
pygame.display.set_caption("Fear Of The Death")

##--- SELECT PLAYER
fundoSelect = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectPlayer.jpg").convert_alpha()
selectedShadow = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectShadow.png").convert_alpha()
selectedKnuckles = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectKnuckles.png").convert_alpha()
selectedSonic = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectSonic.png").convert_alpha()

##--- FUNDO NOME
fundoShadow = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"shadow.jpg").convert_alpha()
fundoKnuckles = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"knuckles.jpg").convert_alpha()
fundoSonic = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"sonic.jpg").convert_alpha()
tarjaNome = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"tarjaNome.png").convert_alpha()

##--- INICIANDO SONS
sndGrana    = {}
sndGrana[0] = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"grana1.wav")
sndGrana[1] = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"grana2.wav")

##-- FONTES
fonteGta1 = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'fonteGta1.ttf',20,bold = False)
fonteNome = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'numeros.ttf',30,bold = False)

#fundo = pygame.image.load("data"+os.sep+"tiles"+os.sep+"fundo.jpg")

sonic        = Player.Sonic() ##-- INSTANCIACAO DE UM OBJETO DE SONIC
fantasma     = Fantasma.Fantasma()
fantasma1    = Fantasma.Fantasma()
fantasma2    = Fantasma.Fantasma()
fantasma3    = Fantasma.Fantasma()
##protect   = Colete()
##protect1  = Colete()
##protect2  = Colete()
##protect3  = Colete()
nomeTile     = {}       ##-- ARMAZENA OS NOMES DOS TILES
colete       = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA COLETE
parede       = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA PAREDE
imgPlayer    = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
shadowPlayer = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
knucklesPlayer = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
sonicPlayer = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
##sonicB       = {}
##sonicE       = {}
##sonicD       = {}
##sonicC       = {}
roda         = {}
jogo         = Jogo.Jogo()   ##-- INSTANCIACAO DE UM OBJETO DE Jogo
nivel        = Nivel.Nivel()  ##-- INSTANCIACAO DE UM OBJETO DE Nivel
grava        = NomeUser.NomeUser() ## --- Grava a bagaceira
#nivel.loadNivel( jogo.getNivel() )
menu         = Menu.Menu()
start        = Loop.Principal()
escolha      = EscolhePlayer.EscolhePlayer()
opcoes       = Opcoes.Opcoes()
instrucoes   = Instrucoes.Instrucoes()
creditos     = Creditos.Creditos()


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
for i in range(4):
    shadowPlayer["playerB"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"shadow"+os.sep+ "0"+str(i)+".png").convert_alpha()
    shadowPlayer["playerE"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"shadow"+os.sep+ "1"+str(i)+".png").convert_alpha()
    shadowPlayer["playerD"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"shadow"+os.sep+ "2"+str(i)+".png").convert_alpha()
    shadowPlayer["playerC"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"shadow"+os.sep+ "3"+str(i)+".png").convert_alpha()

    knucklesPlayer["playerB"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"knuckles"+os.sep+ "0"+str(i)+".png").convert_alpha()
    knucklesPlayer["playerE"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"knuckles"+os.sep+ "1"+str(i)+".png").convert_alpha()
    knucklesPlayer["playerD"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"knuckles"+os.sep+ "2"+str(i)+".png").convert_alpha()
    knucklesPlayer["playerC"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"knuckles"+os.sep+ "3"+str(i)+".png").convert_alpha()

    sonicPlayer["playerB"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"sonic"+os.sep+ "0"+str(i)+".png").convert_alpha()
    sonicPlayer["playerE"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"sonic"+os.sep+ "1"+str(i)+".png").convert_alpha()
    sonicPlayer["playerD"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"sonic"+os.sep+ "2"+str(i)+".png").convert_alpha()
    sonicPlayer["playerC"][i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"sonic"+os.sep+ "3"+str(i)+".png").convert_alpha()
    
    parede[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"paredes"+os.sep+ "parede"+str(i)+".jpg").convert_alpha()
##    sonicB[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"shadow"+os.sep+ "0"+str(i)+".png").convert_alpha()
##    sonicE[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"shadow"+os.sep+ "1"+str(i)+".png").convert_alpha()
##    sonicD[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"shadow"+os.sep+ "2"+str(i)+".png").convert_alpha()
##    sonicC[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"shadow"+os.sep+ "3"+str(i)+".png").convert_alpha()
    roda[i]  = pygame.image.load("data"+os.sep+"sprites"+os.sep+"rodas"+os.sep+ "0"+str(i)+".png").convert_alpha()
