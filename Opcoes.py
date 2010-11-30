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

            #print mouse_pos
            #print pygame.mouse.get_rel()
            
            this.texto = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][0],True, (139, 0, 0))

            modoTela = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][1], True, (139, 0, 0))
            fullscreen = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][2], True, (0, 255, 0))
            modoNormal = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][3], True, (255, 255, 0))

            idioma = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][4], True, (79, 79, 79))
            portugues = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][5], True, (255, 255, 255))
            ingles = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][6], True, (169, 169, 169))
            espanhol = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][7], True, (139, 0, 0))

            volume = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][8], True, (130, 130, 130))
            volumeNum = Objetos.fonteHoliday.render(str(Objetos.volume), True, (169, 169, 169))

            ranking = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][9], True, (255, 255, 255))

            
            if 100 <= mouse_pos[0] <= 280 and 185 <= mouse_pos[1] <= 210:
                fullscreen = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][2], True, (255,0,0))
                if mouse_press[0]:
                    pygame.display.set_mode((608,672), FULLSCREEN, 32)

            elif 320 <= mouse_pos[0] <= 525 and 185 <= mouse_pos[1] <= 210:
                modoNormal = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][3], True, (255,0,0))
                if mouse_press[0]:
                    pygame.display.set_mode((608,672), 0, 32)

            elif 70 <= mouse_pos[0] <= 235 and 335 <= mouse_pos[1] <= 362:
                portugues = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][5], True, (255,0,0))
                if mouse_press[0]:
                    Objetos.idioma = "portugues"
                    #print "portugues"
            elif 270 <= mouse_pos[0] <= 370 and 335 <= mouse_pos[1] <= 362:
                ingles = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][6], True, (255,0,0))
                if mouse_press[0]:
                    Objetos.idioma = "ingles"
                    #print "ingles"
            elif 410 <= mouse_pos[0] <= 558 and 335 <= mouse_pos[1] <= 362:
                espanhol = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][7], True, (255,0,0))
                if mouse_press[0]:
                    Objetos.idioma = "espanhol"
                    #print "espanhol"
            elif 277 <= mouse_pos[0] <= 333 and 485 <= mouse_pos[1] <= 508:
                #print "vol"
                if 0 <= Objetos.volume <= 100:
                    for event in pygame.event.get(): 
                        if event.type == MOUSEBUTTONDOWN:                        
                            if event.button == 4 and Objetos.volume != 100:
                                Objetos.volume += 5
                                Objetos.sndMoeda.set_volume(Objetos.volume/100.0)
                            elif event.button == 4 and Objetos.volume == 100:
                                Objetos.sndMoeda.play()
                            if event.button == 5 and Objetos.volume != 0:
                                Objetos.volume -= 5
                                Objetos.sndMoeda.set_volume(Objetos.volume/100.0)
                            elif event.button == 5 and Objetos.volume == 0:
                                Objetos.sndMoeda.play()
                            #print event.button
                
                volumeNum = Objetos.fonteHoliday.render(str(Objetos.volume), True, (255,0,0))
                if 0 <= Objetos.volume <= 100:
                    if mouse_press[0] and Objetos.volume != 100:
                        Objetos.volume += 1
                        Objetos.sndMoeda.set_volume(Objetos.volume/100.0)
                    elif mouse_press[0] and Objetos.volume == 100:
                        Objetos.sndMoeda.play()
                    if mouse_press[2] and Objetos.volume != 0:
                        Objetos.volume -= 1
                        Objetos.sndMoeda.set_volume(Objetos.volume/100.0)
                    elif mouse_press[2] and Objetos.volume == 0:
                        Objetos.sndMoeda.play()
            elif 223 <= mouse_pos[0] <= 385 and 553 <= mouse_pos[1] <= 578:
                ranking = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][9], True, (255,0,0))
                if mouse_press[0]:
                    print "ranking"

            



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

            Objetos.background.blit(ranking, (225,550))
            
            

            pygame.display.update()

