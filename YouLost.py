import pygame
import sys
import os


class YouLost(object):

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(resource_path('youlost2.png')).convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
