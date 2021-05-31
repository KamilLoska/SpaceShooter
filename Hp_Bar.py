import pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)


class HP_Bar(object):

    def __init__(self, ai_settings, screen, bosss):

        super(HP_Bar, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.Surface((75, 25)).convert_alpha()
        self.screen_rect = screen.get_rect()
        self.Health = 180

    def hit(self, bosss, new_bullet, boss_bullet, ai_settings, extra_bullet):

        for boss in bosss.sprites():
            for naboje in new_bullet.sprites():
                if boss.rect.x < naboje.rect.x < boss.rect.x + 150 and boss.rect.y < naboje.rect.y < boss.rect.y + 200:
                    self.hit_sound = pygame.mixer.Sound('C:/Users/Kamil/Pictures/hitboss.wav')
                    self.Health -= 5
                    self.hit_sound.play()
                    new_bullet.remove(naboje)

    def blitme(self, bosss):

        if self.Health >= 0:
            for bosik in bosss:
                pygame.draw.rect(self.screen, (255, 0, 0), (bosik.rect.x + 3, bosik.rect.y - 35, 180, 15))
                pygame.draw.rect(self.screen, (0, 255, 0), (bosik.rect.x + 3, bosik.rect.y - 35, self.Health, 15))
