import pygame
from pygame.sprite import Sprite
import sys
import os


class Explosion(Sprite):
    def __init__(self, bosss):
        super(Explosion, self).__init__()
        self.images = []
        self.bosss = bosss

        for num in range(10):
            img = pygame.image.load(resource_path(f"animations/ani{num}.png")).convert_alpha()
            img = pygame.transform.scale(img, (200, 200))
            if num > 5:
                img = pygame.transform.scale(img,  (0, 0))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        for boss in bosss.copy():
            rect = bosss.sprites()[0].rect
            self.rect.center = rect.center
        self.counter = 0

    def update(self):
        for boss in self.bosss:
            rect = boss.rect.x
            self.rect.center = boss.rect.center
        explosion_speed = 4
        self.counter += 1


        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
