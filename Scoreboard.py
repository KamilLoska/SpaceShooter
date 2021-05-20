import pygame.font
from pygame.sprite import Group
from Player import Character

class Scoreboard():


    def __init__(self, ai_settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #Ustawienie koloru czcionki i czcionki
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 49)
        self.font2 = pygame.font.SysFont(None, 30)
        self.prep_ships()
        self.prep_score()


    def prep_score(self):
    #Przeksztalcenie punktacji w obraz

        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.BG_COLOR)
        self.score_image.set_colorkey((255, 255, 255, 255))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.bottom = self.screen_rect.bottom - 10
        self.score_rect_top = 20


        self.pausetxt = self.font2.render("Click 'z' to pause", True, self.text_color, self.ai_settings.BG_COLOR)
        self.pausetxt.set_colorkey((255, 255, 255, 255))
        self.pause_rect = self.pausetxt.get_rect()
        self.pause_rect.center = (90,30)

        level_str = str(self.stats.level)
        self.leveltxt = self.font2.render("level: " + level_str, True, self.text_color, self.ai_settings.BG_COLOR)
        self.leveltxt.set_colorkey((255, 255, 255, 255))
        self.level_rect = self.leveltxt.get_rect()
        self.level_rect.bottom = self.screen_rect.bottom - 60


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.pausetxt, self.pause_rect)
        self.screen.blit(self.leveltxt, self.level_rect)
        self.ships.draw(self.screen)


    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Character(self.ai_settings, self.screen)
            ship.rect.x = 2 + ship_number * ship.rect.width / 2
            ship.rect.y = 2
            ship.rect.x += 200
            ship.rect.y += 12
            ship.image = pygame.transform.scale(ship.image, (40, 40))

            self.ships.add(ship)
