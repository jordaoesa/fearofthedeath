# -*- coding: cp1252 -*-

import pygame
from pygame.locals import *
import os
import Objetos
import random



class Menu:
	
    def __init__(self):

        Objetos.sndTema.play(-1)
        
        pygame.init()

        self.image_grande = pygame.image
        self.image_medio = pygame.image
        self.image_pequeno = pygame.image
        self.animaFantasma = 0

        self.som = pygame.mixer.Sound("data" +os.sep+ "sons" + "menu.wav")

        self.screen = pygame.display.set_mode((608, 672), 0, 32)
        self.background = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fundoMenu.jpg").convert()
        self.fantasma = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma.png").convert_alpha()
        self.fantasma1 = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma1.png").convert_alpha()
        self.fantasma2 = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma2.png").convert_alpha()

        self.fantasma_medio = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma_medio.png").convert_alpha()
        self.fantasma_medio1 = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma_medio1.png").convert_alpha()
        self.fantasma_medio2 = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma_medio2.png").convert_alpha()

        self.fantasma_pequeno = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma_pequeno.png").convert_alpha()
        self.fantasma_pequeno1 = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma_pequeno1.png").convert_alpha()
        self.fantasma_pequeno2 = pygame.image.load("data" +os.sep+ "sprites" +os.sep+ "fundo" +os.sep+"fantasma_pequeno2.png").convert_alpha()

        self.clock = pygame.time.Clock();
        self.x = 0
        self.y = 0

        self.fonte = pygame.font.Font("data"+os.sep+"fontes"+os.sep+"Holiday.ttf", 40, bold = False)
        self.fonte1 = pygame.font.Font("data"+os.sep+"fontes"+os.sep+"Holiday.ttf", 55, bold = True)

##        self.font = pygame.font.SysFont("courrier new", 40, bold = False)
##        self.i = self.font.render("cr�ditos", True, (255,255,255))

    def run(self):

        
        
        self.titulo = self.fonte.render("Fear of The Death", True, (255,255,255))
        self.inicio = self.fonte.render(Objetos.idiomas[Objetos.idioma][0][0], True, (255,255,255))
        self.instrucoes = self.fonte.render(Objetos.idiomas[Objetos.idioma][0][1], True, (255,255,255))
        self.creditos = self.fonte.render(Objetos.idiomas[Objetos.idioma][0][2], True, (255,255,255))
        self.opcoes = self.fonte.render(Objetos.idiomas[Objetos.idioma][0][3], True, (255,255,255))
        self.sair = self.fonte.render(Objetos.idiomas[Objetos.idioma][0][4], True, (255,255,255))

        self.titulo1 = self.fonte1.render("Fear of The Death", True, (205,205,205))
        self.inicio1 = self.fonte1.render(Objetos.idiomas[Objetos.idioma][0][0], True, (255,0,0))
        self.instrucoes1 = self.fonte1.render(Objetos.idiomas[Objetos.idioma][0][1], True, (255,0,0))
        self.creditos1 = self.fonte1.render(Objetos.idiomas[Objetos.idioma][0][2], True, (255,0,0))
        self.opcoes1 = self.fonte1.render(Objetos.idiomas[Objetos.idioma][0][3], True, (255,0,0))
        self.sair1 = self.fonte1.render(Objetos.idiomas[Objetos.idioma][0][4], True, (255,0,0))
        
        self.cont1 = True
        self.cont2 = True
        self.cont3 = True
        self.cont4 = True
        self.cont5 = True
        self.ve1, self.ve2, self.ve3, self.ve4 = True, False, False, False

        #variavel do fantasma
        x = -170
        x1 = -350
        x2 = -500
        y = random.randint(-100, 580)
        y1 = y + 50
        y2 = y + 80
        v = False
        
        while True:

            
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:	
                        pygame.quit()
                            
            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
                                    
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.titulo, (130, 50))
            
            if not v:

                self.animaFantasma += 1
                if self.animaFantasma == 15:
                    self.animaFantasma = 0

                if self.animaFantasma <= 5:
                    self.image_grande = self.fantasma1
                    self.image_medio = self.fantasma_medio1
                    self.image_pequeno = self.fantasma_pequeno1

                elif self.animaFantasma <= 10:
                    self.image_grande = self.fantasma
                    self.image_medio = self.fantasma_medio
                    self.image_pequeno = self.fantasma_pequeno

                elif self.animaFantasma <= 15:
                    self.image_grande = self.fantasma2
                    self.image_medio = self.fantasma_medio2
                    self.image_pequeno = self.fantasma_pequeno2

                
                if self.ve1:
                    x+=1
                    #x1+=1
                    #x2+=1
                elif self.ve2:
                    y+=1
                    #y1+=1
                    #y2+=1
                elif self.ve3:
                    y-=1
                    #y1-=1
                    #y2-=1
                elif self.ve4:
                    x-=1
                    #x1-=1
                    #x2-=1

                if x >= 608:
                    self.ve1 = False
                    self.ve2 = True
                    self.ve3 = False
                    self.ve4 = False
                    x = random.randint(0, 400)
                    y = -170
                    
                elif y >= 672:
                    self.ve1 = False
                    self.ve2 = False
                    self.ve3 = True
                    self.ve4 = False
                    x = random.randint(0, 400)
                    y = 672
                    
                elif y <= -170:
                    self.ve1 = False
                    self.ve2 = False
                    self.ve3 = False
                    self.ve4 = True
                    x = 608
                    y = random.randint(0, 580)
                    
                elif x <= -170:
                    self.ve1 = True
                    self.ve2 = False
                    self.ve3 = False
                    self.ve4 = False
                    x = -170
                    y = random.randint(0, 580)
                    
                    
                    

                self.screen.blit(self.image_grande, (x, y))

                #if x >= 30:
                #self.screen.blit(self.image_medio, (x1, y1))

                #if x1 >= 30:
                #self.screen.blit(self.image_pequeno, (x2, y2))
                  
