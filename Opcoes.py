import pygame, os
from pygame.locals import *
import Objetos

class Opcoes:     

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
            
            this.texto = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][0],True, (255,255,255))

            this.modoTela = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][1], True, (0,0,0))
            this.fullscreen = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][2], True, (0,0,0))
            this.modoNormal = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][3], True, (0,0,0))

            this.idioma = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][4], True, (0,0,0))
            this.portugues = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][5], True, (0,0,0))
            this.ingles = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][6], True, (0,0,0))
            this.espanhol = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][7], True, (0,0,0))

            this.volume = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][8], True, (0,0,0))
            this.volumeNum = Objetos.fonteHoliday.render(str(Objetos.volume), True, (0,0,0))

            this.posicoes = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][9], True, (0,0,0))


            ##--- TELA CHEIA
            if 100 <= mouse_pos[0] <= 280 and 185 <= mouse_pos[1] <= 210:
                this.fullscreen = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][2], True, (255,0,0))
                if mouse_press[0]:
                    pygame.display.set_mode((608,672), FULLSCREEN, 32)

            ##--- TELA NORMAL
            elif 320 <= mouse_pos[0] <= 525 and 185 <= mouse_pos[1] <= 210:
                this.modoNormal = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][3], True, (255,0,0))
                if mouse_press[0]:
                    pygame.display.set_mode((608,672), 0, 32)

            ##--- IDIOMA PORTUGUES
            elif 70 <= mouse_pos[0] <= 235 and 335 <= mouse_pos[1] <= 362:
                this.portugues = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][5], True, (255,0,0))
                if mouse_press[0]:
                    Objetos.idioma = "portugues"

            ##--- IDIOMA INGLES
            elif 270 <= mouse_pos[0] <= 370 and 335 <= mouse_pos[1] <= 362:
                this.ingles = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][6], True, (255,0,0))
                if mouse_press[0]:
                    Objetos.idioma = "ingles"

            ##--- IDIOMA ESPANHOL
            elif 410 <= mouse_pos[0] <= 558 and 335 <= mouse_pos[1] <= 362:
                this.espanhol = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][7], True, (255,0,0))
                if mouse_press[0]:
                    Objetos.idioma = "espanhol"

            ##--- CONTROLE DE VOLUME
            elif 277 <= mouse_pos[0] <= 333 and 485 <= mouse_pos[1] <= 508:
                if 0 <= Objetos.volume <= 100:
                    for event in pygame.event.get(): 
                        if event.type == MOUSEBUTTONDOWN:                        
                            if event.button == 4 and Objetos.volume != 100:
                                Objetos.volume += 5
                                Objetos.sndMoeda.set_volume(Objetos.volume/100.0)
                                Objetos.sndTema.set_volume(Objetos.volume/100.0)
                            elif event.button == 4 and Objetos.volume == 100:
                                Objetos.sndMoeda.play()
                            if event.button == 5 and Objetos.volume != 0:
                                Objetos.volume -= 5
                                Objetos.sndMoeda.set_volume(Objetos.volume/100.0)
                                Objetos.sndTema.set_volume(Objetos.volume/100.0)
                            elif event.button == 5 and Objetos.volume == 0:
                                Objetos.sndMoeda.play()
                
                this.volumeNum = Objetos.fonteHoliday.render(str(Objetos.volume), True, (255,0,0))
                if 0 <= Objetos.volume <= 100:
                    if mouse_press[0] and Objetos.volume != 100:
                        Objetos.volume += 1
                        Objetos.sndMoeda.set_volume(Objetos.volume/100.0)
                        Objetos.sndTema.set_volume(Objetos.volume/100.0)
                    elif mouse_press[0] and Objetos.volume == 100:
                        Objetos.sndMoeda.play()
                    if mouse_press[2] and Objetos.volume != 0:
                        Objetos.volume -= 1
                        Objetos.sndMoeda.set_volume(Objetos.volume/100.0)
                        Objetos.sndTema.set_volume(Objetos.volume/100.0)
                    elif mouse_press[2] and Objetos.volume == 0:
                        Objetos.sndMoeda.play()

            ##--- POSICOES
            elif 223 <= mouse_pos[0] <= 385 and 553 <= mouse_pos[1] <= 578:
                this.posicoes = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][9], True, (255,0,0))
                if mouse_press[0]:
                    dados  = []
                    try:
                        ler = open("data" + os.sep + "rank.dat", "r")
                        lerDados = ler.readlines()
                        ler.close()
                        for dado in lerDados:
                            dados.append(dado.strip())
                    except:
                        arq = open("data" + os.sep + "rank.dat", "w")
                        arq.close()
                        this.mensagem = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][6][1], True, (255,0,0))
                        Objetos.background.blit(this.mensagem, (200, 200))
                    while True:

                        mouse_pos = pygame.mouse.get_pos()
                        mouse_press = pygame.mouse.get_pressed()

                        for event in pygame.event.get(): 
                            if event.type == QUIT: 
                                pygame.quit()
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    Objetos.opcoes.run()
                        Objetos.background.blit(Objetos.fundoOpcoes, (0,0))
                        Objetos.background.blit(Objetos.papiro2, (4, 40))
                        
                        voltar = Objetos.fonteHoliday.render("...", True, (0,0,0))
                        if 545 <= mouse_pos[0] <= 585 and 614 <= mouse_pos[1] <= 633:
                            voltar = Objetos.fonteHoliday.render("...", True, (255,0,0))
                            for event in pygame.event.get(): 
                                if event.type == MOUSEBUTTONDOWN:
                                    if event.button == 1:
                                        Objetos.opcoes.run()                        
                        Objetos.background.blit(voltar, (550, 600))
                        
                        i=0
                        for dado in dados:
                            mensagem = Objetos.fonteHoliday.render("%-10s"%(dado.split("|")[0])+" : "+dado.split("|")[1], True, (0,0,0))
                            Objetos.background.blit(mensagem, (100, 150+i))
                            i+=40
                        this.posicoes = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][6][0], True, (255,255,255))
                        Objetos.background.blit(this.posicoes, (220,30))
                        pygame.display.update()

            ##--- BOTAO VOLTAR
            this.voltar = Objetos.fonteHoliday.render("...", True, (0,0,0))

            if 545 <= mouse_pos[0] <= 585 and 614 <= mouse_pos[1] <= 633:
                this.voltar = Objetos.fonteHoliday.render("...", True, (255,0,0))
                for event in pygame.event.get(): 
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            Objetos.menu.run()

            Objetos.background.blit(Objetos.fundoOpcoes, (0,0))
            Objetos.background.blit(Objetos.papiro2, (4, 40))
            Objetos.background.blit(this.voltar, (550, 600))
            Objetos.background.blit(this.texto, (240, 30))
            Objetos.background.blit(this.modoTela,(170, 130))
            Objetos.background.blit(this.fullscreen,(10, 180))
            Objetos.background.blit(this.modoNormal,(325, 180))
            Objetos.background.blit(this.idioma,(240, 280))
            Objetos.background.blit(this.portugues,(70,330))
            Objetos.background.blit(this.ingles,(270,330))
            Objetos.background.blit(this.espanhol,(410,330))
            Objetos.background.blit(this.volume,(240,430))
            Objetos.background.blit(this.volumeNum, (280,480))
            Objetos.background.blit(this.posicoes, (225,550))
            
            pygame.display.update()

