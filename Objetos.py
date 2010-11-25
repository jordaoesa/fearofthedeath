import pygame
import os
import Player
import Fantasma
import Jogo
import NomeUser
import Nivel
import Funcoes


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

claude    = Player.Claude() ##-- INSTANCIACAO DE UM OBJETO DE Claude
fantasma  = Fantasma.Fantasma()
fantasma1 = Fantasma.Fantasma()
fantasma2 = Fantasma.Fantasma()
fantasma3 = Fantasma.Fantasma()
##protect   = Colete()
##protect1  = Colete()
##protect2  = Colete()
##protect3  = Colete()
nomeTile  = {}       ##-- ARMAZENA OS NOMES DOS TILES
colete    = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA COLETE
grana     = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA GRANA
parede    = {}       ##-- ARMAZENA TODOS OS SPRITES USADOS PARA PAREDE
jogo      = Jogo.Jogo()   ##-- INSTANCIACAO DE UM OBJETO DE Jogo
nivel     = Nivel.Nivel()  ##-- INSTANCIACAO DE UM OBJETO DE Nivel

grava     = NomeUser.NomeUser() ## --- Grava a bagaceira

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