##                x1 += 1
##                #y1+=1
##                if x1 >= 580:
##                    x1 = -170
##                    y1 = y + 50
##
##                x2 += 1
##                #y2+=1
##                if x2 >= 580:
##                    x2 = -170
##                    y2 = y + 80
            ##--- Inicio  
            if 85 < mouse_pos[0] < 195 and 180 < mouse_pos[1] < 205:
                temp1 = self.cont1
                self.screen.blit(self.inicio1, (70, 165))

                if temp1:
                    self.som.play()
                self.cont1 = False
                
                if mouse_press[0]:
                    #Objetos.sndTema.stop()
                    Objetos.escolha.selectPlayer()
            else:
                self.screen.blit(self.inicio, (85, 170))
                self.cont1 = True

            ##--- Instrucoes
            if 85 < mouse_pos[0] < 300 and 250 < mouse_pos[1] < 275:
                temp2 = self.cont2
                self.screen.blit(self.instrucoes1, (60, 230))
                if temp2:
                    self.som.play()
                self.cont2 = False

                if mouse_press[0]:
                    #Objetos.sndTema.stop()
                    Objetos.instrucoes.run()
            else:
                self.screen.blit(self.instrucoes, (85, 240))
                self.cont2 = True

            ##--- Creditos
            if 85 < mouse_pos[0] < 255 and 320 < mouse_pos[1] < 350:
                temp3 = self.cont3
                self.screen.blit(self.creditos1, (70, 300))
                if temp3:
                    self.som.play()
                self.cont3 = False

                if mouse_press[0]:
                    #Objetos.sndTema.stop()
                    Objetos.creditos.run()
            else:
                self.screen.blit(self.creditos, (85, 310))
                self.cont3 = True


            ##--- Opcoes
            if 85 < mouse_pos[0] < 220 and 390 < mouse_pos[1] < 420:
                temp4 = self.cont4
                self.screen.blit(self.opcoes1, (70, 370))
                if temp4:
                    self.som.play()
                self.cont4 = False

                if mouse_press[0]:
                    #Objetos.sndTema.stop()
                    Objetos.opcoes.run()
                
            else:
                self.screen.blit(self.opcoes, (85, 380))
                self.cont4 = True

            ##--- Sair
            if 85 < mouse_pos[0] < 175 and 460 < mouse_pos[1] < 490:
                temp5 = self.cont5
                self.screen.blit(self.sair1, (75, 440))
                if temp5:
                    self.som.play()
                self.cont5 = False
                if mouse_press[0]:
                    #Objetos.sndTema.stop()
                    pygame.quit()
            else:
                self.screen.blit(self.sair, (85, 450))
                self.cont5 = True
                    
            pygame.display.update()
            self.clock.tick(60)
