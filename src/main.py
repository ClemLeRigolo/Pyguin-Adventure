import pygame
pygame.init()

pygame.display.set_mode((1280,720))#, pygame.FULLSCREEN)
pygame.display.set_caption("Pyco Park")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
