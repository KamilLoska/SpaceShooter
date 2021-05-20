import pygame
from Alien import Alien
import random
from BulletBoss import PociskBoss
from pygame.sprite import Sprite
from pygame.sprite import Group


class boss(Sprite):

    def __init__(self, ai_settings, screen, bosss, koloo, boss_bullet, all_sprites):
        super(boss, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('C:/Users/Kamil/Pictures/boss1.png').convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.right = self.screen_rect.right #set rect of object on right site of screen
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

    def update(self,new_bullet, hpbar):
        #Przesunięcie obcego na górę i dół
        self.y -= (self.ai_settings.boss_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.y = self.y

    def check_edges(self):
        # Zwraca wartość True, jeśłi obcy znajduje się przy krawędzi ekranu.
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.top:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True
