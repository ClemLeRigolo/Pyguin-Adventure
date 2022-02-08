import pygame, sys
from settings import * 
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Penguins Adventure')
clock = pygame.time.Clock()

lvl=2
selec=True

level = Level(lvl-1)

bg = pygame.image.load("./images/map/background1.png")

while True:
	# event loop

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#if selec==True:

	screen.blit(bg, (0, 0))
	level.run()


	# drawing logic
	pygame.display.update()
	clock.tick(60)