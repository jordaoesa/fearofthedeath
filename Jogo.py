import pygame
import Objetos

class Jogo:

    def __init__ (this):
        this.nivel        = 1
        this.score        = 0
        this.vidas        = 3
        this.modo         = 0
        this.tempoModo    = 0
        this.posicaoPixel = (0, 0)
        this.proximoTile  = (0, 0)
        this.deslocamento = (0, 0)
        
        this.setModo(4)
                
        this.qtdTilesTela = (21, 19)
        this.tamanhoTela = (this.qtdTilesTela[1] * 32, this.qtdTilesTela[0] * 32)

    def pontos(this, pontos):
        this.score += pontos

    def clearScore(this):
        this.score = 0

    def getScore(this):
        return this.score
        
    def printPontuacao(this):
        this.texto = Objetos.fonteGta1.render("SCORE: ", True, (0,0,255))
        this.pontuacao = Objetos.fonteGta1.render(str(this.score), True, (0,255,0))
        Objetos.background.blit(this.texto, (100,650))
        Objetos.background.blit(this.pontuacao, (165, 650))

    def printVidas(this):
        this.texto = Objetos.fonteGta1.render("VIDAS: " + (str(1)*this.vidas), True, (255,0,0))
        Objetos.background.blit(this.texto, (5,650))
        
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
        Objetos.sonic.images = Objetos.sonicD
        
    def setModo (this, newMode):
        this.modo = newMode
        this.tempoModo = 0
