import pygame, os
from pygame.locals import *
import Objetos

class EscolhePlayer:

    def __init__(this):
        this.player = ""

    def selectPlayer(this):

        while True:

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Objetos.menu.run()
            
            Objetos.background.blit(Objetos.fundoSelect, (0,0))

            this.texto = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][1][0],True, (255,255,255))
            Objetos.background.blit(this.texto, (100, 30))
            
            if 11 <= mouse_pos[0] <= 186 and 250 <= mouse_pos[1] <= 650:
                Objetos.background.blit(Objetos.fundoSelect1, (0,0))
                Objetos.background.blit(this.texto, (100, 30))
                Objetos.background.blit(Objetos.selectedShadow, (254,70))
                if mouse_press[0]:
                    this.player = "shadow"
                    Objetos.imgPlayer = Objetos.shadowPlayer
                    Objetos.jogo.novoJogo()
                    Objetos.grava.screenName()
                    Objetos.start.run()
            elif 196 <= mouse_pos[0] <= 409 and 252 <= mouse_pos[1] <= 650:
                Objetos.background.blit(Objetos.fundoSelect1, (0,0))
                Objetos.background.blit(this.texto, (100, 30))
                Objetos.background.blit(Objetos.selectedKnuckles, (254,70))
                if mouse_press[0]:
                    this.player = "knuckles"
                    Objetos.imgPlayer = Objetos.knucklesPlayer
                    Objetos.jogo.novoJogo()
                    Objetos.grava.screenName()
                    Objetos.start.run()
            elif 429 <= mouse_pos[0] <= 600 and 265 <= mouse_pos[1] <= 650:
                Objetos.background.blit(Objetos.fundoSelect1, (0,0))
                Objetos.background.blit(this.texto, (100, 30))
                Objetos.background.blit(Objetos.selectedSonic, (254,70))
                if mouse_press[0]:
                    this.player = "sonic"
                    Objetos.imgPlayer = Objetos.sonicPlayer
                    Objetos.jogo.novoJogo()
                    Objetos.grava.screenName()
                    Objetos.start.run()
                    
            pygame.display.update()
