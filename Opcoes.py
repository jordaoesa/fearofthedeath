import pygame
from pygame.locals import *
import Objetos

class Opcoes:

    def __init__(this):
        pass

    def run(this):

        while True:

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Objetos.menu.run()
                    elif event.key == K_UP:
                        pygame.display.set_mode((608,672), FULLSCREEN, 32)
                    elif event.key == K_DOWN:
                        pygame.display.set_mode((608,672), 0, 32)
                        
            Objetos.background.blit(Objetos.fundoOpcoes, (0,0))
            this.texto = Objetos.fonteHoliday.render("OPCOES",True, (255,255,255))

            modoTela = Objetos.fonteHoliday.render("MODO DE TELA", True, (0,0,0))
            fullscreen = Objetos.fonteHoliday.render("Tela Cheia", True, (0,0,0))
            modoNormal = Objetos.fonteHoliday.render("Tela Normal", True, (0,0,0))

            idioma = Objetos.fonteHoliday.render("IDIOMA", True, (0,0,0))
            portugues = Objetos.fonteHoliday.render("Portugues", True, (0,0,0))
            ingles = Objetos.fonteHoliday.render("Ingles", True, (0,0,0))
            espanhol = Objetos.fonteHoliday.render("Espanhol", True, (0,0,0))

            volume = Objetos.fonteHoliday.render("VOLUME", True, (0,0,0))
            
            


            Objetos.background.blit(this.texto, (240, 30))

            pygame.display.update()

