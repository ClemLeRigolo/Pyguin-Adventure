import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,collision_sprites,nb):
		super().__init__(groups)
		self.sprite_sheet = pygame.image.load('images\Pixel arts\Pingouins\pingouin1.png')
		self.image = self.get_image(0, 0)
		self.rect = self.image.get_rect(topleft = pos)

		# player movement
		self.nb=nb
		self.direction = pygame.math.Vector2()
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = 16
		self.collision_sprites = collision_sprites
		self.on_floor = False

	def input(self):
		keys = pygame.key.get_pressed()

		if self.nb==1:
			if keys[pygame.K_RIGHT]:
				self.direction.x = 1
			elif keys[pygame.K_LEFT]:
				self.direction.x = -1
			else:
				self.direction.x = 0

			if keys[pygame.K_UP] and self.on_floor:
				self.direction.y = -self.jump_speed

		if self.nb == 2:
			if keys[pygame.K_d]:
				self.direction.x = 1
			elif keys[pygame.K_q]:
				self.direction.x = -1
			else:
				self.direction.x = 0

			if keys[pygame.K_z] and self.on_floor:
				self.direction.y = -self.jump_speed

	def get_image(self, x, y):
		image = pygame.Surface([32, 32])
		image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
		return image

	def horizontal_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0:
					self.rect.left = sprite.rect.right
				if self.direction.x > 0:
					self.rect.right = sprite.rect.left

	def vertical_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					self.on_floor = True
				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0

		if self.on_floor and self.direction.y != 0:
			self.on_floor = False

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def update(self):
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.horizontal_collisions()
		self.apply_gravity()
		self.vertical_collisions()
