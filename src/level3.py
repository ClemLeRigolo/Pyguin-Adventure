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
from mask import Mask
from bloc import Bloc
from homard import Homard
from bloc_break import Bloc_break


class Level3:
    def __init__(self, lvl, nb):

        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.fish_sprites = pygame.sprite.Group()
        self.mask_sprites = pygame.sprite.Group()
        self.door_sprites = pygame.sprite.Group()
        self.igloo_sprites = pygame.sprite.Group()
        self.limit_sprites = pygame.sprite.Group()
        self.bloc_sprites = pygame.sprite.Group()
        self.homard_sprites = pygame.sprite.Group()
        self.bloc_break_sprites = pygame.sprite.Group()
        self.time = Timer()
        self.time.start()
        self.time_start = self.time.real()
        self.time_last = 0
        self.time_last_super = 0
        self.time_last_homard = 0
        self.night = False
        pygame.mixer.init()
        pygame.mixer.music.load("sound/Pyguin_adventure_ost.mp3")
        pygame.mixer.music.play(loops=-1)
        self.bgj = pygame.image.load("./images/map/background1.png")
        self.bgn = pygame.image.load("./images/map/background2.png")
        self.change = False
        self.mask_is = False
        self.homard_is = False

        self.setup_level(lvl, nb)

    def setup_level(self, lvl, nb):
        for row_index, row in enumerate(LEVEL_MAP[nb][lvl]):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == '1':
                    Sol1((x, y), [self.visible_sprites, self.collision_sprites])
                if col == '2':
                    Sol2((x, y), [self.visible_sprites, self.collision_sprites])
                if col == '3':
                    Sol3((x, y), [self.visible_sprites, self.collision_sprites])
                if col == '4':
                    Sol4((x, y), [self.visible_sprites, self.collision_sprites])
                if col == '5':
                    Sol5((x, y), [self.visible_sprites, self.collision_sprites])
                if col == 'B':
                    Ice((x, y), [self.visible_sprites, self.collision_sprites])
                if col == 'P':
                    self.player1 = Player((x, y), [self.visible_sprites, self.active_sprites],
                                          [self.active_sprites, self.collision_sprites, self.fish_sprites,
                                           self.visible_sprites, self.door_sprites, self.igloo_sprites,
                                           self.limit_sprites, self.mask_sprites, self.bloc_sprites,
                                           self.homard_sprites, self.bloc_break_sprites], 1, "Gris")
                if col == 'Q':
                    self.player2 = Player((x, y), [self.visible_sprites, self.active_sprites],
                                          [self.active_sprites, self.collision_sprites, self.fish_sprites,
                                           self.visible_sprites, self.door_sprites, self.igloo_sprites,
                                           self.limit_sprites, self.mask_sprites, self.bloc_sprites,
                                           self.homard_sprites, self.bloc_break_sprites], 2, "Gris")
                if col == 'R':
                    self.player3 = Player((x, y), [self.visible_sprites, self.active_sprites],
                                          [self.active_sprites, self.collision_sprites, self.fish_sprites,
                                           self.visible_sprites, self.door_sprites, self.igloo_sprites,
                                           self.limit_sprites, self.mask_sprites, self.bloc_sprites,
                                           self.homard_sprites, self.bloc_break_sprites], 3, "Gris")
                if col == 'F':
                    self.fish = Fish((x, y), [self.visible_sprites, self.collision_sprites, self.fish_sprites])
                if col == 'D':
                    self.door = Door((x, y), [self.visible_sprites, self.collision_sprites, self.door_sprites])
                if col == 'I':
                    self.igloo = Igloo((x, y), [self.visible_sprites, self.collision_sprites, self.igloo_sprites])
                if col == 'Y':
                    self.limit = Limit((x, y), self.limit_sprites)
                if col == 'M':
                    self.mask = Mask((x, y), [self.visible_sprites, self.mask_sprites])
                    self.mask_is = True
                if col == 'X':
                    self.bloc = Bloc((x, y), [self.visible_sprites, self.bloc_sprites])
                if col == 'H':
                    self.homard = Homard((x, y), [self.visible_sprites, self.homard_sprites])
                    self.homard_is = True
                if col == 'C':
                    self.bloc_break = Bloc_break((x, y), [self.visible_sprites, self.bloc_break_sprites,
                                                            self.collision_sprites])
        if not self.mask_is:
            self.mask = Mask((-200, -300), [self.visible_sprites, self.mask_sprites])
        if not self.homard_is:
            self.homard = Homard((-200, -300), [self.visible_sprites, self.homard_sprites])

    def run(self):
        # run the entire game (level)
        if self.mask.grab and self.time_last_super == 0:
            self.time_last_super = self.time.real() - self.time_start
            if self.mask.nb == 1:
                self.player1.super_hero(True)
            elif self.mask.nb == 2:
                self.player2.super_hero(True)
            elif self.mask.nb == 3:
                self.player3.super_hero(True)
        elif 25 > self.time.real() - self.time_start - self.time_last_super >= 20:
            if self.mask.nb == 1:
                self.player1.super_hero(False)
            elif self.mask.nb == 2:
                self.player2.super_hero(False)
            elif self.mask.nb == 3:
                self.player3.super_hero(False)
            self.mask.nb = 0
        elif self.time.real() - self.time_start - self.time_last_super >= 25:
            self.time_last_super = 0
            self.mask.grab = False
            self.mask_sprites.add(self.mask)
            self.visible_sprites.add(self.mask)
        if self.homard.grab and self.time_last_homard == 0:
            self.time_last_homard = self.time.real() - self.time_start
            if self.homard.nb == 1:
                self.player1.set_homard(True)
            elif self.homard.nb == 2:
                self.player2.set_homard(True)
            elif self.homard.nb == 3:
                self.player3.set_homard(True)
        elif 25 > self.time.real() - self.time_start - self.time_last_homard >= 20:
            if self.homard.nb == 1:
                self.player1.set_homard(False)
            elif self.homard.nb == 2:
                self.player2.set_homard(False)
            elif self.homard.nb == 3:
                self.player3.set_homard(False)
            self.homard.nb = 0
        elif self.time.real() - self.time_start - self.time_last_homard >= 25:
            self.time_last_homard = 0
            self.homard.grab = False
            self.homard_sprites.add(self.homard)
            self.visible_sprites.add(self.homard)
        if self.night:
            self.display_surface.blit(self.bgn.convert_alpha(), (0, 0))
            if self.time.real() - self.time_start - self.time_last >= 10:
                self.night = False
                self.time_last = self.time.real() - self.time_start
        else:
            self.display_surface.blit(self.bgj.convert_alpha(), (0, 0))
            if self.time.real() - self.time_start - self.time_last >= 20:
                self.night = True
                self.time_last = self.time.real() - self.time_start
        self.player1.nuit(self.night)
        self.player2.nuit(self.night)
        self.player3.nuit(self.night)
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player1, self.player2, self.player3)
        self.visible_sprites.custom_draw(self.player2, self.player1, self.player3)
        self.visible_sprites.custom_draw(self.player3, self.player1, self.player2)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100, 300)

        # center camera setup
        # self.half_w = self.display_surface.get_size()[0] // 2
        # self.half_h = self.display_surface.get_size()[1] // 2

        # camera
        cam_left = CAMERA_BORDERS['left']
        cam_top = CAMERA_BORDERS['top']
        cam_width = self.display_surface.get_size()[0] - (cam_left + CAMERA_BORDERS['right'])
        cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BORDERS['bottom'])

        self.camera_rect = pygame.Rect(cam_left, cam_top - 64, cam_width, cam_height)

    def custom_draw(self, player1, player2, player3):

        # get the player offset
        # self.offset.x = player.rect.centerx - self.half_w
        # self.offset.y = player.rect.centery - self.half_h

        # getting the camera position

        if player1.rect.left < self.camera_rect.left:
            if player2.rect.right >= self.camera_rect.right:
                player1.possibleG = False
                player2.possibleD = False
                player3.possibleD = True
            elif player3.rect.right >= self.camera_rect.right:
                player1.possibleG = False
                player2.possibleD = True
                player3.possibleD = False
            elif player3.rect.right >= self.camera_rect.right and player2.rect.right >= self.camera_rect.right:
                player1.possibleG = False
                player2.possibleD = False
                player3.possibleD = False
            else:
                player1.possibleG = True
                player2.possibleD = True
                player3.possibleD = True
        if player1.rect.right > self.camera_rect.right:
            if player2.rect.left <= self.camera_rect.left:
                player1.possibleD = False
                player2.possibleG = False
                player3.possibleG = True
            elif player3.rect.left <= self.camera_rect.left:
                player1.possibleD = False
                player2.possibleG = True
                player3.possibleG = False
            elif player2.rect.left <= self.camera_rect.left and player3.rect.left <= self.camera_rect.left:
                player1.possibleD = False
                player2.possibleG = False
                player3.possibleG = False
            else:
                player1.possibleD = True
                player2.possibleG = True
                player3.possibleG = True

        left = max(player1.rect.left, player2.rect.left, player3.rect.left)
        right = min(player1.rect.left, player2.rect.left, player3.rect.left)
        self.camera_rect.left = (left + right) / 2 - 512 + CAMERA_BORDERS['left']

        # camera offset
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - CAMERA_BORDERS['left'],
            self.camera_rect.top - CAMERA_BORDERS['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
