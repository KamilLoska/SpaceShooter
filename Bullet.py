
import pygame
from pygame.sprite import Sprite


class Pocisk(Sprite):
    def __init__(self, ai_settings, screen, player):
        super(Pocisk, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect2 = pygame.Rect(0, 0, ai_settings.bullets_width, ai_settings.bullets_height)
        self.rect.center = player.rect.center
        self.rect.right = player.rect.right

        # Położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej
        self.x = float(self.rect.x)
        self.x = float(self.rect2.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # Poruszanie pociskiem po ekranie
        self.x = self.speed_factor
        self.rect.x += self.x

    def draw_pocisk(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
