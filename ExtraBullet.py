import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2
import sys
import os


class BulletPlus(Sprite):

    def __init__(self, ai_settings, screen, bosss, player, pos):

        super(BulletPlus, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.bosss = bosss
        self.image = pygame.image.load(resource_path('ExtraBullet.png')).convert_alpha()
        target = Vector2(player.rect.x, player.rect.y)

        self.rect = self.image.get_rect(center=pos)
        for boss in bosss.copy():
            self.position = Vector2(boss.rect.centerx, boss.rect.centery)
            self.rect.left = boss.rect.left
            direction = target - self.position
            self.screen_rect = screen.get_rect()
            # radius, angle = direction.as_polar()
            # self.image = pygame.transform.rotozoom(self.image, -angle, 1)
            self.velocity = direction.normalize() * 20
            self.x = float(self.rect.x)
            self.y = float(self.rect.y)

    def update(self):
        for boss in self.bosss.copy():
            # Poruszanie się pociskiem po ekranie
            self.position += self.velocity
            self.rect.center = self.position
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
