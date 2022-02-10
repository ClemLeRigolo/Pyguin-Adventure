import button
import pygame

from bloc import Bloc
from bloc_break import Bloc_break
from door import Door
from fish import Fish
from homard import Homard
from ice import Ice
from igloo import Igloo
from limit import Limit
from mask import Mask
from player import Player
from settings import *
from sol1 import Sol1
from sol2 import Sol2
from sol3 import Sol3
from sol4 import Sol4
from sol5 import Sol5
from timer import Timer


class Level1:
    def __init__(self, lvl, nb, c1):

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
        self.time_at_pause = 0
        self.time_at_play = 0
        self.minute = 0
        self.seconde = 0
        self.temps = pygame.font.SysFont(None, 100)
        self.night = False
        pygame.mixer.init()
        pygame.mixer.music.load("sound/Pyguin_adventure_ost.mp3")
        pygame.mixer.music.play(loops=-1)
        self.bgj = pygame.image.load("./images/map/background1.png")
        self.bgn = pygame.image.load("./images/map/background2.png")
        self.change = False
        self.mask_is = False
        self.homard_is = False
        self.game_paused = False

        self.c1 = c1

        self.nb_fish = self.setup_level(lvl, nb)

        self.player1.set_fish(self.nb_fish)

    def setup_level(self, lvl, nb):
        fish = 0
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
                                           self.homard_sprites, self.bloc_break_sprites], 1, self.c1)
                if col == 'F':
                    self.fish = Fish((x, y), [self.visible_sprites, self.collision_sprites, self.fish_sprites])
                    fish += 1
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
                    self.bloc_break = Bloc_break((x, y), [self.visible_sprites, self.bloc_break_sprites, self.collision_sprites])
        if not self.mask_is:
            self.mask = Mask((-200, -300), [self.visible_sprites, self.mask_sprites])
        if not self.homard_is:
            self.homard = Homard((-200, -300), [self.visible_sprites, self.homard_sprites])
        return fish

    def run(self):
        # run the entire game (level)
        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()
        if keys[pygame.K_ESCAPE] and not self.game_paused:
            if self.night:
                self.display_surface.blit(self.bgn.convert_alpha(), (0, 0))
            else:
                self.display_surface.blit(self.bgj.convert_alpha(), (0, 0))
            bgpause = pygame.Rect(51, 38, 921, 691)
            pygame.draw.rect(self.display_surface, (168, 211, 228), bgpause)
            self.game_paused = True
            pygame.mixer.music.pause()
            self.time_at_pause = self.time.real() - self.time_start
        elif self.game_paused:
            if self.night:
                self.display_surface.blit(self.bgn.convert_alpha(), (0, 0))
            else:
                self.display_surface.blit(self.bgj.convert_alpha(), (0, 0))
            bgpause = pygame.Rect(51, 38, 921, 691)
            pygame.draw.rect(self.display_surface, (168, 211, 228), bgpause)
            self.minute = self.time_at_pause.real // 60
            self.seconde = (self.time_at_pause.real % 60) // 1
            temps_pause = pygame.font.SysFont(None, 50)
            if self.seconde <10:
                img = temps_pause.render('(' + str(int(self.minute)) + ':0' + str(int(self.seconde)) + ')', True, (0, 0, 0))
                self.display_surface.blit(img, (462, 50))
            else:
                img = temps_pause.render('(' + str(int(self.minute)) + ':' + str(int(self.seconde)) + ')', True, (0, 0, 0))
                self.display_surface.blit(img, (451, 50))
            pause_img = pygame.image.load('./images/boutons/pause.png').convert_alpha()
            pause_button = button.Button(262, 100, pause_img, 1)
            pause_button.draw(self.display_surface)
            if 762 > mx > 262 and 460 > my > 300:
                resum_img = pygame.image.load('./images/boutons/resumeHover.png').convert_alpha()
            else:
                resum_img = pygame.image.load('./images/boutons/resume.png').convert_alpha()
            resum_button = button.Button(262, 300, resum_img, 1)
            if resum_button.draw(self.display_surface):
                pygame.mixer.music.unpause()
                self.game_paused = False
                self.time_at_play = self.time.real() - self.time_start
                self.time_start += self.time_at_play - self.time_at_pause
            if 762 > mx > 262 and 660 > my > 500:
                leave_img = pygame.image.load('./images/boutons/leaveHover.png').convert_alpha()
            else:
                leave_img = pygame.image.load('./images/boutons/leave.png').convert_alpha()
            leave_button = button.Button(262, 500, leave_img, 1)
            if leave_button.draw(self.display_surface):
                return 5
        else:
            if self.mask.grab and self.time_last_super == 0:
                self.time_last_super = self.time.real() - self.time_start
                if self.mask.nb == 1:
                    self.player1.super_hero(True)
            elif 25 > self.time.real() - self.time_start - self.time_last_super >= 20:
                if self.mask.nb == 1:
                    self.player1.super_hero(False)
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
            elif 25 > self.time.real() - self.time_start - self.time_last_homard >= 20:
                if self.homard.nb == 1:
                    self.player1.set_homard(False)
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
            # self.active_sprites.update()
            self.visible_sprites.custom_draw(self.player1)
            if self.player1.update() == 5:
                pygame.mixer.music.stop()
                return 5

            bg_time = pygame.image.load('./images/boutons/backgroundTime.png').convert_alpha()
            bg_button = button.Button(0, 0, bg_time, 1)
            bg_button.draw(self.display_surface)
            bg_button = button.Button(800, 0, bg_time, 1)
            bg_button.draw(self.display_surface)
            self.minute = (self.time.real() - self.time_start) // 60
            self.seconde = ((self.time.real() - self.time_start) % 60) // 1
            if self.seconde < 10:
                img = self.temps.render(str(int(self.minute)) + ':0' + str(int(self.seconde)), True, (0, 0, 0))
            else:
                img = self.temps.render(str(int(self.minute)) + ':' + str(int(self.seconde)), True, (0, 0, 0))
            if self.minute < 10:
                self.display_surface.blit(img, (40, 20))
            else:
                self.display_surface.blit(img, (20, 20))
            fish_catch = 0
            for sprite in self.fish_sprites.sprites():
                if sprite.grab:
                    fish_catch += 1
            self.player1.set_grab(fish_catch)
            img = self.temps.render(str(fish_catch) + '/' + str(self.nb_fish), True, (0, 0, 0))
            self.display_surface.blit(img, (820, 20))
            bg_time = pygame.image.load('./images/Pixel arts/Autres/PoissonPng.png').convert_alpha()
            bg_button = button.Button(950, 20, bg_time, 2)
            bg_button.draw(self.display_surface)


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

        self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_height)

    def custom_draw(self, player1):

        # get the player offset
        # self.offset.x = player.rect.centerx - self.half_w
        # self.offset.y = player.rect.centery - self.half_h

        # getting the camera position



        self.camera_rect.left = (player1.rect.left) - 512 + CAMERA_BORDERS['left']

        # camera offset
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - CAMERA_BORDERS['left'],
            self.camera_rect.top - CAMERA_BORDERS['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
