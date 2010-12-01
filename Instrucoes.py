import pygame
from pygame.locals import *
import Objetos

class Instrucoes:

    def __init__(this):
        this.cont       = 0
        this.animaRoda  = 0
        this.animaTurbo = 0

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
                        this.cont = 0
                        Objetos.menu.run()
                        
            Objetos.background.blit(Objetos.fundoOpcoes, (0,0))
            
            if this.cont == 0:
                Objetos.background.blit(Objetos.botoes, (250, 180))
                this.texto1 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][1], True,(0,0,0))
                this.texto2 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][2], True, (0,0,0))
                this.texto3 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][3], True, (0,0,0))
                this.texto4 = Objetos.fonteHoliday.render("...", True, (255,255,255))
                Objetos.background.blit(Objetos.papiro, (40, 320))
                Objetos.background.blit(this.texto1, (110, 370))
                Objetos.background.blit(this.texto2, (110, 400))
                Objetos.background.blit(this.texto3, (110, 430))

                if 545 <= mouse_pos[0] <= 585 and 614 <= mouse_pos[1] <= 633:
                    this.texto4 = Objetos.fonteHoliday.render("...", True, (255,0,0))
                    for event in pygame.event.get(): 
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                this.cont += 1
                Objetos.background.blit(this.texto4, (550, 600))
                
            elif this.cont == 1:
                image = Objetos.roda[0]
                if this.animaRoda > 20:
                    this.animaRoda = 0
                this.animaRoda += 0.5
                if this.animaRoda <= 5: image    = Objetos.roda[0]
                elif this.animaRoda <= 10: image = Objetos.roda[1]
                elif this.animaRoda <= 15: image = Objetos.roda[2]
                elif this.animaRoda <= 20: image = Objetos.roda[3]
                
                Objetos.background.blit(image, (260, 180))
                Objetos.background.blit(image, (280, 180))
                Objetos.background.blit(image, (300, 180))
                Objetos.background.blit(image, (320, 180))
                Objetos.background.blit(image, (260, 210))
                Objetos.background.blit(image, (280, 210))
                Objetos.background.blit(image, (300, 210))
                Objetos.background.blit(image, (320, 210))
                Objetos.background.blit(image, (260, 240))
                Objetos.background.blit(image, (280, 240))
                Objetos.background.blit(image, (300, 240))
                Objetos.background.blit(image, (320, 240))
                this.texto1 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][4], True,(0,0,0))
                this.texto2 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][5], True, (0,0,0))
                this.texto3 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][6], True, (0,0,0))
                this.texto4 = Objetos.fonteHoliday.render("...", True, (255,255,255))
                this.texto5 = Objetos.fonteHoliday.render("...", True, (255,255,255))
                Objetos.background.blit(Objetos.papiro, (40, 320))
                Objetos.background.blit(this.texto1, (120, 370))
                Objetos.background.blit(this.texto2, (140, 400))
                Objetos.background.blit(this.texto3, (120, 430))
                if 545 <= mouse_pos[0] <= 585 and 614 <= mouse_pos[1] <= 633:
                    this.texto4 = Objetos.fonteHoliday.render("...", True, (255,0,0))
                    for event in pygame.event.get(): 
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                this.cont += 1
                if 25 <= mouse_pos[0] <= 65 and 614 <= mouse_pos[1] <= 633:
                    this.texto5 = Objetos.fonteHoliday.render("...", True, (255,0,0))
                    for event in pygame.event.get(): 
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1 and this.cont > 0:
                                this.cont -= 1
                Objetos.background.blit(this.texto4, (550, 600))
                Objetos.background.blit(this.texto5, (30, 600))
                
            elif this.cont == 2:
                image = Objetos.turbo[0]
                if this.animaTurbo >= 181:
                    this.animaTurbo = 0
                this.animaTurbo += 1
                
                if this.animaTurbo <= 5:     image = Objetos.turbo[0]
                elif this.animaTurbo <= 10:  image = Objetos.turbo[1]
                elif this.animaTurbo <= 15:  image = Objetos.turbo[2]
                elif this.animaTurbo <= 20:  image = Objetos.turbo[3]
                elif this.animaTurbo <= 25:  image = Objetos.turbo[4]
                elif this.animaTurbo <= 30:  image = Objetos.turbo[5]
                elif this.animaTurbo <= 35:  image = Objetos.turbo[6]
                elif this.animaTurbo <= 40:  image = Objetos.turbo[7]
                elif this.animaTurbo <= 45:  image = Objetos.turbo[8]
                elif this.animaTurbo <= 50:  image = Objetos.turbo[9]
                elif this.animaTurbo <= 55:  image = Objetos.turbo[10]
                elif this.animaTurbo <= 60:  image = Objetos.turbo[11]
                elif this.animaTurbo <= 65:  image = Objetos.turbo[12]
                elif this.animaTurbo <= 70:  image = Objetos.turbo[13]
                elif this.animaTurbo <= 75:  image = Objetos.turbo[14]
                elif this.animaTurbo <= 80:  image = Objetos.turbo[15]
                elif this.animaTurbo <= 85:  image = Objetos.turbo[16]
                elif this.animaTurbo <= 90:  image = Objetos.turbo[17]
                elif this.animaTurbo <= 95:  image = Objetos.turbo[18]
                elif this.animaTurbo <= 100: image = Objetos.turbo[19]
                elif this.animaTurbo <= 105: image = Objetos.turbo[20]
                elif this.animaTurbo <= 110: image = Objetos.turbo[21]
                elif this.animaTurbo <= 115: image = Objetos.turbo[22]
                elif this.animaTurbo <= 120: image = Objetos.turbo[23]
                elif this.animaTurbo <= 125: image = Objetos.turbo[24]
                elif this.animaTurbo <= 130: image = Objetos.turbo[25]
                elif this.animaTurbo <= 135: image = Objetos.turbo[26]
                elif this.animaTurbo <= 140: image = Objetos.turbo[27]
                elif this.animaTurbo <= 145: image = Objetos.turbo[28]
                elif this.animaTurbo <= 150: image = Objetos.turbo[29]
                elif this.animaTurbo <= 155: image = Objetos.turbo[30]
                elif this.animaTurbo <= 160: image = Objetos.turbo[31]
                elif this.animaTurbo <= 165: image = Objetos.turbo[32]
                elif this.animaTurbo <= 170: image = Objetos.turbo[33]
                elif this.animaTurbo <= 175: image = Objetos.turbo[34]
                elif this.animaTurbo <= 180: image = Objetos.turbo[35]

                Objetos.background.blit(image, (250, 180))
                Objetos.background.blit(image, (280, 180))
                Objetos.background.blit(image, (310, 180))
                Objetos.background.blit(image, (340, 180))
                Objetos.background.blit(image, (250, 210))
                Objetos.background.blit(image, (280, 210))
                Objetos.background.blit(image, (310, 210))
                Objetos.background.blit(image, (340, 210))
                Objetos.background.blit(image, (250, 240))
                Objetos.background.blit(image, (280, 240))
                Objetos.background.blit(image, (310, 240))
                Objetos.background.blit(image, (340, 240))
                
                this.texto1 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][7], True,(0,0,0))
                this.texto2 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][8], True, (0,0,0))
                this.texto3 = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][9], True, (0,0,0))
                this.texto4 = Objetos.fonteHoliday.render("...", True, (255,255,255))
                this.texto5 = Objetos.fonteHoliday.render("...", True, (255,255,255))
                Objetos.background.blit(Objetos.papiro, (40, 320))
                Objetos.background.blit(this.texto1, (110, 370))
                Objetos.background.blit(this.texto2, (100, 400))
                Objetos.background.blit(this.texto3, (70, 430))
                if 545 <= mouse_pos[0] <= 585 and 614 <= mouse_pos[1] <= 633:
                    this.texto4 = Objetos.fonteHoliday.render("...", True, (255,0,0))
                    for event in pygame.event.get(): 
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                this.cont += 1
                if 25 <= mouse_pos[0] <= 65 and 614 <= mouse_pos[1] <= 633:
                    this.texto5 = Objetos.fonteHoliday.render("...", True, (255,0,0))
                    for event in pygame.event.get(): 
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1 and this.cont > 0:
                                this.cont -= 1
                Objetos.background.blit(this.texto4, (550, 600))
                Objetos.background.blit(this.texto5, (30, 600))
                
            elif this.cont == 3:
                this.cont = 0
                Objetos.menu.run()
            
            this.texto = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][3][0],True, (255,255,255))
            
            Objetos.background.blit(this.texto, (215, 30))
            pygame.display.update()

