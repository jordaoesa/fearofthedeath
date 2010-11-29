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

            print mouse_pos
            
            this.texto = Objetos.fonteHoliday.render("OPCOES",True, (255,255,255))

            modoTela = Objetos.fonteHoliday.render("MODO DE TELA", True, (255,255,255))
            fullscreen = Objetos.fonteHoliday.render("Tela Cheia", True, (255,255,255))
            modoNormal = Objetos.fonteHoliday.render("Tela Normal", True, (255,255,255))

            idioma = Objetos.fonteHoliday.render("IDIOMA", True, (255,255,255))
            portugues = Objetos.fonteHoliday.render("Portugues", True, (255,255,255))
            ingles = Objetos.fonteHoliday.render("Ingles", True, (255,255,255))
            espanhol = Objetos.fonteHoliday.render("Espanhol", True, (255,255,255))

            volume = Objetos.fonteHoliday.render("VOLUME", True, (255,255,255))
            volumeNum = Objetos.fonteHoliday.render("00", True, (255,255,255))

            
            if 100 <= mouse_pos[0] <= 280 and 185 <= mouse_pos[1] <= 210:
                fullscreen = Objetos.fonteHoliday.render("Tela Cheia", True, (255,0,0))
                if mouse_press[0]:
                    pygame.display.set_mode((608,672), FULLSCREEN, 32)

            elif 320 <= mouse_pos[0] <= 525 and 185 <= mouse_pos[1] <= 210:
                modoNormal = Objetos.fonteHoliday.render("Tela Normal", True, (255,0,0))
                if mouse_press[0]:
                    pygame.display.set_mode((608,672), 0, 32)

            elif 70 <= mouse_pos[0] <= 235 and 335 <= mouse_pos[1] <= 362:
                portugues = Objetos.fonteHoliday.render("Portugues", True, (255,0,0))
                if mouse_press[0]:
                    pass
            elif 270 <= mouse_pos[0] <= 370 and 335 <= mouse_pos[1] <= 362:
                ingles = Objetos.fonteHoliday.render("Ingles", True, (255,0,0))
                if mouse_press[0]:
                    pass
            elif 410 <= mouse_pos[0] <= 558 and 335 <= mouse_pos[1] <= 362:
                espanhol = Objetos.fonteHoliday.render("Espanhol", True, (255,0,0))
                if mouse_press[0]:
                    pass

            



            Objetos.background.blit(Objetos.fundoOpcoes, (0,0))

            Objetos.background.blit(this.texto, (240, 30))

            Objetos.background.blit(modoTela,(170, 130))
            Objetos.background.blit(fullscreen,(100, 180))
            Objetos.background.blit(modoNormal,(320, 180))
            
            Objetos.background.blit(idioma,(240, 280))
            Objetos.background.blit(portugues,(70,330))
            Objetos.background.blit(ingles,(270,330))
            Objetos.background.blit(espanhol,(410,330))

            Objetos.background.blit(volume,(240,430))
            Objetos.background.blit(volumeNum, (280,480))
            
            

            pygame.display.update()

