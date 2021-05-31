import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('C:/Users/Kamil/Pictures/alien7.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.right = self.screen_rect.right
        self.y = int

    def check_edges(self):
        # Zwraca wartość True, jeśłi obcy znajduje się przy krawędzi ekranu.
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 and self.rect.top <= self.ai_settings.SCREEN_HEIGHT:
            return True
        elif self.rect.bottom >= screen_rect.height and self.rect.centery <= self.ai_settings.SCREEN_HEIGHT:
            return True

    def update(self):
        # Przesunięcie obcego w lewo
        self.y += (self.ai_settings.alien_speed_factor / self.ai_settings.fleet_direction)
        self.rect.y = self.y
