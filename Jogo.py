import pygame
import Objetos

class Jogo:

    def __init__ (this):
        this.nivel        = 1
        this.score        = 0
        this.vidas        = 3
        this.modo         = 0
        this.tempoModo    = 0
        this.setModo(4)
        this.qtdTilesTela = (21, 19)
        this.tamanhoTela = (this.qtdTilesTela[1] * 32, this.qtdTilesTela[0] * 32)

    def pontos(this, pontos):
        this.score += pontos

    def getScore(this):
        return this.score
        
    def printPontuacao(this):
        this.texto = Objetos.fonteHoliday20.render(Objetos.idiomas[Objetos.idioma][8][0]+str(this.score), True, (255,255,255))
        Objetos.background.blit(this.texto, (130,0))

    def printVidas(this):
        this.texto = Objetos.fonteHoliday20.render(Objetos.idiomas[Objetos.idioma][8][1] + ("*"*this.vidas), True, (255,255,255))
        Objetos.background.blit(this.texto, (5,0))

    def printTurbo(this):
        this.turbo = Objetos.fonteHoliday20.render(Objetos.idiomas[Objetos.idioma][8][2], True, (255,255,255))
        Objetos.background.blit(this.turbo, (325,0))
        if Objetos.sonic.limiteEscudo > 0:
            Objetos.background.blit(Objetos.turbo[18], (400,0))
        
    def novoJogo(this):
        this.nivel = 1
        this.score = 0
        this.vidas = 3
        this.setModo(1)
        Objetos.nivel.loadNivel(1)
        
    def getNivel(this):
        return this.nivel
        
    def proximoNivel(this):
        this.nivel += 1
        this.setModo(1)
        Objetos.nivel.loadNivel(Objetos.jogo.getNivel())
        Objetos.sonic.velX = 0
        Objetos.sonic.velY = 0
        Objetos.sonic.images = Objetos.imgPlayer["playerD"]
        
    def setModo (this, newMode):
        this.modo = newMode
        this.tempoModo = 0
