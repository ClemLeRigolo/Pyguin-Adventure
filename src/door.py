import pygame
from settings import *


class Door(pygame.sprite.Sprite):

	def __init__(self,pos,groups):
		super().__init__(groups)
		self.sprite_sheet = pygame.image.load('images/Pixel arts/Autres/OursPolaire.png')
		self.image = self.get_image(0, 0)
		self.image.set_colorkey([0,7,255])
		self.rect = self.image.get_rect(topleft=pos)
		self.grab=False


	def get_image(self, x, y):
		image = pygame.Surface([128, 128])
		image.blit(self.sprite_sheet, (0, 0), (x, y, 128, 128))
		return image
