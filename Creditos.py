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
            this.texto = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][4][0],True, (255,255,255))
            this.desenvolvedores = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][4][1],True, (0,0,0))
            this.jordao = Objetos.fonteHoliday.render("Jordao Ezequiel Serafim",True, (0,0,0))
            this.marcelo = Objetos.fonteHoliday.render("Marcelo Avelino Xavier",True, (0,0,0))

            
            Objetos.background.blit(this.texto, (225, 30))
            Objetos.background.blit(Objetos.papiro3, (60, 110))
            Objetos.background.blit(this.desenvolvedores, (140, 200))
            Objetos.background.blit(this.jordao, (100, 280))
            Objetos.background.blit(this.marcelo, (120, 330))

            pygame.display.update()

