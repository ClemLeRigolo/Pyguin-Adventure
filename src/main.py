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

etape = 1

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

    pygame.display.set_icon(programIcon)
    if etape == 1:
        screen.fill((0, 0, 0))
        draw_text('NB JOUEURS', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        Pred = False

        buttonNB_1 = pygame.Rect(50, 100, 200, 50)
        if buttonNB_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                nb = 1
                etape += 1
        pygame.draw.rect(screen, (255, 0, 0), buttonNB_1)
        draw_text('1', font, (255, 255, 255), screen, 70, 120)

        buttonNB_2 = pygame.Rect(50, 200, 200, 50)
        if buttonNB_2.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                nb = 2
                etape += 1
        pygame.draw.rect(screen, (255, 0, 0), buttonNB_2)
        draw_text('2', font, (255, 255, 255), screen, 70, 220)

        buttonNB_3 = pygame.Rect(50, 300, 200, 50)
        if buttonNB_3.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                nb = 3
                etape += 1
        pygame.draw.rect(screen, (255, 0, 0), buttonNB_3)
        draw_text('3', font, (255, 255, 255), screen, 70, 320)

        buttonNB_4 = pygame.Rect(50, 400, 200, 50)
        if buttonNB_4.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                nb = 4
                etape += 1
        pygame.draw.rect(screen, (255, 0, 0), buttonNB_4)
        draw_text('4', font, (255, 255, 255), screen, 70, 420)

    if etape == 2:
        screen.fill((0, 0, 0))
        draw_text('NIVEAU', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        buttonLVL_1 = pygame.Rect(50, 50, 200, 550)
        pygame.draw.rect(screen, (255, 0, 0), buttonLVL_1)
        draw_text('1', font, (255, 255, 255), screen, 370, 120)

    if etape == 2:
        if buttonLVL_1.collidepoint((mx, my)):
            if Pred and pygame.mouse.get_pressed()[0]:
                print("etape 2")
                etape += 1
                lvl = 1

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

    if not pygame.mouse.get_pressed()[0]:
        Pred = True
    else:
        Pred = False

    # drawing logic
    pygame.display.update()
    clock.tick(60)
