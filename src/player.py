import pygame, sys
from settings import *
from color import Color
from timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, nb, couleur):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load('images\Pixel arts\Pingouins\PingouinGris.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 8, 255])
        self.rect = self.image.get_rect(topleft=pos)
        self.colors = Color(couleur)
        self.L_PING_IMG = self.colors.table[0]
        self.R_PING_IMG = self.colors.table[1]
        self.S_L_PING_IMG = self.colors.table[2]
        self.S_R_PING_IMG = self.colors.table[3]
        self.D_L_PING_IMG = self.colors.table[4]
        self.D_R_PING_IMG = self.colors.table[5]
        self.DEM_L_PING_IMG = self.colors.table[6]
        self.DEM_R_PING_IMG = self.colors.table[7]
        self.DEM_S_L_PING_IMG = self.colors.table[8]
        self.DEM_S_R_PING_IMG = self.colors.table[9]
        self.DEM_D_L_PING_IMG = self.colors.table[10]
        self.DEM_D_R_PING_IMG = self.colors.table[11]
        self.SUP_L_PING_IMG = self.colors.table[12]
        self.SUP_R_PING_IMG = self.colors.table[13]
        self.SUP_D_L_PING_IMG = self.colors.table[14]
        self.SUP_D_R_PING_IMG = self.colors.table[15]
        self.SUP_S_L_PING_IMG = self.colors.table[16]
        self.SUP_S_R_PING_IMG = self.colors.table[17]
        self.HOM_L_PING_IMG = self.colors.table[18]
        self.HOM_R_PING_IMG = self.colors.table[19]
        self.HOM_S_L_PING_IMG = self.colors.table[20]
        self.HOM_S_R_PING_IMG = self.colors.table[21]
        self.HOM_D_L_PING_IMG = self.colors.table[22]
        self.HOM_D_R_PING_IMG = self.colors.table[23]

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
        self.mask_sprites = collision_sprites[7]
        self.bloc_sprites = collision_sprites[8]
        self.homard_sprites = collision_sprites[9]
        self.bloc_break_sprites = collision_sprites[10]
        self.homard = False
        self.super = False
        self.demon = False
        self.glissade = False
        self.on_floor = False
        self.possibleD = True
        self.possibleG = True
        self.contre_bloc = False
        self.last_pos_on_flor = [self.rect.left, self.rect.top]
        self.time_in_pos = 0
        self.last_pos = self.sprite_sheet

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
            elif self.nb == 3:
                if keys[pygame.K_j] and not keys[pygame.K_l]:
                    self.direction.x = 1
                elif keys[pygame.K_l] and not keys[pygame.K_j]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_k] and self.on_floor:
                    self.direction.y = -self.jump_speed

                if keys[pygame.K_i]:
                    self.glissade = True
                else:
                    self.glissade = False
                    if self.time != 0:
                        self.time = 0
            elif self.nb == 4:
                if keys[pygame.K_KP4] and not keys[pygame.K_KP6]:
                    self.direction.x = 1
                elif keys[pygame.K_KP6] and not keys[pygame.K_KP4]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_KP5] and self.on_floor:
                    self.direction.y = -self.jump_speed

                if keys[pygame.K_KP8]:
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
            elif self.nb == 2:
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
            elif self.nb == 3:
                if keys[pygame.K_l] and not keys[pygame.K_j]:
                    self.direction.x = 1
                elif keys[pygame.K_j] and not keys[pygame.K_l]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_i] and self.on_floor:
                    self.direction.y = -self.jump_speed

                if keys[pygame.K_k]:
                    self.glissade = True
                else:
                    self.glissade = False
                    if self.time != 0:
                        self.time = 0
            elif self.nb == 4:
                if keys[pygame.K_KP6] and not keys[pygame.K_KP4]:
                    self.direction.x = 1
                elif keys[pygame.K_KP4] and not keys[pygame.K_KP6]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_KP8] and self.on_floor:
                    self.direction.y = -self.jump_speed

                if keys[pygame.K_KP5]:
                    self.glissade = True
                else:
                    self.glissade = False
                    if self.time != 0:
                        self.time = 0

    def horizontal_collisions(self):
        if self.homard:
            for sprite1 in self.bloc_break_sprites.sprites():
                if sprite1.rect.colliderect(self.rect):
                    print("cassé")
                    self.visible_sprites.remove(sprite1)
                    self.collision_sprites.remove(sprite1)
                    self.bloc_break_sprites.remove(sprite1)

        for sprite1 in self.bloc_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    possible = sprite1.collision(True, self, self.collision_sprites, self.active_sprite)
                    if possible:
                        print("oui")
                        sprite1.rect.right = self.rect.left
                        self.contre_bloc = False
                    else:
                        self.rect.left = sprite1.rect.right
                        self.contre_bloc = True
                if self.direction.x > 0:
                    possible = sprite1.collision(True, self, self.collision_sprites, self.active_sprite)
                    if possible:
                        print("oui")
                        sprite1.rect.left = self.rect.right
                        self.contre_bloc = False
                    else:
                        self.rect.right = sprite1.rect.left
                        self.contre_bloc = True
                else:
                    self.contre_bloc = True
            else:
                self.contre_bloc = False

        if not self.homard:
            for sprite1 in self.mask_sprites.sprites():
                if sprite1.rect.colliderect(self.rect):
                    print("mask")
                    sprite1.grab = True
                    if self.nb == 1:
                        sprite1.nb = 1
                    elif self.nb == 2:
                        sprite1.nb = 2
                    elif self.nb == 3:
                        sprite1.nb = 3
                    elif self.nb == 4:
                        sprite1.nb = 4
                    self.visible_sprites.remove(sprite1)
                    self.mask_sprites.remove(sprite1)

        if not self.super:
            for sprite1 in self.homard_sprites.sprites():
                if sprite1.rect.colliderect(self.rect):
                    print("homard")
                    sprite1.grab = True
                    if self.nb == 1:
                        sprite1.nb = 1
                    elif self.nb == 2:
                        sprite1.nb = 2
                    elif self.nb == 3:
                        sprite1.nb = 3
                    elif self.nb == 4:
                        sprite1.nb = 4
                    self.visible_sprites.remove(sprite1)
                    self.homard_sprites.remove(sprite1)

        for sprite1 in self.fish_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                print("fish")
                sprite1.grab = True
                self.visible_sprites.remove(sprite1)
                self.collision_sprites.remove(sprite1)

        for sprite1 in self.door_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                for sprite2 in self.fish_sprites.sprites():
                    if sprite2.grab == True:
                        self.collision_sprites.remove(sprite1)

        for sprite1 in self.igloo_sprites.sprites():
            if sprite1.rect.colliderect(self.rect):
                print("colliderect return")
                return 5

        for sprite1 in self.collision_sprites.sprites():
            for sprite2 in self.active_sprite.sprites():
                a = False
                if sprite1.rect.colliderect(self.rect):
                    if self.direction.x < 0:
                        self.rect.left = sprite1.rect.right
                    if self.direction.x > 0:
                        self.rect.right = sprite1.rect.left
                    a = True
                if sprite2.rect.colliderect(self.rect) and not a:
                    if sprite2.rect != self.rect:
                        if self.direction.x < 0:
                            self.rect.left = sprite2.rect.right
                        if self.direction.x > 0:
                            self.rect.right = sprite2.rect.left


    def vertical_collisions(self):
        if self.homard:
            for sprite1 in self.bloc_break_sprites.sprites():
                if sprite1.rect.colliderect(self.rect):
                    print("cassé")
                    self.visible_sprites.remove(sprite1)
                    self.collision_sprites.remove(sprite1)
                    self.bloc_break_sprites.remove(sprite1)

        if not self.contre_bloc:
            for sprite1 in self.bloc_sprites.sprites():
                if sprite1.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        print("tp")
                        self.rect.bottom = sprite1.rect.top
                        self.direction.y = 0
                        self.on_floor = True
                    if self.direction.y < 0:
                        self.rect.top = sprite1.rect.bottom
                        self.direction.y = 0
                        self.on_floor = False

        if not self.homard:
            for sprite1 in self.mask_sprites.sprites():
                if sprite1.rect.colliderect(self.rect):
                    print("mask")
                    sprite1.grab = True
                    if self.nb == 1:
                        sprite1.nb = 1
                    elif self.nb == 2:
                        sprite1.nb = 2
                    elif self.nb == 3:
                        sprite1.nb = 3
                    elif self.nb == 4:
                        sprite1.nb = 4
                    self.visible_sprites.remove(sprite1)
                    self.mask_sprites.remove(sprite1)

        if not self.super:
            for sprite1 in self.homard_sprites.sprites():
                if sprite1.rect.colliderect(self.rect):
                    print("homard")
                    sprite1.grab = True
                    if self.nb == 1:
                        sprite1.nb = 1
                    elif self.nb == 2:
                        sprite1.nb = 2
                    elif self.nb == 3:
                        sprite1.nb = 3
                    elif self.nb == 4:
                        sprite1.nb = 4
                    self.visible_sprites.remove(sprite1)
                    self.homard_sprites.remove(sprite1)

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
                for sprite2 in self.fish_sprites.sprites():
                    if sprite2.grab == True:
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
                    if (self.speedG / 1.05 ** self.time) > 1:
                        self.rect.x += self.direction.x * (self.speedG / 1.05 ** self.time)
                        self.time += 1
                        self.possibleD = True
                else:
                    self.rect.x += self.direction.x * self.speed
                    self.possibleD = True
        if self.direction.x > 0:
            if self.possibleD:
                if self.glissade:
                    if (self.speedG / 1.05 ** self.time) > 1:
                        self.rect.x += self.direction.x * (self.speedG / 1.05 ** self.time)
                        self.time += 1
                        self.possibleG = True
                else:
                    self.rect.x += self.direction.x * self.speed
                    self.possibleG = True
        if self.on_floor:
            self.last_pos_on_flor[0] = self.rect.left
            self.last_pos_on_flor[1] = self.rect.top
        if self.horizontal_collisions() == 5:
            print("rreturn LE 2")
            return 5
        self.apply_gravity()
        self.vertical_collisions()
        self.update_pos()
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 8, 255])
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        return 0


    def get_image(self, x, y):
        image = pygame.Surface([64, 64])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 64, 64))
        return image

    def nuit(self, val):
        if not self.super and not self.homard:
            if val:
                self.demon = True
            else:
                self.demon = False

    def super_hero(self, val):
        self.demon = False
        if val:
            self.super = True
            self.speed = self.speed * 1.3
            self.speedG = self.speedG * 1.3
            self.gravity = self.gravity * 0.6
        else:
            self.super = False
            self.speed = self.speed / 1.3
            self.speedG = self.speedG / 1.3
            self.gravity = self.gravity / 0.6

    def set_homard(self, val):
        self.demon = False
        if val:
            self.homard = True
        else:
            self.homard = False

    def update_pos(self):
        if self.last_pos == self.sprite_sheet:
            self.time_in_pos += 1
            if self.time_in_pos == 20:
                self.time_in_pos = 0
        else:
            self.time_in_pos = 0
        if self.super:
            if self.glissade and self.direction.x != 0:
                if self.direction.x == -1:
                    self.sprite_sheet = self.SUP_D_L_PING_IMG
                elif self.direction.x == 1:
                    self.sprite_sheet = self.SUP_D_R_PING_IMG
            else:
                if self.direction.y > 1 or self.direction.y < 0:
                    if self.direction.x == -1:
                        self.sprite_sheet = self.SUP_S_L_PING_IMG
                    elif self.direction.x == 1:
                        self.sprite_sheet = self.SUP_S_R_PING_IMG
                    else:
                        if self.sprite_sheet == self.S_L_PING_IMG or self.sprite_sheet == self.D_L_PING_IMG or self.sprite_sheet == self.L_PING_IMG or self.sprite_sheet == self.DEM_S_L_PING_IMG or self.sprite_sheet == self.DEM_D_L_PING_IMG or self.sprite_sheet == self.DEM_L_PING_IMG or self.sprite_sheet == self.SUP_S_L_PING_IMG or self.sprite_sheet == self.SUP_D_L_PING_IMG or self.sprite_sheet == self.SUP_L_PING_IMG:
                            self.sprite_sheet = self.SUP_S_L_PING_IMG
                        else:
                            self.sprite_sheet = self.SUP_S_R_PING_IMG
                else:
                    if self.direction.x == -1:
                        if 0 <= self.time_in_pos < 10:
                            self.sprite_sheet = self.SUP_S_L_PING_IMG
                        else:
                            self.sprite_sheet = self.SUP_L_PING_IMG
                    elif self.direction.x == 1:
                        if 0 <= self.time_in_pos < 10:
                            self.sprite_sheet = self.SUP_S_R_PING_IMG
                        else:
                            self.sprite_sheet = self.SUP_R_PING_IMG
                    else:
                        if self.sprite_sheet == self.S_L_PING_IMG or self.sprite_sheet == self.D_L_PING_IMG or self.sprite_sheet == self.L_PING_IMG or self.sprite_sheet == self.DEM_S_L_PING_IMG or self.sprite_sheet == self.DEM_D_L_PING_IMG or self.sprite_sheet == self.DEM_L_PING_IMG or self.sprite_sheet == self.SUP_S_L_PING_IMG or self.sprite_sheet == self.SUP_D_L_PING_IMG or self.sprite_sheet == self.SUP_L_PING_IMG:
                            self.sprite_sheet = self.SUP_L_PING_IMG
                        else:
                            self.sprite_sheet = self.SUP_R_PING_IMG
        elif self.homard:
            if self.glissade and self.direction.x != 0:
                if self.direction.x == -1:
                    self.sprite_sheet = self.HOM_D_L_PING_IMG
                elif self.direction.x == 1:
                    self.sprite_sheet = self.HOM_D_R_PING_IMG
            else:
                if self.direction.y > 1 or self.direction.y < 0:
                    if self.direction.x == -1:
                        self.sprite_sheet = self.HOM_S_L_PING_IMG
                    elif self.direction.x == 1:
                        self.sprite_sheet = self.HOM_S_R_PING_IMG
                    else:
                        if self.sprite_sheet == self.S_L_PING_IMG or self.sprite_sheet == self.D_L_PING_IMG or self.sprite_sheet == self.L_PING_IMG \
                                or self.sprite_sheet == self.DEM_S_L_PING_IMG or self.sprite_sheet == self.DEM_D_L_PING_IMG or self.sprite_sheet == self.DEM_L_PING_IMG \
                                or self.sprite_sheet == self.SUP_S_L_PING_IMG or self.sprite_sheet == self.SUP_D_L_PING_IMG or self.sprite_sheet == self.SUP_L_PING_IMG \
                                or self.sprite_sheet == self.HOM_S_L_PING_IMG or self.sprite_sheet == self.HOM_D_L_PING_IMG or self.sprite_sheet == self.HOM_L_PING_IMG:
                            self.sprite_sheet = self.HOM_S_L_PING_IMG
                        else:
                            self.sprite_sheet = self.HOM_S_R_PING_IMG
                else:
                    if self.direction.x == -1:
                        if 0 <= self.time_in_pos < 10:
                            self.sprite_sheet = self.HOM_S_L_PING_IMG
                        else:
                            self.sprite_sheet = self.HOM_L_PING_IMG
                    elif self.direction.x == 1:
                        if 0 <= self.time_in_pos < 10:
                            self.sprite_sheet = self.HOM_S_R_PING_IMG
                        else:
                            self.sprite_sheet = self.HOM_R_PING_IMG
                    else:
                        if self.sprite_sheet == self.S_L_PING_IMG or self.sprite_sheet == self.D_L_PING_IMG or self.sprite_sheet == self.L_PING_IMG \
                                or self.sprite_sheet == self.DEM_S_L_PING_IMG or self.sprite_sheet == self.DEM_D_L_PING_IMG or self.sprite_sheet == self.DEM_L_PING_IMG \
                                or self.sprite_sheet == self.SUP_S_L_PING_IMG or self.sprite_sheet == self.SUP_D_L_PING_IMG or self.sprite_sheet == self.SUP_L_PING_IMG \
                                or self.sprite_sheet == self.HOM_S_L_PING_IMG or self.sprite_sheet == self.HOM_D_L_PING_IMG or self.sprite_sheet == self.HOM_L_PING_IMG:
                            self.sprite_sheet = self.HOM_L_PING_IMG
                        else:
                            self.sprite_sheet = self.HOM_R_PING_IMG
        elif self.demon:
            if self.glissade and self.direction.x != 0:
                if self.direction.x == -1:
                    self.sprite_sheet = self.DEM_D_L_PING_IMG
                elif self.direction.x == 1:
                    self.sprite_sheet = self.DEM_D_R_PING_IMG
            else:
                if self.direction.y > 1 or self.direction.y < 0:
                    if self.direction.x == -1:
                        self.sprite_sheet = self.DEM_S_L_PING_IMG
                    elif self.direction.x == 1:
                        self.sprite_sheet = self.DEM_S_R_PING_IMG
                    else:
                        if self.sprite_sheet == self.S_L_PING_IMG or self.sprite_sheet == self.D_L_PING_IMG or self.sprite_sheet == self.L_PING_IMG \
                                or self.sprite_sheet == self.DEM_S_L_PING_IMG or self.sprite_sheet == self.DEM_D_L_PING_IMG or self.sprite_sheet == self.DEM_L_PING_IMG \
                                or self.sprite_sheet == self.SUP_S_L_PING_IMG or self.sprite_sheet == self.SUP_D_L_PING_IMG or self.sprite_sheet == self.SUP_L_PING_IMG \
                                or self.sprite_sheet == self.HOM_S_L_PING_IMG or self.sprite_sheet == self.HOM_D_L_PING_IMG or self.sprite_sheet == self.HOM_L_PING_IMG:
                            self.sprite_sheet = self.DEM_S_L_PING_IMG
                        else:
                            self.sprite_sheet = self.DEM_S_R_PING_IMG
                else:
                    if self.direction.x == -1:
                        if 0 <= self.time_in_pos < 10:
                            self.sprite_sheet = self.DEM_S_L_PING_IMG
                        else:
                            self.sprite_sheet = self.DEM_L_PING_IMG
                    elif self.direction.x == 1:
                        if 0 <= self.time_in_pos < 10:
                            self.sprite_sheet = self.DEM_S_R_PING_IMG
                        else:
                            self.sprite_sheet = self.DEM_R_PING_IMG
                    else:
                        if self.sprite_sheet == self.S_L_PING_IMG or self.sprite_sheet == self.D_L_PING_IMG or self.sprite_sheet == self.L_PING_IMG \
                                or self.sprite_sheet == self.DEM_S_L_PING_IMG or self.sprite_sheet == self.DEM_D_L_PING_IMG or self.sprite_sheet == self.DEM_L_PING_IMG \
                                or self.sprite_sheet == self.SUP_S_L_PING_IMG or self.sprite_sheet == self.SUP_D_L_PING_IMG or self.sprite_sheet == self.SUP_L_PING_IMG \
                                or self.sprite_sheet == self.HOM_S_L_PING_IMG or self.sprite_sheet == self.HOM_D_L_PING_IMG or self.sprite_sheet == self.HOM_L_PING_IMG:
                            self.sprite_sheet = self.DEM_L_PING_IMG
                        else:
                            self.sprite_sheet = self.DEM_R_PING_IMG
        else:
            if self.glissade and self.direction.x != 0:
                if self.direction.x == -1:
                    self.sprite_sheet = self.D_L_PING_IMG
                elif self.direction.x == 1:
                    self.sprite_sheet = self.D_R_PING_IMG
            else:
                if self.direction.y > 1 or self.direction.y < 0:
                    if self.direction.x == -1:
                        self.sprite_sheet = self.S_L_PING_IMG
                    elif self.direction.x == 1:
                        self.sprite_sheet = self.S_R_PING_IMG
                    else:
                        if self.sprite_sheet == self.S_L_PING_IMG or self.sprite_sheet == self.D_L_PING_IMG or self.sprite_sheet == self.L_PING_IMG \
                                or self.sprite_sheet == self.DEM_S_L_PING_IMG or self.sprite_sheet == self.DEM_D_L_PING_IMG or self.sprite_sheet == self.DEM_L_PING_IMG \
                                or self.sprite_sheet == self.SUP_S_L_PING_IMG or self.sprite_sheet == self.SUP_D_L_PING_IMG or self.sprite_sheet == self.SUP_L_PING_IMG \
                                or self.sprite_sheet == self.HOM_S_L_PING_IMG or self.sprite_sheet == self.HOM_D_L_PING_IMG or self.sprite_sheet == self.HOM_L_PING_IMG:
                            self.sprite_sheet = self.S_L_PING_IMG
                        else:
                            self.sprite_sheet = self.S_R_PING_IMG
                else:
                    if self.direction.x == -1:
                        if 0 <= self.time_in_pos < 10:
                            self.sprite_sheet = self.S_L_PING_IMG
                        else:
                            self.sprite_sheet = self.L_PING_IMG
                    elif self.direction.x == 1:
                        if 0 <= self.time_in_pos < 10:
                            self.sprite_sheet = self.S_R_PING_IMG
                        else:
                            self.sprite_sheet = self.R_PING_IMG
                    else:
                        if self.sprite_sheet == self.S_L_PING_IMG or self.sprite_sheet == self.D_L_PING_IMG or self.sprite_sheet == self.L_PING_IMG \
                                or self.sprite_sheet == self.DEM_S_L_PING_IMG or self.sprite_sheet == self.DEM_D_L_PING_IMG or self.sprite_sheet == self.DEM_L_PING_IMG \
                                or self.sprite_sheet == self.SUP_S_L_PING_IMG or self.sprite_sheet == self.SUP_D_L_PING_IMG or self.sprite_sheet == self.SUP_L_PING_IMG \
                                or self.sprite_sheet == self.HOM_S_L_PING_IMG or self.sprite_sheet == self.HOM_D_L_PING_IMG or self.sprite_sheet == self.HOM_L_PING_IMG:
                            self.sprite_sheet = self.L_PING_IMG
                        else:
                            self.sprite_sheet = self.R_PING_IMG
        self.last_pos = self.sprite_sheet
