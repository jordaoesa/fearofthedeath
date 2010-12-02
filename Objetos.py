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


##--- IMAGEM VIDA
imgVida = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"vida.png").convert_alpha()

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

##--- FUNDO OPCOES
fundoOpcoes = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"fundoOpcoes.png").convert_alpha()

##--- INSTRUCOES
botoes = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"botoes.png").convert_alpha()
papiro = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"papiro.png").convert_alpha()
papiro1 = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"papiro1.png").convert_alpha()
papiro2 = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"papiro2.png").convert_alpha()
papiro3 = pygame.image.load("data"+os.sep+"sprites"+os.sep+"fundo"+os.sep+"papiro3.png").convert_alpha()

##--- INICIANDO SONS
musicas = [pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"0"+str(i)+".ogg") for i in range(7)]
sndMoeda = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"playerMoeda.ogg")
sndMorte = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"playerMorte.ogg")
sndAlerta = pygame.mixer.Sound("data"+os.sep+"sons"+os.sep+"playerMoeda.ogg")

##--- FONTES
fonteHoliday = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'Holiday.ttf',30,bold = False)
fonteHoliday20 = pygame.font.Font("data" + os.sep + "fontes" + os.sep + 'Holiday.ttf',20,bold = False)

sonic            = Player.Sonic() ##-- INSTANCIACAO DE UM OBJETO DE SONIC
fantasma         = Fantasma.Fantasma()
fantasma1        = Fantasma.Fantasma()
fantasma2        = Fantasma.Fantasma()
fantasma3        = Fantasma.Fantasma()
nomeTile         = {} ##-- ARMAZENA OS NOMES DOS TILES
parede           = {} ##-- ARMAZENA TODOS OS SPRITES USADOS PARA PAREDE
turbo            = {} ##--- ARMAZENA OS SPRITES DO MODO TURBO
imgPlayer        = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
shadowPlayer     = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
knucklesPlayer   = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
sonicPlayer      = {"playerB":{}, "playerE":{},"playerD":{},"playerC":{}}
roda             = {} ##-- MOEDA PLAYER
jogo             = Jogo.Jogo() ##-- INSTANCIACAO DE UM OBJETO DE Jogo
nivel            = Nivel.Nivel() ##-- INSTANCIACAO DE UM OBJETO DE Nivel
grava            = NomeUser.NomeUser() ## --- Grava a bagaceira
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
    
    roda[i]  = pygame.image.load("data"+os.sep+"sprites"+os.sep+"rodas"+os.sep+ "0"+str(i)+".png").convert_alpha()

for i in range(1,5):
    parede[i] = pygame.image.load("data"+os.sep+"sprites"+os.sep+"paredes"+os.sep+ "parede"+str(i)+".jpg").convert_alpha()

##--- MATRIZES CAMPO

matriz1 = [
[1,1,21,1,1,1,1,1,1,1,1,1,1,1,1,1,21,1,1],
[1,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,1,1],
[20,7,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,7,20],
[1,1,2,1,2,2,2,2,2,1,2,2,2,2,2,1,2,1,1],
[1,2,2,2,2,1,1,1,2,1,2,1,1,1,2,2,2,2,1],
[1,2,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
[1,2,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1],
[1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1],
[1,1,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,1,1],
[1,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,1],
[1,1,1,1,1,2,2,11,12,13,10,2,2,2,1,1,1,1,1],
[1,2,2,2,2,2,1,1,1,1,1,1,2,1,2,2,2,2,1],
[1,2,1,1,1,2,2,2,2,1,2,2,2,1,1,1,1,1,1],
[1,2,2,2,2,1,1,1,2,1,2,1,1,2,2,2,2,2,1],
[1,1,1,1,2,2,2,2,2,1,2,2,2,1,1,1,1,2,1],
[1,2,2,2,2,1,2,1,2,4,2,1,2,2,2,2,2,2,1],
[1,2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1],
[1,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,1,1],
[20,7,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,7,20],
[1,1,7,2,2,2,2,2,2,1,2,2,2,2,2,2,2,1,1],
[1,1,21,1,1,1,1,1,1,1,1,1,1,1,1,1,21,1,1]
]

matriz2 = [
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

matriz3 = [
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

matriz4 = [
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
                 ["INSTRUCOES","Utilize os botoes do","teclado direcional para","mover o seu jogador","O objetivo do jogo","eh pegar a maior","quantidade de moedas","Pegue os super booster","aumente sua velocidade e","se proteja dos fantasmas"],
                 ["CREDITOS", "DESENVOLVEDORES","COLABORADORES"],
                 ["OPCOES", "MODO DE TELA","Tela Cheia","Tela Normal","IDIOMA","Portugues","Ingles","Espanhol","VOLUME","POSICOES"],
                 ["POSICOES","Nao ha Resultados"],
                 ["Carregando...","VOCE VENCEU","PERDEU MANOLO"],
                 ["Pontos: ","Vidas: ","Turbo: "]
                 ],
    
    "ingles":[["Begin","Instructions","Credits","Options","Exit"],
              ["SELECT YOUR PLAYER"],
              ["ENTER YOUR NAME"],
              ["INSTRUCTIONS","Use keyboard directional", "buttons to move", "your player", "The goal of the game", "is to get the most", "amounty of coins", "Take the super booster", "increase your speed and", "protect yourself from ghosts"],
              ["CREDITS","DEVELOPERS","CONTRIBUTORS"],
              ["OPTIONS","DISPLAY MODE","Fullscreen","Normal Mode","LANGUAGE","Portuguese","English","Spanish","VOLUME","RANKING"],
              ["RANKING", "No hay Resultados"],
              ["Loading...","YOU WIN","LOST MANOLO"],
              ["Score: ","Lifes: ","Turbo: "]
              ],

    "espanhol":[["Inicio","Instrucciones","Creditos","Opciones","Salida"],
                ["ELIGE TU JUGADOR"],
                ["INGRESSE SU NOMBRE"],
                ["INSTRUCCIONES","Utilice los botones del", "teclado direccional para", "mover el jugador", "El objetivo del juego", "es obtener la mayor", "cantidad de monedas", "Obtena el refuerzo super", "aumenta su velocidad y", "protejase de los fantasmas"],
                ["CREDITOS","DESARROLLADORES","COLABORADORES"],
                ["OPCIONES", "MODO DE PANTALLA","Pantalla Completa","Pantalla Normal","IDIOMA","Portugues","Ingles","Espanol","VOLUMEN","POSICIONES"],
                ["POSICIONES","No Results"],
                ["Cargando...","HAS GANADO","MANOLO PERDIDO"],
                ["Puntos: ","Vidas: ","Turbo: "]
                ]
}
