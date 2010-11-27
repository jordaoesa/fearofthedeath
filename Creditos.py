import pygame
from pygame.locals import *
import Objetos

class Creditos:

    def __init__(this):
        pass

    def run(this):

        while True:

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Objetos.menu.run()
                        

            print "creditos"
            Objetos.background.fill((255,255,255))
            pygame.display.update()

