import pygame
from settings import *


class Bloc(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load('images/map/blocglaceglisse.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 8, 255])
        self.rect = self.image.get_rect(topleft=pos)

    def get_image(self, x, y):
        image = pygame.Surface([64, 64])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 64, 64))
        return image

    def collision(self, val, bord, collisions_sprite, active_sprite):
        for sprite1 in collisions_sprite.sprites():
            for sprite2 in active_sprite.sprites():
                a = False
                if sprite1.rect.colliderect(self.rect):
                    return False
                if (sprite1.rect.right + 5 >= self.rect.left >= sprite1.rect.right - 5 and sprite1.rect.bottom == self.rect.bottom) or (sprite1.rect.left + 5 >= self.rect.right >= sprite1.rect.left - 5 and sprite1.rect.bottom == self.rect.bottom):
                    return False
                if sprite2.rect != bord.rect and ((sprite2.rect.right + 5 >= self.rect.left >= sprite2.rect.right - 5 and sprite2.rect.bottom == self.rect.bottom) or (sprite2.rect.left + 5 >= self.rect.right >= sprite2.rect.left - 5 and sprite2.rect.bottom == self.rect.bottom)):
                    return False
                if sprite2.rect.colliderect(self.rect) and not a:
                    if val:
                        if bord.direction.x == 0:
                            return False
                        if sprite2.rect != bord.rect:
                            return False
        return True
