import pygame
from pygame.sprite import Sprite
import random
from pygame.math import Vector2


class BulletPlus(Sprite):

    def __init__(self, ai_settings, screen, bosss, player, pos):

        super(BulletPlus, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('C:/Users/Kamil/Pictures/ExtraBullet.png').convert_alpha()
        target = Vector2(player.rect.x, player.rect.y)

        self.rect = self.image.get_rect(center = pos)
        for boss in bosss.copy():
            self.position = Vector2(boss.rect.centerx, boss.rect.centery)
            self.rect.left = boss.rect.left
            direction = target - self.position
            self.screen_rect = screen.get_rect()
            radius, angle = direction.as_polar()
            #self.image = pygame.transform.rotozoom(self.image, -angle, 1)
            self.velocity = direction.normalize() *20
            self.x = float(self.rect.x)
            self.y = float(self.rect.y)
    def update(self,bosss):
        for boss in bosss.copy():
        #moving bullet
            self.position += self.velocity  #Update the position vector
            self.rect.center = self.position
