import pygame
import random

# Inicializando o Pygame
pygame.init()

# Dimensões da tela e cores
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

cor_cobra = (0,255,0)
bk_tela = (0, 0, 0)
cor_comida = (255, 0, 0)

# Configurações da cobra
tamanho_cobra = 10
comprimento_cobra = 1
velocidade_cobra = 15
x, y = largura // 2, altura // 2
dx, dy = 0, 0
corpo_cobra = []

# Posição inicial da comida
comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0

# Loop do jogo
relogio = pygame.time.Clock()
jogo_ativo = True
while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                dx, dy = -tamanho_cobra, 0
            elif evento.key == pygame.K_RIGHT:
                dx, dy = tamanho_cobra, 0
            elif evento.key == pygame.K_UP:
                dx, dy = 0, -tamanho_cobra
            elif evento.key == pygame.K_DOWN:
                dx, dy = 0, tamanho_cobra

    # Movimento da cobra
    x += dx
    y += dy
    tela.fill(bk_tela)
    pygame.draw.rect(tela, cor_comida, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])

    # Atualização da posição e do corpo da cobra
    cabeca_cobra = [x, y]
    corpo_cobra.append(cabeca_cobra)
    if len(corpo_cobra) > comprimento_cobra:
        del corpo_cobra[0]
    for bloco in corpo_cobra:
        pygame.draw.rect(tela, cor_cobra, [bloco[0], bloco[1], tamanho_cobra, tamanho_cobra])

    # Verificação de colisão com as bordas e comida
    if x == comida_x and y == comida_y:
        comprimento_cobra += 1
        comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
        comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0
    
    if x <= 0:
        x = largura
    elif x >= largura:
        x = 0
    if y <= 0:
        y = altura
    elif y >= altura:
        y = 0
    if comprimento_cobra >= 10:
        jogo_ativo = False

    pygame.display.update()
    relogio.tick(velocidade_cobra)

pygame.quit()


