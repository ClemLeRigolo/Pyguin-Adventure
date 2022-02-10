import pygame
import button


class Color_selec:
    def __init__(self, nb):
        self.display_surface = pygame.display.get_surface()
        self.active_sprites = pygame.sprite.Group()
        self.nb = nb + 1
        self.setup_color()
        self.p1 = False
        self.p2 = False
        self.p3 = False
        self.p4 = False
        self.p1_pos = (0, 0)
        self.p2_pos = (0, 0)
        self.p3_pos = (0, 0)
        self.p4_pos = (0, 0)
        self.c1 = "Noir"
        self.c2 = "Noir"
        self.c3 = "Noir"
        self.c4 = "Noir"
        self.click = False

    def setup_color(self):
        if self.nb == 1:
            self.player1 = True
            self.player2 = False
            self.player3 = False
            self.player4 = False
        if self.nb == 2:
            self.player1 = True
            self.player2 = True
            self.player3 = False
            self.player4 = False
        if self.nb == 3:
            self.player1 = True
            self.player2 = True
            self.player3 = True
            self.player4 = False
        if self.nb == 4:
            self.player1 = True
            self.player2 = True
            self.player3 = True
            self.player4 = True

    def run(self):
        bg = pygame.image.load('./images/map/backgroundIHM.png').convert_alpha()
        bg = button.Button(0, 0, bg, 1)
        bg.draw(self.display_surface)
        selec_color = pygame.image.load('./images/boutons/selectAColor.png').convert_alpha()
        selec_color = button.Button(262, 20, selec_color, 1)
        selec_color.draw(self.display_surface)
        mx, my = pygame.mouse.get_pos()
        if 300 > mx > 50 and 728 > my > 668:
            back_img = pygame.image.load('./images/boutons/ReturnHover.png').convert_alpha()
        else:
            back_img = pygame.image.load('./images/boutons/Return.png').convert_alpha()
        back_button = button.Button(50, 668, back_img, 1)
        if back_button.draw(self.display_surface):
            if pygame.mouse.get_pressed()[0]:
                return ("Noir", "Noir", "Noir", "Noir")
        back = pygame.Rect(107, 245, 805, 325)
        pygame.draw.rect(self.display_surface, (0, 0, 0), back)
        rouge = pygame.Rect(112, 250, 155, 155)
        pygame.draw.rect(self.display_surface, (255, 0, 0), rouge)
        if rouge.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1 and self.c2 != "Rouge" and self.c3 != "Rouge" and self.c4 != "Rouge") or self.c1 == "Rouge":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "Rouge"
                        self.p1_pos = (rouge.x, rouge.y)
                elif (not self.p2 and self.c1 != "Rouge" and self.c3 != "Rouge" and self.c4 != "Rouge" and self.nb > 1) or self.c2 == "Rouge":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "Rouge"
                        self.p2_pos = (rouge.x, rouge.y)
                elif (not self.p3 and self.c1 != "Rouge" and self.c2 != "Rouge" and self.c4 != "Rouge" and self.nb > 2) or self.c3 == "Rouge":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "Rouge"
                        self.p3_pos = (rouge.x, rouge.y)
                elif (not self.p4 and self.c1 != "Rouge" and self.c2 != "Rouge" and self.c3 != "Rouge" and self.nb > 3) or self.c4 == "Rouge":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "Rouge"
                        self.p4_pos = (rouge.x, rouge.y)
        cyan = pygame.Rect(272, 250, 155, 155)
        pygame.draw.rect(self.display_surface, (0, 208, 255), cyan)
        if cyan.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1 and self.c2 != "BleuClair" and self.c3 != "BleuClair" and self.c4 != "BleuClair") or self.c1 == "BleuClair":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "BleuClair"
                        self.p1_pos = (cyan.x, cyan.y)
                elif (not self.p2 and self.c1 != "BleuClair" and self.c3 != "BleuClair" and self.c4 != "BleuClair" and self.nb > 1) or self.c2 == "BleuClair":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "BleuClair"
                        self.p2_pos = (cyan.x, cyan.y)
                elif (not self.p3 and self.c1 != "BleuClair" and self.c2 != "BleuClair" and self.c4 != "BleuClair" and self.nb > 2) or self.c3 == "BleuClair":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "BleuClair"
                        self.p3_pos = (cyan.x, cyan.y)
                elif (not self.p4 and self.c1 != "BleuClair" and self.c2 != "BleuClair" and self.c3 != "BleuClair" and self.nb > 3) or self.c4 == "BleuClair":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "BleuClair"
                        self.p4_pos = (cyan.x, cyan.y)
        vert = pygame.Rect(432, 250, 155, 155)
        pygame.draw.rect(self.display_surface, (0, 122, 9), vert)
        if vert.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1 and self.c2 != "VertFoncé" and self.c3 != "VertFoncé" and self.c4 != "VertFoncé") or self.c1 == "VertFoncé":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "VertFoncé"
                        self.p1_pos = (vert.x, vert.y)
                elif (not self.p2 and self.c1 != "VertFoncé" and self.c3 != "VertFoncé" and self.c4 != "VertFoncé" and self.nb > 1) or self.c2 == "VertFoncé":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "VertFoncé"
                        self.p2_pos = (vert.x, vert.y)
                elif (not self.p3 and self.c1 != "VertFoncé" and self.c2 != "VertFoncé" and self.c4 != "VertFoncé" and self.nb > 2) or self.c3 == "VertFoncé":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "VertFoncé"
                        self.p3_pos = (vert.x, vert.y)
                elif (not self.p4 and self.c1 != "VertFoncé" and self.c2 != "VertFoncé" and self.c3 != "VertFoncé" and self.nb > 3) or self.c4 == "VertFoncé":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "VertFoncé"
                        self.p4_pos = (vert.x, vert.y)
        violet = pygame.Rect(592, 250, 155, 155)
        pygame.draw.rect(self.display_surface, (164, 0, 255), violet)
        if violet.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1 and self.c2 != "Mauve" and self.c3 != "Mauve" and self.c4 != "Mauve") or self.c1 == "Mauve":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "Mauve"
                        self.p1_pos = (violet.x, violet.y)
                elif (not self.p2 and self.c1 != "Mauve" and self.c3 != "Mauve" and self.c4 != "Mauve" and self.nb > 1) or self.c2 == "Mauve":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "Mauve"
                        self.p2_pos = (violet.x, violet.y)
                elif (not self.p3 and self.c1 != "Mauve" and self.c2 != "Mauve" and self.c4 != "Mauve" and self.nb > 2) or self.c3 == "Mauve":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "Mauve"
                        self.p3_pos = (violet.x, violet.y)
                elif (not self.p4 and self.c1 != "Mauve" and self.c2 != "Mauve" and self.c3 != "Mauve" and self.nb > 3) or self.c4 == "Mauve":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "Mauve"
                        self.p4_pos = (violet.x, violet.y)
        gris = pygame.Rect(752, 250, 155, 155)
        pygame.draw.rect(self.display_surface, (65, 65, 65), gris)
        if gris.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1 and self.c2 != "Gris" and self.c3 != "Gris" and self.c4 != "Gris") or self.c1 == "Gris":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "Gris"
                        self.p1_pos = (gris.x, gris.y)
                elif (not self.p2 and self.c1 != "Gris" and self.c3 != "Gris" and self.c4 != "Gris" and self.nb > 1) or self.c2 == "Gris":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "Gris"
                        self.p2_pos = (gris.x, gris.y)
                elif (not self.p3 and self.c1 != "Gris" and self.c2 != "Gris" and self.c4 != "Gris" and self.nb > 2) or self.c3 == "Gris":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "Gris"
                        self.p3_pos = (gris.x, gris.y)
                elif (not self.p4 and self.c1 != "Gris" and self.c2 != "Gris" and self.c3 != "Gris" and self.nb > 3) or self.c4 == "Gris":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "Gris"
                        self.p4_pos = (gris.x, gris.y)
        orange = pygame.Rect(112, 410, 155, 155)
        pygame.draw.rect(self.display_surface, (255, 102, 0), orange)
        if orange.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1 and self.c2 != "Orange" and self.c3 != "Orange" and self.c4 != "Orange") or self.c1 == "Orange":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "Orange"
                        self.p1_pos = (orange.x, orange.y)
                elif (not self.p2 and self.c1 != "Orange" and self.c3 != "Orange" and self.c4 != "Orange" and self.nb > 1) or self.c2 == "Orange":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "Orange"
                        self.p2_pos = (orange.x, orange.y)
                elif (not self.p3 and self.c1 != "Orange" and self.c2 != "Orange" and self.c4 != "Orange" and self.nb > 2) or self.c3 == "Orange":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "Orange"
                        self.p3_pos = (orange.x, orange.y)
                elif (not self.p4 and self.c1 != "Orange" and self.c2 != "Orange" and self.c3 != "Orange" and self.nb > 3) or self.c4 == "Orange":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "Orange"
                        self.p4_pos = (orange.x, orange.y)
        blue = pygame.Rect(272, 410, 155, 155)
        pygame.draw.rect(self.display_surface, (0, 94, 255), blue)
        if blue.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1  and self.c2 != "Bleu" and self.c3 != "Bleu" and self.c4 != "Bleu") or self.c1 == "Bleu":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "Bleu"
                        self.p1_pos = (blue.x, blue.y)
                elif (not self.p2 and self.c1 != "Bleu" and self.c3 != "Bleu" and self.c4 != "Bleu" and self.nb > 1) or self.c2 == "Bleu":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "Bleu"
                        self.p2_pos = (blue.x, blue.y)
                elif (not self.p3 and self.c1 != "Bleu" and self.c2 != "Bleu" and self.c4 != "Bleu" and self.nb > 2) or self.c3 == "Bleu":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "Bleu"
                        self.p3_pos = (blue.x, blue.y)
                elif (not self.p4 and self.c1 != "Bleu" and self.c2 != "Bleu" and self.c3 != "Bleu" and self.nb > 3) or self.c4 == "Bleu":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "Bleu"
                        self.p4_pos = (blue.x, blue.y)
        vertclair = pygame.Rect(432, 410, 155, 155)
        pygame.draw.rect(self.display_surface, (45, 255, 0), vertclair)
        if vertclair.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1  and self.c2 != "Vert" and self.c3 != "Vert" and self.c4 != "Vert") or self.c1 == "Vert":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "Vert"
                        self.p1_pos = (vertclair.x, vertclair.y)
                elif (not self.p2 and self.c1 != "Vert" and self.c3 != "Vert" and self.c4 != "Vert" and self.nb > 1) or self.c2 == "Vert":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "Vert"
                        self.p2_pos = (vertclair.x, vertclair.y)
                elif (not self.p3 and self.c1 != "Vert" and self.c2 != "Vert" and self.c4 != "Vert" and self.nb > 2) or self.c3 == "Vert":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "Vert"
                        self.p3_pos = (vertclair.x, vertclair.y)
                elif (not self.p4 and self.c1 != "Vert" and self.c2 != "Vert" and self.c3 != "Vert" and self.nb > 3) or self.c4 == "Vert":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "Vert"
                        self.p4_pos = (vertclair.x, vertclair.y)
        rose = pygame.Rect(592, 410, 155, 155)
        pygame.draw.rect(self.display_surface, (255, 0, 187), rose)
        if rose.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1 and self.c2 != "Rose" and self.c3 != "Rose" and self.c4 != "Rose") or self.c1 == "Rose":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "Rose"
                        self.p1_pos = (rose.x, rose.y)
                elif (not self.p2 and self.c1 != "Rose" and self.c3 != "Rose" and self.c4 != "Rose" and self.nb > 1) or self.c2 == "Rose":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "Rose"
                        self.p2_pos = (rose.x, rose.y)
                elif (not self.p3 and self.c1 != "Rose" and self.c2 != "Rose" and self.c4 != "Rose" and self.nb > 2) or self.c3 == "Rose":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "Rose"
                        self.p3_pos = (rose.x, rose.y)
                elif (not self.p4 and self.c1 != "Rose" and self.c2 != "Rose" and self.c3 != "Rose" and self.nb > 3) or self.c4 == "Rose":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "Rose"
                        self.p4_pos = (rose.x, rose.y)
        jaune = pygame.Rect(752, 410, 155, 155)
        pygame.draw.rect(self.display_surface, (251, 255, 0), jaune)
        if jaune.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                if (not self.p1 and self.c2 != "Jaune" and self.c3 != "Jaune" and self.c4 != "Jaune") or self.c1 == "Jaune":
                    if self.click and self.p1:
                        self.p1 = False
                        self.c1 = "Noir"
                    elif self.click:
                        self.p1 = True
                        self.c1 = "Jaune"
                        self.p1_pos = (jaune.x, jaune.y)
                elif (not self.p2 and self.c1 != "Jaune" and self.c3 != "Jaune" and self.c4 != "Jaune" and self.nb > 1) or self.c2 == "Jaune":
                    if self.click and self.p2:
                        self.p2 = False
                        self.c2 = "Noir"
                    elif self.click:
                        self.p2 = True
                        self.c2 = "Jaune"
                        self.p2_pos = (jaune.x, jaune.y)
                elif (not self.p3 and self.c1 != "Jaune" and self.c2 != "Jaune" and self.c4 != "Jaune" and self.nb > 2) or self.c3 == "Jaune":
                    if self.click and self.p3:
                        self.p3 = False
                        self.c3 = "Noir"
                    elif self.click:
                        self.p3 = True
                        self.c3 = "Jaune"
                        self.p3_pos = (jaune.x, jaune.y)
                elif (not self.p4 and self.c1 != "Jaune" and self.c2 != "Jaune" and self.c3 != "Jaune" and self.nb > 3) or self.c4 == "Jaune":
                    if self.click and self.p4:
                        self.p4 = False
                        self.c4 = "Noir"
                    elif self.click:
                        self.p4 = True
                        self.c4 = "Jaune"
                        self.p4_pos = (jaune.x, jaune.y)

        if self.nb == 1:
            self.p2 = False
            self.p3 = False
            self.p4 = False
        elif self.nb == 2:
            self.p3 = False
            self.p4 = False
        elif self.nb == 3:
            self.p4 = False
        else:
            self.p1 = self.p1

        if self.c1 == "Noir":
            self.p1 = False
        if self.c2 == "Noir":
            self.p2 = False
        if self.c3 == "Noir":
            self.p3 = False
        if self.c4 == "Noir":
            self.p4 = False

        if self.p1:
            back_img = pygame.image.load('./images/Pixel arts/Autres/player1.png').convert_alpha()
            back_button = button.Button(self.p1_pos[0], self.p1_pos[1], back_img, 1)
            back_button.draw(self.display_surface)

        if self.p2:
            back_img = pygame.image.load('./images/Pixel arts/Autres/player2.png').convert_alpha()
            back_button = button.Button(self.p2_pos[0], self.p2_pos[1], back_img, 1)
            back_button.draw(self.display_surface)

        if self.p3:
            back_img = pygame.image.load('./images/Pixel arts/Autres/player3.png').convert_alpha()
            back_button = button.Button(self.p3_pos[0], self.p3_pos[1], back_img, 1)
            back_button.draw(self.display_surface)

        if self.p4:
            back_img = pygame.image.load('./images/Pixel arts/Autres/player4.png').convert_alpha()
            back_button = button.Button(self.p4_pos[0], self.p4_pos[1], back_img, 1)
            back_button.draw(self.display_surface)

        if not pygame.mouse.get_pressed()[0]:
            self.click = True
        else:
            self.click = False

        if self.next_possible():
            if 974 > mx > 724 and 728 > my > 668:
                back_img = pygame.image.load('./images/boutons/NextHover.png').convert_alpha()
            else:
                back_img = pygame.image.load('./images/boutons/Next.png').convert_alpha()
            back_button = button.Button(724, 668, back_img, 1)
            if back_button.draw(self.display_surface):
                if pygame.mouse.get_pressed()[0]:
                    return (self.c1, self.c2, self.c3, self.c4)
    def next_possible(self):
        if self.nb == 1:
            return self.p1
        elif self.nb == 2:
            return self.p1 and self.p2
        elif self.nb == 3:
            return self.p1 and self.p2 and self.p3
        else:
            return self.p1 and self.p2 and self.p3 and self.p4