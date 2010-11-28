import pygame
from pygame.locals import *
import os
import Objetos

class NomeUser:

    def __init__(this):
        this.user = ""
        this.image = pygame.image

    def clearUser(this):
        this.user = ""

    def gravarScore(this):

        dados  = []
        
        try:
            ler = open("data" + os.sep + "rank.dat", "r")
            lerDados = ler.readlines()
            ler.close()
            for dado in lerDados:
                dados.append(dado.strip())
        except:
            criar = open("data" + os.sep + "rank.dat", "w")
            
        try:
            if not this.user + "|" + str(Objetos.jogo.getScore()) in dados:
                
                gravar = open("data" + os.sep + "rank.dat", "a")
                gravar.write(this.user + "|" + str(Objetos.jogo.getScore()) + "\n")
                gravar.close()
                this.clearUser()
                print "gravado com sucesso"
        except:
            pass

    def screenName(this):
        
        if Objetos.escolha.player == "shadow":
            this.image = Objetos.fundoShadow
        elif Objetos.escolha.player == "knuckles":
            this.image = Objetos.fundoKnuckles
        elif Objetos.escolha.player == "sonic":
            this.image = Objetos.fundoSonic

        while True:

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                    
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        this.clearUser()
                        Objetos.escolha.selectPlayer()
                    elif event.key == K_KP_ENTER:
                        if len(this.user.strip().split()) > 0:
                            return this.user
                    elif event.key == K_RETURN:
                        if len(this.user.strip().split()) > 0:
                            return this.user
                    elif event.key == K_BACKSPACE: this.user = this.user[:-1]
                    
                    if len(this.user) < 10:
                        if event.key == K_SPACE: this.user += " "
                        elif event.key == K_COMMA: this.user += ","
                        elif event.key == K_MINUS: this.user += "-"
                        elif event.key == K_PERIOD: this.user += "."
                        elif event.key == K_0: this.user += "0"
                        elif event.key == K_1: this.user += "1"
                        elif event.key == K_2: this.user += "2"
                        elif event.key == K_3: this.user += "3"
                        elif event.key == K_4: this.user += "4"
                        elif event.key == K_5: this.user += "5"
                        elif event.key == K_6: this.user += "6"
                        elif event.key == K_7: this.user += "7"
                        elif event.key == K_8: this.user += "8"
                        elif event.key == K_9: this.user += "9"
                        elif event.key == K_EQUALS: this.user += "="
                        elif event.key == K_BACKQUOTE: this.user += "'"
                        elif event.key == K_a: this.user += "a"
                        elif event.key == K_b: this.user += "b"
                        elif event.key == K_c: this.user += "c"
                        elif event.key == K_d: this.user += "d"
                        elif event.key == K_e: this.user += "e"
                        elif event.key == K_f: this.user += "f"
                        elif event.key == K_g: this.user += "g"
                        elif event.key == K_h: this.user += "h"
                        elif event.key == K_i: this.user += "i"
                        elif event.key == K_j: this.user += "j"
                        elif event.key == K_k: this.user += "k"
                        elif event.key == K_l: this.user += "l"
                        elif event.key == K_m: this.user += "m"
                        elif event.key == K_n: this.user += "n"
                        elif event.key == K_o: this.user += "o"
                        elif event.key == K_p: this.user += "p"
                        elif event.key == K_q: this.user += "q"
                        elif event.key == K_r: this.user += "r"
                        elif event.key == K_s: this.user += "s"
                        elif event.key == K_t: this.user += "t"
                        elif event.key == K_u: this.user += "u"
                        elif event.key == K_v: this.user += "v"
                        elif event.key == K_w: this.user += "w"
                        elif event.key == K_x: this.user += "x"
                        elif event.key == K_y: this.user += "y"
                        elif event.key == K_z: this.user += "z"
                        elif event.key == K_KP0: this.user += "0"
                        elif event.key == K_KP1: this.user += "1"
                        elif event.key == K_KP2: this.user += "2"
                        elif event.key == K_KP3: this.user += "3"
                        elif event.key == K_KP4: this.user += "4"
                        elif event.key == K_KP5: this.user += "5"
                        elif event.key == K_KP6: this.user += "6"
                        elif event.key == K_KP7: this.user += "7"
                        elif event.key == K_KP8: this.user += "8"
                        elif event.key == K_KP9: this.user += "9"
                        elif event.key == K_KP_PERIOD: this.user += "."
                        elif event.key == K_KP_DIVIDE: this.user += "/"
                        elif event.key == K_KP_MULTIPLY: this.user += "*"
                        elif event.key == K_KP_MINUS: this.user += "-"
                        elif event.key == K_KP_PLUS: this.user += "+"
                        elif event.key == K_KP_EQUALS: this.user += "="

            this.texto = Objetos.fonteHoliday.render("DIGITE SEU NOME", True, (0,0,0))
            this.nome = Objetos.fonteHoliday.render(this.user, True, (0,0,0))

            Objetos.background.blit(this.image, (0,0))
            Objetos.background.blit(Objetos.tarjaNome, (150,100))
            Objetos.background.blit(Objetos.tarjaNome, (150,130))
            Objetos.background.blit(this.texto, (153,99))
            Objetos.background.blit(this.nome, (183, 128))
            pygame.display.update()
