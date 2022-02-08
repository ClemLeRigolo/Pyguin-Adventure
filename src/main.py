import pygame, sys
sys.path.append('../')
from settings import *
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pyguins Adventure')
clock = pygame.time.Clock()

lvl=2
selec=True

level = Level(lvl-1)

programIcon = pygame.image.load('./images/icon/icon.png')
bg = pygame.image.load("./images/map/background1.png")

while True:
	# event loop

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#if selec==True:

	screen.blit(bg, (0, 0))
	pygame.display.set_icon(programIcon)
	level.run()


	# drawing logic
	pygame.display.update()
	clock.tick(60)