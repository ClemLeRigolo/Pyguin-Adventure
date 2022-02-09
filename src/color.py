import pygame


class Color:
    def __init__(self, color):
        self.table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        self.table[0] = pygame.image.load("images\Pixel arts\Pingouins\Pingouin" + color + "G.png")
        self.table[1] = pygame.image.load("images\Pixel arts\Pingouins\Pingouin" + color + ".png")
        self.table[2] = pygame.image.load("images\Pixel arts\Pingouins\Saut" + color + "G.png")
        self.table[3] = pygame.image.load("images\Pixel arts\Pingouins\Saut" + color + ".png")
        self.table[4] = pygame.image.load("images\Pixel arts\Pingouins\Pingouin" + color + "_glisseG.png")
        self.table[5] = pygame.image.load("images\Pixel arts\Pingouins\Pingouin" + color + "_glisse.png")
        self.table[6] = pygame.image.load("images\Pixel arts\Pingouins\Diable" + color + "G.png")
        self.table[7] = pygame.image.load("images\Pixel arts\Pingouins\Diable" + color + ".png")
        self.table[8] = pygame.image.load("images\Pixel arts\Pingouins\SautDiable" + color + "G.png")
        self.table[9] = pygame.image.load("images\Pixel arts\Pingouins\SautDiable" + color + ".png")
        self.table[10] = pygame.image.load("images\Pixel arts\Pingouins\Diable" + color + "_glisseG.png")
        self.table[11] = pygame.image.load("images\Pixel arts\Pingouins\Diable" + color + "_glisse.png")
        self.table[12] = pygame.image.load("images\Pixel arts\Pingouins\SuperPingouin" + color + "G.png")
        self.table[13] = pygame.image.load("images\Pixel arts\Pingouins\SuperPingouin" + color + ".png")
        self.table[14] = pygame.image.load("images\Pixel arts\Pingouins\SuperPingouin" + color + "_glisseG.png")
        self.table[15] = pygame.image.load("images\Pixel arts\Pingouins\SuperPingouin" + color + "_glisse.png")
        self.table[16] = pygame.image.load("images\Pixel arts\Pingouins\SautSuperPingouin" + color + "G.png")
        self.table[17] = pygame.image.load("images\Pixel arts\Pingouins\SautSuperPingouin" + color + ".png")
        self.table[18] = pygame.image.load("images\Pixel arts\Pingouins\HommardPingouin" + color + "G.png")
        self.table[19] = pygame.image.load("images\Pixel arts\Pingouins\HommardPingouin" + color + ".png")
        self.table[20] = pygame.image.load("images\Pixel arts\Pingouins\SautHommardPingouin" + color + "G.png")
        self.table[21] = pygame.image.load("images\Pixel arts\Pingouins\SautHommardPingouin" + color + ".png")
        self.table[22] = pygame.image.load("images\Pixel arts\Pingouins\HommardPingouin" + color + "_glisseG.png")
        self.table[23] = pygame.image.load("images\Pixel arts\Pingouins\HommardPingouin" + color + "_glisse.png")




