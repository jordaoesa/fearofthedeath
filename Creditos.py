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
                        

            Objetos.background.blit(Objetos.fundoOpcoes, (0,0))
            this.texto = Objetos.fonteHoliday.render("CREDITOS",True, (255,255,255))

            Objetos.background.blit(this.texto, (225, 30))
            pygame.display.update()

