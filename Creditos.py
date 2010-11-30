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
            this.desenvolvedores = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][4][1],True, (255,255,255))
            this.jordao = Objetos.fonteHoliday.render("Jordao Ezequiel",True, (255,255,255))
            this.emailJ = Objetos.fonteHoliday.render("jordaoesa at lcc.ufcg.edu.br",True, (255,255,255))
            this.marcelo = Objetos.fonteHoliday.render("Marcelo Avelino",True, (255,255,255))
            this.emailM = Objetos.fonteHoliday.render("marceloax at lcc.ufcg.edu.br",True, (255,255,255))

            
            Objetos.background.blit(this.texto, (225, 30))
            Objetos.background.blit(this.desenvolvedores, (150, 200))
            Objetos.background.blit(this.jordao, (170, 250))
            Objetos.background.blit(this.emailJ, (60, 280))
            Objetos.background.blit(this.marcelo, (170, 330))
            Objetos.background.blit(this.emailM, (60, 360))

            pygame.display.update()

