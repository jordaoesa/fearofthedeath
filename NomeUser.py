import pygame
from pygame.locals import *
import os
import Objetos

class NomeUser:

    def __init__(this):
        this.user   = ""

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

        while True:

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                    
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE: pygame.quit()
                    elif event.key == K_KP_ENTER:
                        if len(this.user.strip().split()) > 0:
                            return this.user
                    elif event.key == K_RETURN:
                        if len(this.user.strip().split()) > 0:
                            return this.user
                    elif event.key == K_BACKSPACE: this.user = this.user[:-1]
                    
                    if len(this.user) <= 10:
                        if event.key == K_SPACE: this.user += " "
                        elif event.key == K_EXCLAIM: this.user += "!"
                        elif event.key == K_QUOTEDBL: this.user += "\""
                        elif event.key == K_HASH: this.user += "#"
                        elif event.key == K_DOLLAR: this.user += " "
                        elif event.key == K_AMPERSAND: this.user += "&"
                        elif event.key == K_LEFTPAREN: this.user += "("
                        elif event.key == K_RIGHTPAREN: this.user += ")"
                        elif event.key == K_ASTERISK: this.user += "*"
                        elif event.key == K_PLUS: this.user += "+"
                        elif event.key == K_COMMA: this.user += ","
                        elif event.key == K_MINUS: this.user += "-"
                        elif event.key == K_PERIOD: this.user += "."
                        elif event.key == K_SLASH: this.user += "/"
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
                        elif event.key == K_COLON: this.user += ":"
                        elif event.key == K_SEMICOLON: this.user += ";"
                        elif event.key == K_LESS: this.user += "<"
                        elif event.key == K_EQUALS: this.user += "="
                        elif event.key == K_GREATER: this.user += ">"
                        elif event.key == K_QUESTION: this.user += "?"
                        elif event.key == K_AT: this.user += "@"
                        elif event.key == K_LEFTBRACKET: this.user += "["
                        elif event.key == K_BACKSLASH: this.user += "\\"
                        elif event.key == K_RIGHTBRACKET: this.user += "]"
                        elif event.key == K_UNDERSCORE: this.user += "_"
                        elif event.key == K_BACKQUOTE: this.user += "'"
                        elif event.key == K_a: this.user += "A"
                        elif event.key == K_b: this.user += "B"
                        elif event.key == K_c: this.user += "C"
                        elif event.key == K_d: this.user += "D"
                        elif event.key == K_e: this.user += "E"
                        elif event.key == K_f: this.user += "F"
                        elif event.key == K_g: this.user += "G"
                        elif event.key == K_h: this.user += "H"
                        elif event.key == K_i: this.user += "I"
                        elif event.key == K_j: this.user += "J"
                        elif event.key == K_k: this.user += "K"
                        elif event.key == K_l: this.user += "L"
                        elif event.key == K_m: this.user += "M"
                        elif event.key == K_n: this.user += "N"
                        elif event.key == K_o: this.user += "O"
                        elif event.key == K_p: this.user += "P"
                        elif event.key == K_q: this.user += "Q"
                        elif event.key == K_r: this.user += "R"
                        elif event.key == K_s: this.user += "S"
                        elif event.key == K_t: this.user += "T"
                        elif event.key == K_u: this.user += "U"
                        elif event.key == K_v: this.user += "V"
                        elif event.key == K_w: this.user += "W"
                        elif event.key == K_x: this.user += "X"
                        elif event.key == K_y: this.user += "Y"
                        elif event.key == K_z: this.user += "Z"
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

            this.texto = Objetos.fonteNome.render("DIGITE SEU NOME", True, (0,0,0))
            this.nome = Objetos.fonteNome.render(this.user, True, (0,0,0))

            Objetos.background.fill((255,255,255))
            Objetos.background.blit(this.texto, (100,300))
            Objetos.background.blit(this.nome, (100, 350))
            pygame.display.update()
