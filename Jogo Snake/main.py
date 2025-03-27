# configurações iniciais

import pygame
import random

pygame.init()
pygame.display.set_caption("Python Snake")
# altere os valores abaixo para ajustar o tamanho do game
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# cores RGB

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (57, 255, 20)
roxa = (128, 0, 128)
amarela = (255, 255, 0)

# parâmetros da snake

tamanho_quadrado = 20
velocidade_jogo = 15


def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) /
                     float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) /
                     float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])


def desenhar_snake(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, roxa, [pixel[0], pixel[1], tamanho, tamanho])


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Calibri", 30)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [1, 1])


def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN and velocidade_y == 0:
        return 0, tamanho_quadrado
    elif tecla == pygame.K_UP and velocidade_y == 0:
        return 0, -tamanho_quadrado
    elif tecla == pygame.K_RIGHT and velocidade_x == 0:
        return tamanho_quadrado, 0
    elif tecla == pygame.K_LEFT and velocidade_x == 0:
        return -tamanho_quadrado, 0
    return velocidade_x, velocidade_y


def desenhar_game_over(pontuacao):
    fonte = pygame.font.SysFont("Calibri", 50)
    texto_game_over = fonte.render("Game Over", True, amarela)
    texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, amarela)

    tela.blit(texto_game_over, [largura / 2 -
              texto_game_over.get_width() / 2, altura / 3])
    tela.blit(texto_pontuacao, [largura / 2 -
              texto_pontuacao.get_width() / 2, altura / 2])


def rodar_jogo():
    fim_Jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_snake = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_Jogo:

        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_Jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(
                    evento.key, velocidade_x, velocidade_y)

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posição da snake

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_Jogo = True

        x += velocidade_x
        y += velocidade_y

        # desenhar_snake
        pixels.append([x, y])
        if len(pixels) > tamanho_snake:
            del pixels[0]

        # se a snake colidiu com ela mesma
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_Jogo = True

        desenhar_snake(tamanho_quadrado, pixels)

        # atualizacao de tela
        pygame.display.update()

        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_snake += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

    desenhar_game_over(tamanho_snake - 1)
    pygame.display.update()
    pygame.time.wait(5000)


rodar_jogo()
