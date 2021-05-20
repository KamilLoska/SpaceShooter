import pygame
from pygame.sprite import Sprite
import random
from pygame.math import Vector2


class PociskBoss(Sprite):

    def __init__(self, ai_settings, screen, bosss, koloo, pos):

        super(PociskBoss, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('C:/Users/Kamil/Pictures/bossbullet.png').convert_alpha()
        self.image = pygame.Surface([8, 5])
        pygame.Surface.fill(self.image, (255, 31, 31))
        target = Vector2(koloo.rect.centerx, koloo.rect.centery)
        self.rect = self.image.get_rect(center = pos)
        for boss in bosss.sprites():
            self.position = Vector2(boss.rect.centerx, boss.rect.centery)
            self.rect.center = boss.rect.center
            self.rect.left = boss.rect.left
            direction = target - self.position
            self.screen_rect = screen.get_rect()
            radius, angle = direction.as_polar()
            self.image = pygame.transform.rotozoom(self.image, -angle, 1)
            self.velocity = direction.normalize() *14
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
    def update(self, bosss):
        # Poruszanie pociskiem po ekranie
        for boss in bosss.copy():
            self.position += self.velocity  # Update the position vector
            self.rect.center = self.position
