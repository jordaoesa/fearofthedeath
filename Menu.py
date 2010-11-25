import pygame
from pygame.locals import *
from sys import exit
import Loop

import os

class Menu:
	
	def __init__(self):
                
		pygame.init()
                
		self.start = Loop.Principal()
		
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
		
		self.fonte = pygame.font.Font("data"+os.sep+"fontes"+os.sep+"fonte.ttf", 50, bold = False)
		self.fonte1 = pygame.font.Font("data"+os.sep+"fontes"+os.sep+"fonte.ttf", 65, bold = True)
	
		self.titulo = self.fonte.render("Fear of The Death", True, (255,255,255))
		self.inicio = self.fonte.render("inicio", True, (255,255,255))
		self.instrucoes = self.fonte.render("instrucoes", True, (255,255,255))
		self.creditos = self.fonte.render("creditos", True, (255,255,255))
		self.voltar = self.fonte.render("sair", True, (255,255,255))

		self.titulo1 = self.fonte1.render("Fear of The Death", True, (205,205,205))
		self.inicio1 = self.fonte1.render("inicio", True, (205,105,105))
		self.instrucoes1 = self.fonte1.render("instrucoes", True, (205,105,105))
		self.creditos1 = self.fonte1.render("creditos", True, (205,105,105))
		self.voltar1 = self.fonte1.render("sair", True, (205,105,105))
		
	def run(self):

		while True:
			
			
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:	
						pygame.quit()
					
				mouse_pos = pygame.mouse.get_pos()
				mouse_press = pygame.mouse.get_pressed()
				#print mouse_press
						
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.titulo, (130, 50))
			
			
			
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

			self.screen.blit(self.image_grande, (200, 430))
			self.screen.blit(self.image_medio, (100, 500))
			self.screen.blit(self.image_pequeno, (0, 550))
			
			

			#para blitar os texto no menu, quando passar o mouse.			
						
			if 85 < mouse_pos[0] < 195 and 180 < mouse_pos[1] < 205:
				self.screen.blit(self.inicio1, (70, 165))
				self.som.play()
				if mouse_press[0]:
					self.start.run()
				
				#if pygame.mouse.get_pressed()[0] == True:
				#	jogo.game_run()
			else:
				self.screen.blit(self.inicio, (85, 170))
				#self.som.play()
				
				
					

			if 85 < mouse_pos[0] < 300 and 250 < mouse_pos[1] < 275:
				self.screen.blit(self.instrucoes1, (60, 230))
				#self.som.play()
			else:
				self.screen.blit(self.instrucoes, (85, 240))
				#self.som.play()


			if 85 < mouse_pos[0] < 255 and 320 < mouse_pos[1] < 350:
				self.screen.blit(self.creditos1, (70, 300))
				#self.som.play()
			else:
				self.screen.blit(self.creditos, (85, 310))
				#self.som.play()


			if 85 < mouse_pos[0] < 220 and 390 < mouse_pos[1] < 420:
				self.screen.blit(self.voltar1, (70, 370))
				#self.som.play()
				if mouse_press[0]:
					pygame.quit()
			else:
				self.screen.blit(self.voltar, (85, 380))
				#self.som.play()
			#self.som.stop()
				
			pygame.display.update()
			self.clock.tick(60)
			
game = Menu()
game.run()
