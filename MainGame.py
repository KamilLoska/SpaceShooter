import pygame
import sys
import os
from pygame.sprite import Sprite
from pygame.sprite import Group
from Settings import Settings
from Player import Character
from Alien import Alien
import Game_Functions as gf
from Bullet import Pocisk
from stars import Star
from kropla import drop
from pygame.locals import *
from Boss import boss
from BulletBoss import PociskBoss
import time
import random
from enemy import ENEMY
from Hp_Bar import HP_Bar
from pygame.math import Vector2
from YouLost import YouLost
from Animations import Explosion
from Game_stats import GameStats
from Button import Button
from Scoreboard import Scoreboard


def game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.SCREEN_WIDTH, ai_settings.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Shootin")
    player = Character(ai_settings, screen)
    # Utworzenie grupy przeznaczonej do przechowywania pocisków.
    new_bullet = Group()
    boss_bullet = Group()
    all_sprites = Group()
    aliens = Group()
    starr = Group()
    deszcz = Group()
    bosss = Group()
    enemyPlayer = Group()
    gf.create_fleet(ai_settings, screen, player, aliens)
    gf.create_fleet_drop(ai_settings, screen, player, deszcz)
    gf.create_boss(ai_settings, screen, bosss, player, boss_bullet,all_sprites)
    stats = GameStats(ai_settings)
    pause_button = Button(ai_settings, screen, "Pause")
    clock=pygame.time.Clock()
    FPS = 60
    pos = Vector2()
    HPbar = HP_Bar(ai_settings, screen, bosss)
    background = pygame.image.load('C:/Users/Kamil/Pictures/lol6.png')
    pygame.mixer.music.load('C:/Users/Kamil/Pictures/music.wav')
    pygame.mixer.music.play(-1)
    extra_bullet = Group()
    explosion = Group()
    gf.AniExplosion(explosion, bosss)
    #gf.create_bosss(ai_settings, screen, aliens, bosss, boss_bullet, new_bullet, extra_bullet, HPbar, player, explosion)
    menu = True
    menu2 = True
    loop = True
    background11 = pygame.image.load('C:/Users/Kamil/Pictures/background11.png')
    image1 = pygame.image.load('C:/Users/Kamil/Pictures/youwin2.png')
    youlost = pygame.image.load('C:/Users/Kamil/Pictures/youlost2.png')
    lost = YouLost(ai_settings, screen)
    myfont = pygame.font.SysFont("Bauhaus 93", 25)
    minutes = 0
    seconds = 0
    miliseconds = 0
    sb = Scoreboard(ai_settings, screen, stats)
    #GŁÓWNA PĘTLA GRY

    while loop:
        timelabel = myfont.render("{}:{}:{}".format(minutes, seconds, miliseconds), 1, (70, 0, 90))
        txt = myfont.render("TIME:  {}:{}:{} ".format(minutes, seconds, miliseconds), 1, (70, 0, 90))
        if miliseconds >1000:
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
                            game()
                    # miliseconds = int(float(".{}".format(miliseconds)))
                miliseconds -= miliseconds
                gf.time_txt(screen, txt, youlost)
                #clock.tick(30)
                #screen.fill((0, 0, 0))
                pygame.display.update()





        for expl in explosion:
            if HPbar.Health <=4 and expl.index >=9:
                while menu2:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_g:
                                menu2 = False
                                game()
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
            screen.fill((0,0,0))
            screen.blit(background11, (0, 0))
            pygame.display.update()
        screen.blit(background, (0, 0))
        screen.blit(timelabel, (500, 10))


        gf.check_events(ai_settings, screen, player, new_bullet, aliens, boss_bullet, bosss,all_sprites, pos, HPbar,
                        extra_bullet, explosion, stats, sb)

        if stats.game_active:

            player.update()
            new_bullet.update()
            gf.update_bullets(ai_settings, screen,stats,sb, player, new_bullet, aliens, bosss, boss_bullet, enemyPlayer, extra_bullet)
            gf.update_rain(ai_settings, deszcz)
            gf.update_aliens(ai_settings,stats,sb, screen, player, aliens, new_bullet, bosss, boss_bullet,extra_bullet, HPbar, explosion)
            boss_bullet.update()
            gf.boss_bullet_update(ai_settings, screen, boss_bullet)
            extra_bullet.update()
            gf.extra_bullet_update(ai_settings, screen, extra_bullet, player)
            gf.update_animation(explosion, bosss)
                #screen.blit(gf.time_txt(screen, txt), (510, 500))
            #if player.health <= 0 or stats.ships_left <= 0:
                #miliseconds = int(float(".{}".format(miliseconds)))
             #   miliseconds -= miliseconds
              #  gf.time_txt(screen, txt, youlost)

        gf.update_boss(ai_settings, bosss)
        gf.update_screen(ai_settings, screen, player, bosss, deszcz, aliens, starr, new_bullet, boss_bullet,
                         all_sprites, HPbar, lost, extra_bullet, explosion,stats,sb, pause_button)


        if not stats.game_active:
            miliseconds = int(float(".{}".format(miliseconds)))

        clock.tick(FPS)

#RUN GAME
game()
