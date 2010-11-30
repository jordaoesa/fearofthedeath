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
pygame.mixer.init()

modoTela = 0
background = pygame.display.set_mode((608,672), modoTela, 32)
pygame.display.set_caption("Fear Of The Death")

##--- VARIAVEL DE VOLUME
volume = 100

##--- SELECT PLAYER
fundoSelect = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectPlayer.jpg").convert_alpha()
fundoSelect1 = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectPlayerRed.jpg").convert_alpha()
selectedShadow = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectShadow.png").convert_alpha()
selectedKnuckles = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectKnuckles.png").convert_alpha()
selectedSonic = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"selectSonic.png").convert_alpha()

##--- FUNDO INSTRUCOES
sonicFala = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"sonicFala.png").convert_alpha()
shadowFala = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"shadowFala.png").convert_alpha()
knucklesFala = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"knucklesFala.png").convert_alpha()


##--- FUNDO NOME
fundoShadow = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"shadow.jpg").convert_alpha()
fundoKnuckles = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"knuckles.jpg").convert_alpha()
fundoSonic = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"sonic.jpg").convert_alpha()
tarjaNome = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"tarjaNome.png").convert_alpha()

##--- FUNDO OPCOES
fundoOpcoes = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"fundoOpcoes.png").convert_alpha()

##--- INICIANDO SONS
sndTema = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"Fear of the dark.ogg")
sndMoeda = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"playerMoeda.ogg")
sndMorte = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"playerMorte.ogg")
sndMoeda.set_volume(volume/100.0)
sndMorte.set_volume(volume/100.0)

##--- FONTES
fonteGta = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'fonteGta1.ttf',20,bold = False)
fonteSega = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'sega.ttf',30,bold = False)
fonteHoliday = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'Holiday.ttf',30,bold = False)
#fonteHoliday = pygame.font.Font("data"+os.sep+"fontes"+os.sep+"50.ttf",30,bold = False)

sonic            = Player.Sonic() ##-- INSTANCIACAO DE UM OBJETO DE SONIC
#player           = Player.Player()
fantasma         = Fantasma.Fantasma()
fantasma1        = Fantasma.Fantasma()
fantasma2        = Fantasma.Fantasma()
fantasma3        = Fantasma.Fantasma()
nomeTile         = {}       ##-- ARMAZENA OS NOMES DOS TILES
##colete           = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA COLETE
parede           = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA PAREDE
turbo            = {} ##--- ARMAZENA OS SPRITES DO MODO TURBO
imgPlayer        = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
shadowPlayer     = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
knucklesPlayer   = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
sonicPlayer      = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
roda             = {} ##-- MOEDA PLAYER
jogo             = Jogo.Jogo()   ##-- INSTANCIACAO DE UM OBJETO DE Jogo
nivel            = Nivel.Nivel()  ##-- INSTANCIACAO DE UM OBJETO DE Nivel
grava            = NomeUser.NomeUser() ## --- Grava a bagaceira
#nivel.loadNivel( jogo.getNivel() )
menu             = Menu.Menu()
start            = Loop.Principal()
escolha          = EscolhePlayer.EscolhePlayer()
opcoes           = Opcoes.Opcoes()
instrucoes       = Instrucoes.Instrucoes()
creditos         = Creditos.Creditos()


nomeTile[1]  = "parede"
nomeTile[2]  = "grana"
nomeTile[3]  = "comida2"
nomeTile[4]  = "comida3"
nomeTile[5]  = "comida4"
nomeTile[6]  = "ghost-door"
nomeTile[7]  = "protetor"
nomeTile[20] = "portaHorizontal"
nomeTile[21] = "portaVertical"

##for i in range(23):
##    colete[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"colete"+os.sep+ "colete"+str(i)+".png").convert_alpha()
for i in range(36):
    turbo[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"turbo"+os.sep+str(i)+".png").convert_alpha()
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
    roda[i]  = pygame.image.load("data"+os.sep+"sprites"+os.sep+"rodas"+os.sep+ "0"+str(i)+".png").convert_alpha()


