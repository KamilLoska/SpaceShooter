# Exe File

import pygame
from pygame.sprite import Group
from Settings import Settings
from Player import Character
import Game_Functions as gf
from pygame.locals import *
from Hp_Bar import HP_Bar
from pygame.math import Vector2
from Game_stats import GameStats
from Button import Button
from Scoreboard import Scoreboard
import sys
import os


def main():
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.SCREEN_WIDTH, ai_settings.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Space Shooter")
    player = Character(ai_settings, screen)
    # Utworzenie grupy przeznaczonej do przechowywania pocisków.
    new_bullet = Group()
    boss_bullet = Group()
    aliens = Group()
    #deszcz = Group()
    bosss = Group()
    gf.create_fleet(ai_settings, screen, player, aliens)
    gf.create_fleet_drop(ai_settings, screen, player, deszcz)
    gf.create_boss(ai_settings, screen, bosss)
    stats = GameStats(ai_settings)
    pause_button = Button(ai_settings, screen, "Pause")
    clock = pygame.time.Clock()
    fps = 60
    pos = Vector2()
    HPbar = HP_Bar(ai_settings, screen, bosss)
    background = pygame.image.load(resource_path('lol6.png'))
    pygame.mixer.music.load(resource_path("music.wav"))
    pygame.mixer.music.play(-1)
    extra_bullet = Group()
    explosion = Group()
    menu = True
    menu2 = True
    loop = True
    background1 = pygame.image.load(resource_path('background11.png'))
    image1 = pygame.image.load(resource_path('youwin2.png'))
    youlost = pygame.image.load(resource_path('youlost2.png'))
    myfont = pygame.font.SysFont("comicsansms", 25)
    minutes = 0
    seconds = 0
    miliseconds = 0
    sb = Scoreboard(ai_settings, screen, stats)
    # GŁÓWNA PĘTLA GRY

    while loop:
        timelabel = myfont.render("{}:{}:{}".format(minutes, seconds, miliseconds), 1, (70, 0, 90))
        txt = myfont.render("TIME:  {}:{}:{} ".format(minutes, seconds, miliseconds), 1, (70, 0, 90))
        if miliseconds > 1000:
            seconds += 1
            miliseconds = 0
        miliseconds += clock.get_rawtime()
        if seconds > 60:
            minutes += 1
            seconds -= 60
        if player.health <= 0 or stats.ships_left <= 0:
            while menu2:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_g:
                            menu2 = False
                            main()
                miliseconds -= miliseconds
                gf.time_txt(screen, txt, youlost)
                pygame.display.update()
        for expl in explosion:
            if HPbar.Health <= 4 and expl.index >= 9:
                while menu2:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_g:
                                menu2 = False
                                main()
                    clock.tick(30)
                    screen.fill((0, 0, 0))
                    screen.blit(image1, (0, 0))
                    screen.blit(txt, (510, 500))
                    pygame.display.update()
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_p:
                        menu = False
            clock.tick(30)
            screen.fill((0, 0, 0))
            screen.blit(background1, (0, 0))
            pygame.display.update()
        screen.blit(background, (0, 0))
        screen.blit(timelabel, (500, 10))
        gf.check_events(ai_settings, screen, player, new_bullet, boss_bullet, bosss, pos, HPbar,
                 extra_bullet, stats)

        if stats.game_active:
            player.update()
            new_bullet.update()
            gf.update_bullets(ai_settings, stats, sb, new_bullet, aliens)
            #gf.update_rain(ai_settings, deszcz)
            gf.update_aliens(ai_settings, stats, sb, screen, player, aliens, new_bullet)
            boss_bullet.update()
            gf.boss_bullet_update(ai_settings, boss_bullet)
            extra_bullet.update()
            gf.extra_bullet_update(ai_settings, extra_bullet)
            gf.update_animation(explosion)
        gf.update_boss(ai_settings, bosss)
        gf.update_screen(ai_settings, screen, player, bosss, aliens, new_bullet, boss_bullet,
                         HPbar, extra_bullet, explosion, stats, sb, pause_button)
        if not stats.game_active:
            miliseconds = int(float(".{}".format(miliseconds)))

        clock.tick(fps)

if __name__ == '__main__':
    main()
