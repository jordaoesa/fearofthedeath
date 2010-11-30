import pygame
from pygame.locals import *
import Objetos

class Instrucoes:

    def __init__(this):
        this.cont = 0

    def run(this):

        while True:
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            key_press = pygame.key.get_pressed()

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Objetos.menu.run()
                if event.type == MOUSEBUTTONDOWN:
                    print event.button
                    if event.button == 1:
                        this.cont += 1
                    elif event.button == 3:
                        if this.cont > 0:
                            this.cont -= 1
            #print this.cont
            Objetos.background.blit(Objetos.fundoOpcoes, (0,0))

            if this.cont == 0:
                Objetos.background.blit(Objetos.sonicFala, (100, 100))
            elif this.cont == 1:
                Objetos.background.blit(Objetos.knucklesFala, (100, 100))
            elif this.cont == 2:
                Objetos.background.blit(Objetos.shadowFala, (100, 100))
            elif this.cont == 3:
                this.cont = 0
                Objetos.menu.run()
                
            this.texto = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][0],True, (255,255,255))
            
            Objetos.background.blit(this.texto, (215, 30))
            pygame.display.update()

