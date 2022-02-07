import pygame
import pytmx
import pyscroll

from pinguin import Pinguin

class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode((2000,1000))
        pygame.display.set_caption("Pyco Park")

        tmx_data = pytmx.util_pygame.load_pygame("../carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())

        player_position = tmx_data.get_object_by_name("Pinguin")
        self.player = Pinguin(player_position.x,player_position.y)

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)


    def run(self):

        running = True

        while running:

            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


        pygame.quit()
