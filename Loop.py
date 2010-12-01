import pygame
from pygame.locals import *
import random
import Objetos
import Funcoes

class Principal:

##    def __init__(this):
##        this.playMusicas()

    def playMusicas(this):
        this.i = random.randint(1,6)
        Objetos.musicas[this.i].play(-1)
        
    def stopMusicas(this):
        for i in range(1,7):
            Objetos.musicas[i].stop()
        
    def run(this):
        Objetos.musicas[0].stop()
        this.playMusicas()
        while True:
            
            Funcoes.verificaTeclas()
            ##--- MODO DE JOGO NORMAL
            if Objetos.jogo.modo == 1:
                
                if Objetos.sonic.limiteEscudo > 0:
                    Objetos.sonic.tempoEscudo += 1

                Funcoes.verificaTeclas()

                Objetos.fantasma.colisao()
                Objetos.fantasma1.colisao()
                Objetos.fantasma2.colisao()
                Objetos.fantasma3.colisao()
                
                Objetos.sonic.andar()
                Objetos.fantasma.andar()
                Objetos.fantasma1.andar()
                Objetos.fantasma2.andar()
                Objetos.fantasma3.andar()

                Objetos.nivel.portaisF((Objetos.fantasma.x, Objetos.fantasma.y), (Objetos.fantasma.proxLinha, Objetos.fantasma.proxColuna), Objetos.fantasma)
                Objetos.nivel.portaisF((Objetos.fantasma1.x, Objetos.fantasma1.y), (Objetos.fantasma1.proxLinha, Objetos.fantasma1.proxColuna), Objetos.fantasma1)
                Objetos.nivel.portaisF((Objetos.fantasma2.x, Objetos.fantasma2.y), (Objetos.fantasma2.proxLinha, Objetos.fantasma2.proxColuna), Objetos.fantasma2)
                Objetos.nivel.portaisF((Objetos.fantasma3.x, Objetos.fantasma3.y), (Objetos.fantasma3.proxLinha, Objetos.fantasma3.proxColuna), Objetos.fantasma3)

            ##--- REINICIO APOS PERDA DE VIDA
            elif Objetos.jogo.modo == 2:
                
                if Objetos.jogo.vidas == 1:
                    while Objetos.jogo.tempoModo <= 500:
                        Objetos.jogo.tempoModo += 1
                        mensagem = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][7][2], True, (255,0,0))
                        Objetos.background.blit(mensagem, (180, 320))
                        pygame.display.update()
                        Objetos.fps.tick(60)
                    this.stopMusicas()
                    Objetos.jogo.tempoModo = 0
                    Objetos.grava.gravarScore()
                    Objetos.menu.__init__()
                    Objetos.menu.run()
                        
                while Objetos.jogo.tempoModo <= 300:
                    Objetos.jogo.tempoModo += 1
                    mensagem = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][7][0], True, (255,0,0))
                    Objetos.background.blit(mensagem, (180, 320))
                    pygame.display.update()
                    Objetos.fps.tick(60)

                Objetos.jogo.tempoModo = 0
                Objetos.sonic.tempoEscudo = 0
                Objetos.jogo.vidas -= 1
                Objetos.nivel.reiniciar()
                Objetos.jogo.setModo(1)

            ##--- INICIO DA PROXIMA FASE
            elif Objetos.jogo.modo == 3:
                    
                if Objetos.jogo.getNivel() == 3:

                    Objetos.jogo.tempoModo = 0                    
                    Objetos.grava.gravarScore()
                    
                    while Objetos.jogo.tempoModo <= 500:
                        Objetos.jogo.tempoModo += 1
                        venceu = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][7][1], True, (0,0,0))
                        Objetos.background.blit(venceu, (200, 320))

                        for event in pygame.event.get(): 
                            if event.type == QUIT: 
                                pygame.quit()
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    Objetos.menu.run()
                                elif event.key == K_RETURN:
                                    Objetos.menu.__init__()
                                    Objetos.menu.run()
                                    
                        pygame.display.update()
                        Objetos.fps.tick(60)
                    this.stopMusicas()
                    Objetos.menu.run()
                        
                while Objetos.jogo.tempoModo <= 300:
                    Objetos.jogo.tempoModo += 1
                    mensagem = Objetos.fonteHoliday.render(Objetos.idiomas[Objetos.idioma][7][0], True, (255,0,0))
                    Objetos.background.blit(mensagem, (180, 320))
                    pygame.display.update()
                    Objetos.fps.tick(60)
                    
                Objetos.nivel.reiniciar()
                Objetos.sonic.tempoEscudo = 0
                Objetos.jogo.tempoModo = 0
                Objetos.jogo.proximoNivel()

            Objetos.background.fill((200, 200, 200))
            Objetos.nivel.printMapa()
            Objetos.sonic.printSonic()

            Objetos.fantasma.printFantasma()
            Objetos.fantasma1.printFantasma()
            Objetos.fantasma2.printFantasma()
            Objetos.fantasma3.printFantasma()
            
            Objetos.jogo.printVidas()
            Objetos.jogo.printPontuacao()
            Objetos.jogo.printTurbo()

            pygame.display.update()
            Objetos.fps.tick (60)