##--- MATRIZES CAMPO

matriz1 = [
[1,1,1,1,1,1,1,1,1,21,1,1,1,1,1,1,1,1,1],
[1,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,1],
[1,2,1,2,1,2,1,1,2,2,2,1,1,2,1,2,1,2,1],
[1,2,1,2,1,2,2,2,1,2,1,2,2,7,1,2,1,2,1],
[1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
[1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1],
[1,2,1,7,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1],
[1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1],
[1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,2,1,2,1],
[1,2,2,2,1,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
[1,1,1,2,1,1,2,1,1,10,1,1,2,1,1,2,1,1,1],
[20,2,2,2,2,2,2,2,11,12,13,2,2,2,2,2,2,2,20],
[1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,1,7,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1],
[1,2,1,2,1,2,2,2,2,4,2,2,2,2,1,2,1,2,1],
[1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,7,1,2,1],
[1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1],
[1,2,1,2,1,2,1,1,2,2,2,1,1,2,1,2,1,2,1],
[1,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,1],
[1,1,1,1,1,1,1,1,1,21,1,1,1,1,1,1,1,1,1]
]

matriz2 = [
[1,1,1,1,1,1,1,1,1,21,1,1,1,1,1,1,1,1,1],
[1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1],
[1,2,2,2,1,2,2,2,1,2,1,2,2,2,1,2,2,2,1],
[1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1],
[1,2,2,2,2,2,1,2,2,7,2,2,1,2,2,2,2,2,1],
[1,2,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,2,1,1,1],
[1,2,2,2,1,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
[1,1,2,1,1,1,2,1,1,10,1,1,2,1,1,1,2,1,1],
[20,2,2,2,2,7,2,2,11,12,13,2,2,7,2,2,2,2,20],
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

matriz3 = [
[1,21,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,21,1],
[1,2,2,1,2,1,2,1,2,2,2,1,2,1,2,1,2,2,1],
[1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1],
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
[1,2,1,2,2,2,2,1,2,1,2,1,2,2,2,2,1,2,1],
[1,2,7,1,1,1,2,1,2,1,2,1,2,1,1,1,7,2,1],
[1,21,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,21,1]
]

##--- IDIOMAS
idioma = "portugues"
idiomas = {
    "portugues":[["Inicio","Instrucoes","Creditos","Opcoes","Sair"],
                 ["SELECIONE SEU JOGADOR"],
                 ["DIGITE SEU NOME"],
                 ["INSTRUCOES"],
                 ["CREDITOS", "DESENVOLVEDORES"],
                 ["OPCOES", "MODO DE TELA","Tela Cheia","Tela Normal","IDIOMA","Portugues","Ingles","Espanhol","VOLUME","POSICOES"],
                 [],
                 [],
                 []
                 ],
    
    "ingles":[["Begin","Instructions","Credits","Options","Exit"],
              ["SELECT YOUR PLAYER"],
              ["ENTER YOUR NAME"],
              ["INSTRUCTIONS"],
              ["CREDITS","DEVELOPERS"],
              ["OPTIONS","DISPLAY MODE","Fullscreen","Normal Mode","LANGUAGE","Portuguese","English","Spanish","VOLUME","RANKING"],
              [],
              [],
              []
              ],

    "espanhol":[["Inicio","Instrucciones","Creditos","Opciones","Salida"],
                ["ELIGE TU JUGADOR"],
                ["INGRESSE SU NOMBRE"],
                ["INSTRUCCIONES"],
                ["CREDITOS","DESARROLLADORES"],
                ["OPCIONES", "MODO DE PANTALLA","Pantalla Completa","Pantalla Normal","LENGUAJE","Portugues","Ingles","Espanol","VOLUMEN","POSICIONES"],
                [],
                [],
                []
                ]
}
