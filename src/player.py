import pygame, sys
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, nb):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load('images\Pixel arts\Pingouins\PingouinGris.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 8, 255])
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.nb = nb
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.speedG = 20
        self.time = 0
        self.gravity = 0.8
        self.jump_speed = 16
        self.collision_sprites = collision_sprites[1]
        self.active_sprite = collision_sprites[0]
        self.fish_sprites = collision_sprites[2]
        self.visible_sprites = collision_sprites[3]
        self.door_sprites = collision_sprites[4]
        self.igloo_sprites = collision_sprites[5]
        self.limit_sprites = collision_sprites[6]
        self.demon = False
        self.glissade = False
        self.on_floor = False
        self.possibleD = True
        self.possibleG = True
        self.last_pos_on_flor = [self.rect.left, self.rect.top]

    def input(self):
        keys = pygame.key.get_pressed()

        if self.demon:
            if self.nb == 1:
                if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    self.direction.x = 1
                elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_DOWN] and self.on_floor:
                    self.direction.y = -self.jump_speed

                if keys[pygame.K_UP]:
                    self.glissade = True
                else:
                    self.glissade = False
                    if self.time != 0:
                        self.time = 0

            if self.nb == 2:
                if keys[pygame.K_q] and not keys[pygame.K_d]:
                    self.direction.x = 1
                elif keys[pygame.K_d] and not keys[pygame.K_q]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_s] and self.on_floor:
                    self.direction.y = -self.jump_speed

                if keys[pygame.K_z]:
                    self.glissade = True
                else:
                    self.glissade = False
                    if self.time != 0:
                        self.time = 0
        else:
            if self.nb == 1:
                if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                    self.direction.x = 1
                elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_UP] and self.on_floor:
                    self.direction.y = -self.jump_speed

                if keys[pygame.K_DOWN]:
                    self.glissade = True
                else:
                    self.glissade = False
                    if self.time != 0:
                        self.time = 0

            if self.nb == 2:
                if keys[pygame.K_d] and not keys[pygame.K_q]:
                    self.direction.x = 1
                elif keys[pygame.K_q] and not keys[pygame.K_d]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_z] and self.on_floor:
                    self.direction.y = -self.jump_speed

                if keys[pygame.K_s]:
                    self.glissade = True
                else:
                    self.glissade = False
                    if self.time != 0:
                        self.time = 0

    def horizontal_collisions(self):


        for sprite1 in self.fish_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                print("fish")
                sprite1.grab = True
                self.visible_sprites.remove(sprite1)
                self.collision_sprites.remove(sprite1)

        for sprite1 in self.door_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                print("door")
                for sprite2 in self.fish_sprites.sprites():
                    if sprite2.grab == True:
                        print("Open")
                        self.collision_sprites.remove(sprite1)

        for sprite1 in self.igloo_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                print("igloo")

        for sprite1 in self.collision_sprites.sprites():
            for sprite2 in self.active_sprite.sprites():
                a = False
                if sprite1.rect.colliderect(self.rect):
                    if self.direction.x < 0:
                        self.rect.left = sprite1.rect.right
                    if self.direction.x > 0:
                        self.rect.right = sprite1.rect.left
                        print("mur")
                    a = True
                if sprite2.rect.colliderect(self.rect) and not a:
                    if sprite2.rect != self.rect:
                        if self.direction.x < 0:
                            self.rect.left = sprite2.rect.right
                        if self.direction.x > 0:
                            self.rect.right = sprite2.rect.left

    def vertical_collisions(self):
        for sprite1 in self.limit_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                print("limit")
                self.rect.left = self.last_pos_on_flor[0] - 128
                self.rect.top = self.last_pos_on_flor[1]

        for sprite1 in self.fish_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                print("fish")
                sprite1.grab = True
                self.visible_sprites.remove(sprite1)
                self.collision_sprites.remove(sprite1)

        for sprite1 in self.door_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                print("door")
                for sprite2 in self.fish_sprites.sprites():
                    if sprite2.grab == True:
                        print("Open")
                        self.collision_sprites.remove(sprite1)

        for sprite1 in self.collision_sprites.sprites():
            for sprite2 in self.active_sprite.sprites():
                if sprite1.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite1.rect.top
                        self.direction.y = 0
                        self.on_floor = True
                    if self.direction.y < 0:
                        self.rect.top = sprite1.rect.bottom
                        self.direction.y = 0
                        self.on_floor = False
                if sprite2.rect.colliderect(self.rect):
                    if sprite2.rect != self.rect:
                        if self.direction.y > 0:
                            self.rect.bottom = sprite2.rect.top
                            self.direction.y = 0
                            self.on_floor = True
                        if self.direction.y < 0:
                            self.rect.top = sprite2.rect.bottom
                            self.direction.y = 0

        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        if self.direction.x < 0:
            if self.possibleG:
                if self.glissade:
                    if (self.speedG / 1.05**self.time) > 1:
                        self.rect.x += self.direction.x * (self.speedG / 1.05**self.time)
                        self.time += 1
                        self.possibleD = True
                else:
                    self.rect.x += self.direction.x * self.speed
                    self.possibleD = True
        if self.direction.x > 0:
            if self.possibleD:
                if self.glissade:
                    if (self.speedG / 1.05 ** self.time) > 1:
                        self.rect.x += self.direction.x * (self.speedG / 1.05**self.time)
                        self.time += 1
                        self.possibleG = True
                else:
                    self.rect.x += self.direction.x * self.speed
                    self.possibleG = True
        if self.on_floor:
            self.last_pos_on_flor[0] = self.rect.left
            self.last_pos_on_flor[1] = self.rect.top
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        self.update_pos()
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 8, 255])
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def get_image(self, x, y):
        image = pygame.Surface([64, 64])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 64, 64))
        return image

    def nuit(self, val):
        if val:
            self.demon = True
        else:
            self.demon = False

    def update_pos(self):
        L_PING_IMG = pygame.image.load('images\Pixel arts\Pingouins\PingouinGrisG.png')
        R_PING_IMG = pygame.image.load('images\Pixel arts\Pingouins\PingouinGris.png')
        D_L_PING_IMG = pygame.image.load('images\Pixel arts\Pingouins\PingouinGris_glisseG.png')
        D_R_PING_IMG = pygame.image.load('images\Pixel arts\Pingouins\PingouinGris_glisse.png')
        DEM_L_PING_IMG = pygame.image.load('images\Pixel arts\Pingouins\diableGrisG.png')
        DEM_R_PING_IMG = pygame.image.load('images\Pixel arts\Pingouins\DiableGris.png')
        DEM_D_L_PING_IMG = pygame.image.load('images\Pixel arts\Pingouins\diableGris_glisseG.png')
        DEM_D_R_PING_IMG = pygame.image.load('images\Pixel arts\Pingouins\diableGris_glisse.png')
        if self.demon:
            if self.glissade and self.direction != 0:
                if self.direction.x == -1:
                    self.sprite_sheet = DEM_D_L_PING_IMG
                elif self.direction.x == 1:
                    self.sprite_sheet = DEM_D_R_PING_IMG
            else:
                if self.direction.x == -1:
                    self.sprite_sheet = DEM_L_PING_IMG
                elif self.direction.x == 1:
                    self.sprite_sheet = DEM_R_PING_IMG
        else:
            if self.glissade and self.direction != 0:
                if self.direction.x == -1:
                    self.sprite_sheet = D_L_PING_IMG
                elif self.direction.x == 1:
                    self.sprite_sheet = D_R_PING_IMG
            else:
                if self.direction.x == -1:
                    self.sprite_sheet = L_PING_IMG
                elif self.direction.x == 1:
                    self.sprite_sheet = R_PING_IMG