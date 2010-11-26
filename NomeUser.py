import pygame
from pygame.locals import *
import os
import Objetos

class NomeUser:

    def __init__(this):
        this.user   = ""

    def gravarHiscore(this):

        dados  = []
        
        try:
            ler = open("data" + os.sep + "hiscore.txt", "r")
            #print "passou do ler dados"
            lerDados = ler.readlines()
            ler.close()
            for dado in lerDados:
                dados.append(dado.strip())
        except:
            criar = open("data" + os.sep + "hiscore.txt", "w")
            #print "entrou no except e crou o arquivo"
        try:
            if not this.user + " " + str(jogo.score) in dados:
                
                gravar = open("data" + os.sep + "hiscore.txt", "a")
                gravar.write(this.user + " " + str(jogo.score) + "\n")
                gravar.close()
                print "gravou a bagaca"
        except:
            pass

    def screenName(this):

        while True:

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                    
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE: pygame.quit()
                    if event.key == K_KP_ENTER:
                        this.gravarHiscore()
                        return this.user
                    if event.key == K_RETURN:
                        this.gravarHiscore()
                        return this.user
                    if event.key == K_BACKSPACE: this.user = this.user[:-1]
                    if event.key == K_SPACE: this.user += " "
                    if event.key == K_EXCLAIM: this.user += "!"
                    if event.key == K_QUOTEDBL: this.user += "\""
                    if event.key == K_HASH: this.user += "#"
                    if event.key == K_DOLLAR: this.user += " "
                    if event.key == K_AMPERSAND: this.user += "&"
                    if event.key == K_LEFTPAREN: this.user += "("
                    if event.key == K_RIGHTPAREN: this.user += ")"
                    if event.key == K_ASTERISK: this.user += "*"
                    if event.key == K_PLUS: this.user += "+"
                    if event.key == K_COMMA: this.user += ","
                    if event.key == K_MINUS: this.user += "-"
                    if event.key == K_PERIOD: this.user += "."
                    if event.key == K_SLASH: this.user += "/"
                    if event.key == K_0: this.user += "0"
                    if event.key == K_1: this.user += "1"
                    if event.key == K_2: this.user += "2"
                    if event.key == K_3: this.user += "3"
                    if event.key == K_4: this.user += "4"
                    if event.key == K_5: this.user += "5"
                    if event.key == K_6: this.user += "6"
                    if event.key == K_7: this.user += "7"
                    if event.key == K_8: this.user += "8"
                    if event.key == K_9: this.user += "9"
                    if event.key == K_COLON: this.user += ":"
                    if event.key == K_SEMICOLON: this.user += ";"
                    if event.key == K_LESS: this.user += "<"
                    if event.key == K_EQUALS: this.user += "="
                    if event.key == K_GREATER: this.user += ">"
                    if event.key == K_QUESTION: this.user += "?"
                    if event.key == K_AT: this.user += "@"
                    if event.key == K_LEFTBRACKET: this.user += "["
                    if event.key == K_BACKSLASH: this.user += "\\"
                    if event.key == K_RIGHTBRACKET: this.user += "]"
                    if event.key == K_UNDERSCORE: this.user += "_"
                    if event.key == K_BACKQUOTE: this.user += "'"
                    if event.key == K_a: this.user += "A"
                    if event.key == K_b: this.user += "B"
                    if event.key == K_c: this.user += "C"
                    if event.key == K_d: this.user += "D"
                    if event.key == K_e: this.user += "E"
                    if event.key == K_f: this.user += "F"
                    if event.key == K_g: this.user += "G"
                    if event.key == K_h: this.user += "H"
                    if event.key == K_i: this.user += "I"
                    if event.key == K_j: this.user += "J"
                    if event.key == K_k: this.user += "K"
                    if event.key == K_l: this.user += "L"
                    if event.key == K_m: this.user += "M"
                    if event.key == K_n: this.user += "N"
                    if event.key == K_o: this.user += "O"
                    if event.key == K_p: this.user += "P"
                    if event.key == K_q: this.user += "Q"
                    if event.key == K_r: this.user += "R"
                    if event.key == K_s: this.user += "S"
                    if event.key == K_t: this.user += "T"
                    if event.key == K_u: this.user += "U"
                    if event.key == K_v: this.user += "V"
                    if event.key == K_w: this.user += "W"
                    if event.key == K_x: this.user += "X"
                    if event.key == K_y: this.user += "Y"
                    if event.key == K_z: this.user += "Z"
                    if event.key == K_KP0: this.user += "0"
                    if event.key == K_KP1: this.user += "1"
                    if event.key == K_KP2: this.user += "2"
                    if event.key == K_KP3: this.user += "3"
                    if event.key == K_KP4: this.user += "4"
                    if event.key == K_KP5: this.user += "5"
                    if event.key == K_KP6: this.user += "6"
                    if event.key == K_KP7: this.user += "7"
                    if event.key == K_KP8: this.user += "8"
                    if event.key == K_KP9: this.user += "9"
                    if event.key == K_KP_PERIOD: this.user += "."
                    if event.key == K_KP_DIVIDE: this.user += "/"
                    if event.key == K_KP_MULTIPLY: this.user += "*"
                    if event.key == K_KP_MINUS: this.user += "-"
                    if event.key == K_KP_PLUS: this.user += "+"
                    if event.key == K_KP_EQUALS: this.user += "="

            this.texto = Objetos.fonteNome.render("DIGITE SEU NOME", True, (0,0,0))
            this.nome = Objetos.fonteNome.render(this.user, True, (0,0,0))

            Objetos.background.fill((255,255,255))
            Objetos.background.blit(this.texto, (100,300))
            Objetos.background.blit(this.nome, (100, 350))
            pygame.display.update()
