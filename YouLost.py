import pygame
import random
from Player import Character
import time
import sys
from pygame.locals import *



class YouLost():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('C:/Users/Kamil/Pictures/youlost2.png').convert_alpha()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
