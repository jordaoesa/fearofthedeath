import pygame
from pygame.locals import *
import Objetos

class EscolhePlayer:

    def __init__(this):
        this.user = ""

    def selectPlayer(this):

        while True:

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Objetos.menu.run()
                    elif event.key == K_RETURN:
                        Objetos.jogo.novoJogo()
                        Objetos.grava.screenName()
                        Objetos.start.run()

            print "escolhe"
            Objetos.background.fill((255,255,255))
            pygame.display.update()
