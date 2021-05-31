class Settings(object):
    def __init__(self):
        # Ustawienia ekranu
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 820
        self.BG_COLOR = (255, 255, 255)
        self.SZYBKOSC = 12
        # ustawienia dotyczące pocisku
        self.bullet_speed_factor = 6
        self.boss_bullet_speed_factor = -12
        self.bullet_width = 15
        self.bullet_height = 555
        self.bullets_width = 10
        self.bullets_height = 22
        self.bullet_color = (102, 255, 102)
        self.bullets_allowed = 10
        self.boss_bullets_allowed = 1
        self.extra_bullet_allowed = 0.1
        self.boss_speed_factor = 8
        self.fleet_drop_speed = 10
        self.speed_drop_rain = 1
        self.rain_direction = 10
        self.ship_limit = 3
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()
        self.alien_points = 10
        self.boss_points = 50
        self.score_scale = 1.1

    def initialize_dynamic_settings(self):

        self.alien_speed_factor = 7
        self.fleet_direction = -1

    def increase_speed(self):
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
