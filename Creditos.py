import pygame
from pygame.locals import *
import Objetos

class Creditos:

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
                    elif event.key == K_RETURN:
                        Objetos.menu.run()
                        

            Objetos.background.blit(Objetos.fundoOpcoes, (0,0))
            this.texto = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][4][0],True, (255,255,255))
            this.desenvolvedores = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][4][1],True, (0,0,0))
            this.jordao = Objetos.fonteHoliday.render("Jordao Ezequiel Serafim",True, (0,0,0))
            this.marcelo = Objetos.fonteHoliday.render("Marcelo Avelino Xavier",True, (0,0,0))
            this.colaboradores = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][4][2],True, (0,0,0))
            this.colaborador1 = Objetos.fonteHoliday.render("Gustavo Pereira",True, (0,0,0))
            this.colaborador2 = Objetos.fonteHoliday.render("Jose Arthur Morais",True, (0,0,0))
            this.voltar = Objetos.fonteHoliday.render("...", True, (255,255,255))

            if 545 <= mouse_pos[0] <= 585 and 614 <= mouse_pos[1] <= 633:
                this.voltar = Objetos.fonteHoliday.render("...", True, (255,0,0))
                for event in pygame.event.get(): 
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            Objetos.menu.run()
            Objetos.background.blit(this.voltar, (550, 600))
            
            Objetos.background.blit(this.texto, (225, 30))
            Objetos.background.blit(Objetos.papiro3, (60, 110))
            Objetos.background.blit(this.desenvolvedores, (140, 170))
            Objetos.background.blit(this.jordao, (100, 220))
            Objetos.background.blit(this.marcelo, (120, 260))
            Objetos.background.blit(this.colaboradores, (160, 310))
            Objetos.background.blit(this.colaborador1, (170, 360))
            Objetos.background.blit(this.colaborador2, (140, 400))

            pygame.display.update()

