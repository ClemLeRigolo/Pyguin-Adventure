import pygame 
from settings import *

class Igloo(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#self.sprite_sheet = pygame.image.load('images\Pixel arts\Autres/igloo.png')
		self.sprite_sheet = pygame.image.load('images\Pixel arts\Blocs/base.png')
		self.image = self.get_image(0, 0)
		self.image.set_colorkey([0, 8, 255])
		self.rect = self.image.get_rect(topleft=pos)


	def get_image(self, x, y):
		image = pygame.Surface([64, 64])
		image.blit(self.sprite_sheet, (0, 0), (x, y, 64, 64))
		return image
