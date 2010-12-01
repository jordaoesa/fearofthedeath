import pygame
from pygame.locals import *
import Objetos
import Funcoes

class Principal:
    
    def run(this):
        Objetos.sndTema.stop()
        
        while True: 

            Funcoes.verificaTeclas()
            if Objetos.jogo.modo == 1: ##-- MODO DE JOGO NORMAL
                
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

            elif Objetos.jogo.modo == 2: ##-- REINICIO APOS PERDA DE VIDA
                
                if Objetos.jogo.vidas == 0:
                    while Objetos.jogo.tempoModo <= 400:
                        Objetos.jogo.tempoModo += 1
                        mensagem = Objetos.fonteHoliday.render("Perdeu Manolo", True, (255,0,0))
                        Objetos.background.blit(mensagem, (180, 320))
                        pygame.display.update()
                        Objetos.fps.tick(60)
                    Objetos.jogo.tempoModo = 0
                    Objetos.grava.gravarScore()
                    #Objetos.grava.clearUser()
                    Objetos.menu.__init__()
                    Objetos.menu.run()
                        
                while Objetos.jogo.tempoModo <= 400:
                    Objetos.jogo.tempoModo += 1
                    mensagem = Objetos.fonteHoliday.render("Carregando...", True, (255,0,0))
                    Objetos.background.blit(mensagem, (180, 320))
                    pygame.display.update()
                    Objetos.fps.tick(60)

                Objetos.jogo.tempoModo = 0
                Objetos.sonic.tempoEscudo = 0
                Objetos.jogo.vidas -= 1
                Objetos.nivel.reiniciar()
                Objetos.jogo.setModo(1)

            elif Objetos.jogo.modo == 3: ##-- INICIO DA PROXIMA FASE
                    
                if Objetos.jogo.getNivel() == 3:

                    Objetos.jogo.tempoModo = 0                    
                    Objetos.grava.gravarScore()
                    #Objetos.grava.clearUser()
                    
                    while Objetos.jogo.tempoModo <= 500:
                        Objetos.jogo.tempoModo += 1
                        venceu = Objetos.fonteHoliday.render("VOCE VENCEU", True, (0,0,0))
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
                    Objetos.menu.run()
                        
                while Objetos.jogo.tempoModo <= 400:
                    Objetos.jogo.tempoModo += 1
                    mensagem = Objetos.fonteHoliday.render("Carregando...", True, (255,0,0))
                    Objetos.background.blit(mensagem, (180, 320))
                    pygame.display.update()
                    Objetos.fps.tick(60)
                    
                Objetos.nivel.reiniciar()
                Objetos.sonic.tempoEscudo = 0
                Objetos.jogo.tempoModo = 0
                Objetos.jogo.proximoNivel()

            Objetos.background.fill((200, 200, 200))

            ####BLITA MAPA E sonic NA TELA
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
