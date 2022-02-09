import pygame, sys

sys.path.append('../')
from settings import *
from level1 import Level1
from level2 import Level2
from level3 import Level3
from level4 import Level4

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pyguins Adventure')
clock = pygame.time.Clock()

lvl = 1
nb = 1

etape=0


first = True

Pred = False

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


programIcon = pygame.image.load('./images/icon/icon.png')


while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if etape==0:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 50)
        draw_text('Pygwin Adventure', font, (255, 255, 255), screen, 400, 20)
        font = pygame.font.SysFont(None, 20)
        mx, my = pygame.mouse.get_pos()
        Pred=False

        buttonC_1 = pygame.Rect(400, 100, 300, 50)
        if buttonC_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                etape= 1
        pygame.draw.rect(screen, (255, 0, 0), buttonC_1)
        draw_text('Jouer', font, (255, 255, 255), screen, 500, 120)

        buttonC_2 = pygame.Rect(400, 200, 300, 50)
        if buttonC_2.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                etape = 9
        pygame.draw.rect(screen, (255, 0, 0), buttonC_2)
        draw_text('Regles du Jeu', font, (255, 255, 255), screen, 500, 200)

        buttonC_3 = pygame.Rect(800, 600, 100, 50)
        if buttonC_3.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                etape = 10
        pygame.draw.rect(screen, (255, 0, 0), buttonC_3)
        draw_text('Credits', font, (255, 255, 255), screen,800, 600)

        buttonC_4 = pygame.Rect(800, 670, 100, 50)
        if buttonC_4.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (255, 0, 0), buttonC_4)
        draw_text('Quitter', font, (255, 255, 255), screen, 800, 670)

    if etape==1:
        screen.fill((0, 0, 0))
        draw_text('NB JOUEURS', font, (255, 255, 255), screen, 400, 20)
        mx, my = pygame.mouse.get_pos()

        buttonNB_1 = pygame.Rect(250, 100, 200, 50)
        if buttonNB_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                nb = 1
                etape = 2
        pygame.draw.rect(screen, (255, 0, 0), buttonNB_1)
        draw_text('1', font, (255, 255, 255), screen, 270, 120)

        buttonNB_2 = pygame.Rect(250, 200, 200, 50)
        if buttonNB_2.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                nb = 2
                etape = 2
        pygame.draw.rect(screen, (255, 0, 0), buttonNB_2)
        draw_text('2', font, (255, 255, 255), screen, 270, 220)

        buttonNB_3 = pygame.Rect(250, 300, 200, 50)
        if buttonNB_3.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                nb = 3
                etape = 2
        pygame.draw.rect(screen, (255, 0, 0), buttonNB_3)
        draw_text('3', font, (255, 255, 255), screen, 270, 320)

        buttonNB_4 = pygame.Rect(250, 400, 200, 50)
        if buttonNB_4.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                nb = 4
                etape = 2
        pygame.draw.rect(screen, (255, 0, 0), buttonNB_4)
        draw_text('4', font, (255, 255, 255), screen, 270, 420)

        buttonT_1 = pygame.Rect(50, 50, 100, 50)
        if buttonT_1.collidepoint((mx, my)):
            if Pred and pygame.mouse.get_pressed()[0]:
                etape = 0
        pygame.draw.rect(screen, (255, 0, 0), buttonT_1)
        draw_text('Retour', font, (255, 255, 255), screen, 60, 60)
        Pred = False

    if etape==2:
        screen.fill((0, 0, 0))
        draw_text('NIVEAU', font, (255, 255, 255), screen, 520, 20)
        mx, my = pygame.mouse.get_pos()
        buttonLVL_1 = pygame.Rect(150, 150, 150, 150)
        pygame.draw.rect(screen, (255, 0, 0), buttonLVL_1)
        draw_text('1', font, (255, 255, 255), screen, 200, 200)

        buttonLVL_2 = pygame.Rect(350, 150, 150, 150)
        pygame.draw.rect(screen, (255, 0, 0), buttonLVL_2)
        draw_text('2', font, (255, 255, 255), screen, 400, 200)

        buttonLVL_3 = pygame.Rect(550, 150, 150, 150)
        pygame.draw.rect(screen, (255, 0, 0), buttonLVL_3)
        draw_text('3', font, (255, 255, 255), screen, 600, 200)

        buttonF_1 = pygame.Rect(50, 50, 100, 50)
        if buttonF_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                etape = 1
        pygame.draw.rect(screen, (255, 0, 0), buttonF_1)
        draw_text('Retour', font, (255, 255, 255), screen, 60, 60)

        if buttonLVL_1.collidepoint((mx, my)):
            if Pred and pygame.mouse.get_pressed()[0]:
                print("etape 2")
                etape = 3
                lvl=1
        if buttonLVL_2.collidepoint((mx, my)):
            if Pred and pygame.mouse.get_pressed()[0]:
                print("etape 2")
                etape = 3
                lvl=2
        if buttonLVL_3.collidepoint((mx, my)):
            if Pred and pygame.mouse.get_pressed()[0]:
                print("etape 2")
                etape = 3
                lvl=3
        Pred = False

    if etape == 3:
        screen.fill(BG_COLOR)
        if first:
            if nb == 1:
                level = Level1(lvl - 1, nb - 1)
            elif nb == 2:
                level = Level2(lvl - 1, nb - 1)
            elif nb == 3:
                level = Level3(lvl - 1, nb - 1)
            elif nb == 4:
                level = Level4(lvl - 1, nb - 1)
            first = False
        level.run()

    if etape == 9:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 50)
        draw_text('Regles du Jeu', font, (255, 255, 255), screen, 400, 20)
        font = pygame.font.SysFont(None, 20)
        draw_text('Le but est de ....', font, (255, 255, 255), screen, 300, 100)
        mx, my = pygame.mouse.get_pos()
        Pred = False

        buttonR_1 = pygame.Rect(50, 50, 100, 50)
        if buttonR_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                etape = 0
        pygame.draw.rect(screen, (255, 0, 0), buttonR_1)
        draw_text('Retour', font, (255, 255, 255), screen, 60, 60)

    if etape==10:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 50)
        draw_text('Credits', font, (255, 255, 255), screen, 400, 20)
        font = pygame.font.SysFont(None, 20)
        draw_text('Réalisé grace à ...', font, (255, 255, 255), screen, 300, 100)
        mx, my = pygame.mouse.get_pos()
        Pred=False

        buttonS_1 = pygame.Rect(50, 50, 100, 50)
        if buttonS_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                etape = 0
        pygame.draw.rect(screen, (255, 0, 0), buttonS_1)
        draw_text('Retour', font, (255, 255, 255), screen, 60, 60)

    if not pygame.mouse.get_pressed()[0]:
        Pred=True
    else:
        Pred=False

    # drawing logic
    pygame.display.update()
    clock.tick(60)

