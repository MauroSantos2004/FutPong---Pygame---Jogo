import pygame

pygame.init()

tela = pygame.display.set_mode([1280, 720])
titulo = pygame.display.set_caption("Futeball Pong")

vencedor = pygame.image.load("Placar/win.png")

ponto1 = 0
ponto1_img = pygame.image.load("score/0.png")
ponto2 = 0
ponto2_img = pygame.image.load("score/0.png")

campo = pygame.image.load("assets/field.png")

jogador1 = pygame.image.load("assets/player1.png")
jogador1_y = 310
jogador1_moveup = False
jogador1_movedown = False

jogador2 = pygame.image.load("assets/player2.png")
jogador2_y = 310
jogador2_moveup = False
jogador2_movedown = False


bola = pygame.image.load("assets/ball.png")
bola_x = 617
bola_y = 337
bola_dir = -25
bola_dir_y = 10


def mover_jogador1():
    global jogador1_y

    if jogador1_moveup:
        jogador1_y -= 20
    else:
        jogador1_y += 0

    if jogador1_movedown:
        jogador1_y += 20
    else:
        jogador1_y += 0

    if jogador1_y <= 0:
        jogador1_y = 0
    elif jogador1_y >= 530:
        jogador1_y = 530

def mover_jogador2():
    global jogador2_y

    if jogador2_moveup:
        jogador2_y -= 20
    else:
        jogador2_y += 0

    if jogador1_movedown:
        jogador2_y += 20
    else:
        jogador2_y += 0

    if jogador2_y <= 0:
        jogador2_y = 0
    elif jogador2_y >= 530:
        jogador2_y = 530

def mover_bola():
    global bola_x
    global bola_y
    global bola_dir
    global bola_dir_y
    global ponto1
    global ponto2
    global ponto1_img
    global ponto2_img

    bola_x += bola_dir
    bola_y += bola_dir_y

    if bola_x < 120:
        if jogador1_y < bola_y + 23:
            if jogador1_y + 146 > bola_y:
                bola_dir *= -1

    if bola_x > 1100:
        if jogador2_y < bola_y + 23:
            if jogador2_y + 146 > bola_y:
                bola_dir *= -1

    if bola_y > 640:
        bola_dir_y *= -1
    elif bola_y <= 0:
        bola_dir_y *= -1

    if bola_x < -50:
        bola_x = 617
        bola_y = 337
        bola_dir_y *= -1
        bola_dir *= -1
        ponto2 += 1
        ponto2_img = pygame.image.load("score/" + str(ponto2) + ".png")

    elif bola_x > 1320:
        bola_x = 617
        bola_y = 337
        bola_dir_y *= -1
        bola_dir *= -1
        ponto1 += 1
        ponto1_img = pygame.image.load("score/" + str(ponto1) + ".png")


def desenho():
    if ponto1 or ponto2 < 9:
        tela.blit(campo, (0, 0))
        tela.blit(jogador1, (50, jogador1_y))
        tela.blit(jogador2, (1150, jogador2_y))
        tela.blit(bola, (bola_x, bola_y))
        tela.blit(ponto1_img, (500, 50))
        tela.blit(ponto2_img, (710, 50))
        mover_bola()
        mover_jogador1()
        mover_jogador2()
    else:
        tela.blit(vencedor, (300, 330))


jogando = True
while jogando:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            jogando = False
        # Movimento do jogador 1
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                jogador1_moveup = True
            if events.key == pygame.K_s:
                jogador1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                jogador1_moveup = False
            if events.key == pygame.K_s:
                jogador1_movedown = False
        # movimento do jogador 2
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                jogador2_moveup = True
            if events.key == pygame.K_DOWN:
                jogador2_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_UP:
                jogador2_moveup = False
            if events.key == pygame.K_DOWN:
                jogador2_movedown = False
    desenho()
    pygame.display.update()