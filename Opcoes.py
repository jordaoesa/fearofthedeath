import pygame, os
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
            
            this.texto = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][0],True, (139, 0, 0))

            this.modoTela = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][1], True, (139, 0, 0))
            this.fullscreen = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][2], True, (0, 255, 0))
            this.modoNormal = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][3], True, (255, 255, 0))

            this.idioma = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][4], True, (79, 79, 79))
            this.portugues = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][5], True, (255, 255, 255))
            this.ingles = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][6], True, (169, 169, 169))
            this.espanhol = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][7], True, (139, 0, 0))

            this.volume = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][8], True, (130, 130, 130))
            this.volumeNum = Objetos.fonteHoliday.render(str(Objetos.volume), True, (169, 169, 169))

            this.posicoes = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][5][9], True, (255, 255, 255))


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
                        this.mensagem = Objetos.fonteHoliday.render("Nao ha Resultados", True, (255,0,0))
                        Objetos.background.blit(this.mensagem, (200, 200))
                    if len(dados) == 0:
                        this.mensagem = Objetos.fonteHoliday.render("Nao ha Resultados", True, (255,0,0))
                        Objetos.background.blit(this.mensagem, (200, 200))
                    else:
                        while True:
                            for event in pygame.event.get(): 
                                if event.type == QUIT: 
                                    pygame.quit()
                                if event.type == KEYDOWN:
                                    if event.key == K_ESCAPE:
                                        Objetos.opcoes.run()
                            Objetos.background.fill((255,255,255))
                            mapaDados = {}
                            i=0
                            for dado in dados:
                                mapaDados[int(dado.split("|")[1])] = dado.split("|")[0]
                            for dado in sorted(mapaDados.items())[::-1]:
                                temp1 = str(dado[0])
                                temp2 = dado[1]
                                while len(temp2) != 10:
                                    temp2+=" "
                                temp3 = Objetos.fonteHoliday.render(temp2+" : "+temp1, True, (255,0,0))
                                Objetos.background.blit(temp3, (100, 200+i))
                                i+=40
                            posicoes = Objetos.fonteHoliday.render("POSICOES", True, (255,0,0))
                            Objetos.background.blit(posicoes, (100,100))
                            pygame.display.update()



                    

                    
##                    dados  = []
##                    try:
##                        ler = open("data" + os.sep + "rank.dat", "r")
##                        lerDados = ler.readlines()
##                        ler.close()
##                        for dado in lerDados:
##                            dados.append(dado.strip())
##                    except:
##                        this.mensagem = Objetos.fonteHoliday.render("Nao ha Resultados", True, (255,0,0))
##                        Objetos.background.blit(this.mensagem, (200, 200))
##                    if len(dados) == 0:
##                        this.mensagem = Objetos.fonteHoliday.render("Nao ha Resultados", True, (255,0,0))
##                        Objetos.background.blit(this.mensagem, (200, 200))
##                    else:
##                        while True:
##                            for event in pygame.event.get(): 
##                                if event.type == QUIT: 
##                                    pygame.quit()
##                                if event.type == KEYDOWN:
##                                    if event.key == K_ESCAPE:
##                                        Objetos.opcoes.run()
##                            Objetos.background.fill((255,255,255))
##                            mapaDados = {}
##                            i=0
##                            for dado in dados:
##                                mapaDados[int(dado.split("|")[1])] = dado.split("|")[0]
##                            for dado in sorted(mapaDados.items())[::-1]:
##                                temp1 = str(dado[0])
##                                temp2 = dado[1]
##                                while len(temp2) != 10:
##                                    temp2+=" "
##                                temp3 = Objetos.fonteHoliday.render(temp2+" : "+temp1, True, (255,0,0))
##                                Objetos.background.blit(temp3, (100, 200+i))
##                                i+=40
##                            posicoes = Objetos.fonteHoliday.render("POSICOES", True, (255,0,0))
##                            Objetos.background.blit(posicoes, (100,100))
##                            pygame.display.update()

            

            Objetos.background.blit(Objetos.fundoOpcoes, (0,0))

            Objetos.background.blit(this.texto, (240, 30))

            Objetos.background.blit(this.modoTela,(170, 130))
            Objetos.background.blit(this.fullscreen,(100, 180))
            Objetos.background.blit(this.modoNormal,(320, 180))
            
            Objetos.background.blit(this.idioma,(240, 280))
            Objetos.background.blit(this.portugues,(70,330))
            Objetos.background.blit(this.ingles,(270,330))
            Objetos.background.blit(this.espanhol,(410,330))

            Objetos.background.blit(this.volume,(240,430))
            Objetos.background.blit(this.volumeNum, (280,480))

            Objetos.background.blit(this.posicoes, (225,550))
            
            

            pygame.display.update()

##    def posicoes(this):
##        
##        this.dados  = []
##        try:
##            ler = open("data" + os.sep + "rank.dat", "r")
##            lerDados = ler.readlines()
##            ler.close()
##            for dado in lerDados:
##                this.dados.append(dado.strip())
##            if len(dados) == 0:
##                this.mensagem = Objetos.fonteHoliday.render("Nao ha Resultados", True, (255,0,0))
##            else:
##                classificacao(dados)
##        except:
##            this.mensagem = Objetos.fonteHoliday.render("Nao ha Resultados", True, (255,0,0))#Objetos.idiomas[Objetos.idioma][5][9]
##            criar = open("data" + os.sep + "rank.dat", "w")
##
##        Objetos.background.blit(this.mensagem, (200, 200))
##
##    def classificacao(this, dados):
##        try:
##            this.mapaDados = {}
##            this.mensagens = []
##            for dado in dados:
##                this.mapaDados[int(dado.split("|")[1])] = dado.split("|")[0]
##            for dado in sorted(mapaDados.items()):
##                temp1 = Objetos.fonteHoliday.render(dado[1]+" : "+dado[0], True, (255,0,0))
####                this.mensagens.append()
##                Objetos.background.blit(temp1, (200, 200))            
##        except:
##            this.mensagem = Objetos.fonteHoliday.render("Nao ha Resultados", True, (255,0,0))#Objetos.idiomas[Objetos.idioma][5][9]
##        Objetos.background.blit(this.mensagem, (200, 200))
            
        

        

