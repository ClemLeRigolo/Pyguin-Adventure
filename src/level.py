import pygame
from settings import *
from sol1 import Sol1
from sol2 import Sol2
from sol3 import Sol3
from sol4 import Sol4
from sol5 import Sol5
from ice import Ice
from fish import Fish
from door import Door
from igloo import Igloo
from player import Player
from limit import Limit
from timer import Timer

class Level:
	def __init__(self):

		# level setup
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = CameraGroup()
		self.active_sprites = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()
		self.fish_sprites = pygame.sprite.Group()
		self.door_sprites = pygame.sprite.Group()
		self.igloo_sprites = pygame.sprite.Group()
		self.limit_sprites = pygame.sprite.Group()
		self.time = Timer()
		self.time.start()
		self.time_start = self.time.real()
		self.time_last = 0
		self.night = False

		self.setup_level()

	def setup_level(self):
		for row_index,row in enumerate(LEVEL_MAP):
			for col_index,col in enumerate(row):
				x = col_index * TILE_SIZE
				y = row_index * TILE_SIZE
				if col == '1':
					Sol1((x,y),[self.visible_sprites, self.collision_sprites])
				if col == '2':
					Sol2((x,y),[self.visible_sprites, self.collision_sprites])
				if col == '3':
					Sol3((x,y),[self.visible_sprites, self.collision_sprites])
				if col == '4':
					Sol4((x,y),[self.visible_sprites, self.collision_sprites])
				if col == '5':
					Sol5((x,y),[self.visible_sprites, self.collision_sprites])
				if col == 'B':
					Ice((x,y),[self.visible_sprites, self.collision_sprites])
				if col == 'P':
					self.player1 = Player((x, y), [self.visible_sprites, self.active_sprites], [self.active_sprites, self.collision_sprites, self.fish_sprites, self.visible_sprites,self.door_sprites,self.igloo_sprites, self.limit_sprites],1)
				if col == 'Q':
					self.player2 = Player((x, y), [self.visible_sprites, self.active_sprites], [self.active_sprites, self.collision_sprites, self.fish_sprites, self.visible_sprites,self.door_sprites,self.igloo_sprites, self.limit_sprites],2)
				if col == 'F':
					self.fish = Fish((x, y), [self.visible_sprites, self.collision_sprites, self.fish_sprites])
				if col == 'D':
					self.door = Door((x, y), [self.visible_sprites, self.collision_sprites, self.door_sprites])
				if col == 'I':
					self.igloo = Igloo((x, y), [self.visible_sprites, self.collision_sprites,self.igloo_sprites])
				if col == 'Y':
					self.limit = Limit((x,y),self.limit_sprites)


	def run(self):
		# run the entire game (level)
		if self.night:
			print("nuit")
			if self.time.real()-self.time_start-self.time_last >= 10:
				self.night = False
				self.time_last = self.time.real()-self.time_start
		else:
			print("jour")
			if self.time.real()-self.time_start-self.time_last >= 20:
				self.night = True
				self.time_last = self.time.real()-self.time_start
		self.player1.nuit(self.night)
		self.player2.nuit(self.night)
		self.player1.update_pos()
		self.player2.update_pos()
		self.active_sprites.update()
		self.visible_sprites.custom_draw(self.player1,self.player2)
		self.visible_sprites.custom_draw(self.player2, self.player1)

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2(100,300)

		# center camera setup 
		# self.half_w = self.display_surface.get_size()[0] // 2
		# self.half_h = self.display_surface.get_size()[1] // 2

		# camera
		cam_left = CAMERA_BORDERS['left']
		cam_top = CAMERA_BORDERS['top']
		cam_width = self.display_surface.get_size()[0] - (cam_left + CAMERA_BORDERS['right'])
		cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BORDERS['bottom'])

		self.camera_rect = pygame.Rect(cam_left,cam_top-64,cam_width,cam_height)

	def custom_draw(self,player1,player2):

		# get the player offset 
		# self.offset.x = player.rect.centerx - self.half_w
		# self.offset.y = player.rect.centery - self.half_h

		# getting the camera position

		if player1.rect.left < self.camera_rect.left:
			if player2.rect.right >= self.camera_rect.right:
				player1.possibleG = False
				player2.possibleD = False
			else:
				player1.possibleG = True
				player2.possibleD = True
		if player1.rect.right > self.camera_rect.right:
			if player2.rect.left <= self.camera_rect.left:
				player1.possibleD = False
				player2.possibleG = False
			else:
				player1.possibleD = True
				player2.possibleG = True

		self.camera_rect.left = (player2.rect.left + player1.rect.left) / 2 - 640 + CAMERA_BORDERS['left']

		# camera offset 
		self.offset = pygame.math.Vector2(
			self.camera_rect.left - CAMERA_BORDERS['left'],
			self.camera_rect.top - CAMERA_BORDERS['top'])

		for sprite in self.sprites():
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
