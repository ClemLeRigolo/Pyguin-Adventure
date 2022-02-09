import pygame, sys, button

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

etape = 0

first = True

Pred = False

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


programIcon = pygame.image.load('./images/icon/icon.png')
pygame.display.set_icon(programIcon)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if etape == 0:
        display_surface = pygame.display.get_surface()
        bgn = pygame.image.load("./images/boutons/backgroundAcceuil.png")
        display_surface.blit(bgn.convert_alpha(), (0, 0))
        mx, my = pygame.mouse.get_pos()
        Pred = False

        if 600 > mx > 400 and 420 > my > 350:
            start_img = pygame.image.load('./images/boutons/PlayHover.png').convert_alpha()
        else:
            start_img = pygame.image.load('./images/boutons/Play.png').convert_alpha()
        start_button = button.Button(400, 350, start_img, 0.8)
        if start_button.draw(screen):
            etape = 1

        if 600 > mx > 400 and 520 > my > 450:
            rules_img = pygame.image.load('./images/boutons/HowToPlayHover.png').convert_alpha()
        else:
            rules_img = pygame.image.load('./images/boutons/HowToPlay.png').convert_alpha()
        rules_button = button.Button(400, 450, rules_img, 0.8)
        if rules_button.draw(screen):
            etape = 9

        if 1000 > mx > 800 and 678 > my > 630:
            credits_img = pygame.image.load('./images/boutons/creditsHover.png').convert_alpha()
        else:
            credits_img = pygame.image.load('./images/boutons/credits.png').convert_alpha()
        credits_button = button.Button(800, 630, credits_img, 0.8)
        if credits_button.draw(screen):
            etape = 10

        if 1000 > mx > 800 and 748 > my > 700:
            quit_img = pygame.image.load('./images/boutons/quitHover.png').convert_alpha()
        else:
            quit_img = pygame.image.load('./images/boutons/quit.png').convert_alpha()
        quit_button = button.Button(800, 700, quit_img, 0.8)
        if quit_button.draw(screen):
            pygame.quit()
            sys.exit()

    if etape == 1:
        screen.fill((168, 211, 228))
        nb_play = pygame.image.load('./images/boutons/numberOfPayers.png').convert_alpha()
        nb_play = button.Button(262, 20, nb_play, 1)
        nb_play.draw(screen)
        mx, my = pygame.mouse.get_pos()

        if 300 > mx > 50 and 728 > my > 668:
            back_img = pygame.image.load('./images/boutons/ReturnHover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/Return.png').convert_alpha()
        back_button = button.Button(50, 668, back_img, 1)
        if back_button.draw(screen):
            if Pred and pygame.mouse.get_pressed()[0]:
                etape = 0
        Pred = False

        if 468 > mx > 168 and 400 > my > 200:
            pu_img = pygame.image.load('./images/boutons/1PlayerHover.png').convert_alpha()
        else:
            pu_img = pygame.image.load('./images/boutons/1Player.png').convert_alpha()
        pu_button = button.Button(168, 200, pu_img, 1)
        if pu_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                nb = 1
                etape = 2

        if 868 > mx > 568 and 400 > my > 200:
            pu_img = pygame.image.load('./images/boutons/2PlayersHover.png').convert_alpha()
        else:
            pu_img = pygame.image.load('./images/boutons/2Players.png').convert_alpha()
        pu_button = button.Button(568, 200, pu_img, 1)
        if pu_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                nb = 2
                etape = 2

        if 468 > mx > 168 and 650 > my > 450:
            pu_img = pygame.image.load('./images/boutons/3PlayersHover.png').convert_alpha()
        else:
            pu_img = pygame.image.load('./images/boutons/3Players.png').convert_alpha()
        pu_button = button.Button(168, 450, pu_img, 1)
        if pu_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                nb = 3
                etape = 2

        if 868 > mx > 568 and 650 > my > 450:
            pu_img = pygame.image.load('./images/boutons/4PlayersHover.png').convert_alpha()
        else:
            pu_img = pygame.image.load('./images/boutons/4Players.png').convert_alpha()
        pu_button = button.Button(568, 450, pu_img, 1)
        if pu_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                nb = 4
                etape = 2

    if etape == 2:
        screen.fill((168, 211, 228))
        selec_lvl = pygame.image.load('./images/boutons/selectALevel.png').convert_alpha()
        selec_lvl = button.Button(262, 20, selec_lvl, 1)
        selec_lvl.draw(screen)
        mx, my = pygame.mouse.get_pos()

        if 300 > mx > 50 and 728 > my > 668:
            back_img = pygame.image.load('./images/boutons/ReturnHover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/Return.png').convert_alpha()
        back_button = button.Button(50, 668, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 1

        if 196 > mx > 46 and 400 > my > 250:
            back_img = pygame.image.load('./images/boutons/1Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/1.png').convert_alpha()
        back_button = button.Button(46, 250, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 1

        if 391 > mx > 241 and 400 > my > 250:
            back_img = pygame.image.load('./images/boutons/2Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/2.png').convert_alpha()
        back_button = button.Button(241, 250, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 2

        if 586 > mx > 436 and 400 > my > 250:
            back_img = pygame.image.load('./images/boutons/3Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/3.png').convert_alpha()
        back_button = button.Button(436, 250, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 3

        if 781 > mx > 631 and 400 > my > 250:
            back_img = pygame.image.load('./images/boutons/4Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/4.png').convert_alpha()
        back_button = button.Button(631, 250, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 4

        if 976 > mx > 826 and 400 > my > 250:
            back_img = pygame.image.load('./images/boutons/5Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/5.png').convert_alpha()
        back_button = button.Button(826, 250, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 5

        if 196 > mx > 46 and 595 > my > 445:
            back_img = pygame.image.load('./images/boutons/6Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/6.png').convert_alpha()
        back_button = button.Button(46, 445, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 6

        if 391 > mx > 241 and 595 > my > 445:
            back_img = pygame.image.load('./images/boutons/7Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/7.png').convert_alpha()
        back_button = button.Button(241, 445, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 7

        if 586 > mx > 436 and 595 > my > 445:
            back_img = pygame.image.load('./images/boutons/8Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/8.png').convert_alpha()
        back_button = button.Button(436, 445, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 8

        if 781 > mx > 631 and 595 > my > 445:
            back_img = pygame.image.load('./images/boutons/9Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/9.png').convert_alpha()
        back_button = button.Button(631, 445, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 9

        if 976 > mx > 826 and 595 > my > 445:
            back_img = pygame.image.load('./images/boutons/10Hover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/10.png').convert_alpha()
        back_button = button.Button(826, 445, back_img, 1)
        if back_button.draw(screen):
            if pygame.mouse.get_pressed()[0]:
                etape = 3
                lvl = 10

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
        if level.run() == 5:
            etape = 2

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

    if etape == 10:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 50)
        draw_text('Credits', font, (255, 255, 255), screen, 400, 20)
        font = pygame.font.SysFont(None, 20)
        draw_text('Réalisé grace à ...', font, (255, 255, 255), screen, 300, 100)
        mx, my = pygame.mouse.get_pos()
        Pred = False

        buttonS_1 = pygame.Rect(50, 50, 100, 50)
        if buttonS_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                etape = 0
        pygame.draw.rect(screen, (255, 0, 0), buttonS_1)
        draw_text('Retour', font, (255, 255, 255), screen, 60, 60)

    if not pygame.mouse.get_pressed()[0]:
        Pred = True
    else:
        Pred = False

    # drawing logic
    pygame.display.update()
    clock.tick(60)
