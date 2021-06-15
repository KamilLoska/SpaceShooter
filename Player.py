from pygame.mixer import SoundType
from pygame.sprite import Sprite
import pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
import os
import sys


class Character(Sprite):

    def __init__(self, ai_settings, screen):
        super(Character, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.hit_sound = pygame.mixer.Sound(resource_path('hit.wav'))
        self.image = pygame.image.load(resource_path('kolo5.png')).convert_alpha()
        #self.image.set_colorkey((255, 255, 255)) #FULL PRZEZROCZYSTOŚĆ OBRAZKA(USUWA TŁO)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_down = False
        self.moving_up = False
        # Każdy nowy kolo  pojawia się na lewej krawdzi ekranu
        # lewakrawedź prostokąta
        self.rect.centerx = self.screen_rect.centerx
        # gdzie ma byc ustawiony cały prostokat
        self.rect.midleft = self.screen_rect.midleft
        self.center = float(self.rect.centery)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.hitbox = (self.x, self.y, 70, 64)
        self.health = 100
        # pygame.draw.rect(self.screen, (0, 255, 0), (self.rect.x, self.rect.y - 25 , 0, 10))
        # pygame.draw.rect(self.screen, (255, 0, 0), (self.rect.x, self.rect.y, self.health, 10))

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.SZYBKOSC
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.SZYBKOSC
        self.rect.centery = self.center

    def hit(self, boss_bullet, extra_bullet):
        for naboje in boss_bullet:
            if self.rect.x < naboje.rect.x < self.rect.x + 50 and self.rect.y < naboje.rect.y < self.rect.y + 80:
                self.health -= 5
                self.hit_sound.play()
                boss_bullet.remove(naboje)
        for bullet in extra_bullet:
            if pygame.sprite.collide_mask(self, bullet):
                self.health -= 10
                self.hit_sound.play()

    def blitme(self, HPbar, screen):
        # Wyswietlanie gracza i paska HP w jego akutalnym położeniu
        self.hitbox = (self.rect.x, self.rect.y, 70 + 18, 64 + 5)
        self.screen.blit(self.image, self.rect)
        if self.health >= 0 and HPbar.Health >= 0:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.rect.x + 4, self.rect.y - 25, 100, 10))
            pygame.draw.rect(self.screen, (0, 255, 0), (self.rect.x + 4, self.rect.y - 25, self.health, 10))
        if self.health <= 0:
            pygame.draw.rect(self.screen, ((255, 255, 255)), (self.rect.x + 4, self.rect.y - 25, 0, 0))

    def player_center(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.midleft = self.screen_rect.midleft


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
