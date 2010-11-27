import pygame
import Objetos
import Funcoes

class Principal:
    
    def run(this):
        
        while True: 

            Funcoes.verificaTeclas()
            if Objetos.jogo.modo == 1:

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

            elif Objetos.jogo.modo == 2: ##REINICIO APOS PERDA DE VIDA
                Objetos.jogo.tempoModo += 1
                
                if Objetos.jogo.tempoModo == 100:
                    Objetos.jogo.vidas -= 1
                    Objetos.nivel.reiniciar()
                    Objetos.jogo.setModo(1)
                    if Objetos.jogo.vidas == 0:
                        print "vc perdeu!!"
                        Objetos.grava.gravarScore()
                        Objetos.menu.run()
                for event in pygame.event.get(): 
                    if event.type == QUIT: 
                        pygame.quit()

            elif Objetos.jogo.modo == 3:
                Objetos.jogo.novoJogo()
                Funcoes.verificaTeclas()

            elif Objetos.jogo.modo == 4:

                Objetos.jogo.tempoModo += 1
                if Objetos.jogo.getNivel() == 3:
                    venceu = Objetos.fonteGta1.render("VOCE VENCEU!!", True, (255,0,0))
                    Objetos.background.blit(venceu, (100, 100))
                    if Objetos.jogo.tempoModo == 100:
                        Objetos.jogo.tempoModo = 0                    
                        Objetos.grava.gravarScore()
                        Objetos.menu.run()
                        
                if Objetos.jogo.tempoModo == 100:
                    Objetos.jogo.tempoModo = 0
                    Objetos.jogo.proximoNivel()
                print "aguardando"
##                if Objetos.jogo.getNivel() == 3:
##                    Objetos.grava.gravarScore()
##                    Objetos.menu.run()
##                    venceu = Objetos.fonteGta1.render("VOCE VENCEU!!", True, (255,0,0))
##                    Objetos.background.blit(venceu, (100, 100))
##                Funcoes.verificaTeclas()

            elif Objetos.jogo.modo == 5:
                
                Objetos.nivel.reiniciar()
                Objetos.jogo.vidas = 3
                Objetos.jogo.nivel = 0
                Objetos.nivel.loadNivel(0) ##--- aqui vai ser chamado novamente um menu
                Objetos.grava.user = ""
                Funcoes.verificaTeclas()

            Objetos.background.fill((200, 200, 200))

            ####BLITA MAPA E sonic NA TELA
            Objetos.nivel.printMapa()
            Objetos.sonic.printSonic()

        ##    protect.printColete()
        ##    protect1.printColete()
        ##    protect2.printColete()
        ##    protect3.printColete()

            Objetos.fantasma.printFantasma()
            Objetos.fantasma1.printFantasma()
            Objetos.fantasma2.printFantasma()
            Objetos.fantasma3.printFantasma()
            
            Objetos.jogo.printVidas()
            Objetos.jogo.printPontuacao()
            pygame.display.update()
            print Objetos.jogo.modo
            Objetos.fps.tick (60)
