import sys
import pygame
from Bullet import Pocisk
from Alien import Alien
from kropla import drop
from Boss import boss
from BulletBoss import PociskBoss
from time import sleep
from ExtraBullet import BulletPlus
from Animations import Explosion
clock = pygame.time.Clock()
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)


def update_bullets(ai_settings, stats, sb, new_bullet, aliens):
    new_bullet.update()
    # Usunięcie pocisków, które znajdują się poza ekranem
    for bullet in new_bullet.copy():
        if bullet.rect.left <= 0 or ai_settings.SCREEN_WIDTH < bullet.rect.right:
            new_bullet.remove(bullet)
    collisions = pygame.sprite.groupcollide(new_bullet, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()


def boss_bullet_update(ai_settings, boss_bullet):
    boss_bullet.update()
    for bullet in boss_bullet.copy():
        if bullet.rect.left <= 0 or ai_settings.SCREEN_WIDTH < bullet.rect.left:
            boss_bullet.remove(bullet)


def extra_bullet_update(ai_settings, extra_bullet):
    extra_bullet.update()
    for bullets in extra_bullet.copy():
        if bullets.rect.right <= 0 or ai_settings.SCREEN_WIDTH < bullets.rect.left:
            extra_bullet.remove(bullets)


def check_keydown_events(event, ai_settings, screen, player, new_bullet, stats):
    if event.key == pygame.K_ESCAPE:
        sys.exit(0)
    if event.key == pygame.K_DOWN and player.rect.bottom < player.screen_rect.bottom:
        player.moving_down = True
    if event.key == pygame.K_UP and player.rect.top > 0:
        player.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, player, new_bullet)
    elif event.key == pygame.K_z:
        stats.game_active = not stats.game_active


def fire_bullet(ai_settings, screen, player, new_bullet):
    # wystrzelenie nowego pociskuu, jeżeli nie przekroczono określonego limitu - 3 kul
    shoot_sound = pygame.mixer.Sound('C:/Users/Kamil/Pictures/hit2.wav')
    if len(new_bullet) <= ai_settings.bullets_allowed and len(new_bullet) < ai_settings.SCREEN_WIDTH:
        bullets = Pocisk(ai_settings, screen, player)
        new_bullet.add(bullets)
        shoot_sound.play()


def fire_boss_bullet(ai_settings, screen, bosss, boss_bullet, player, pos, HPbar):
    if len(boss_bullet) <= ai_settings.boss_bullets_allowed:
        bullet = PociskBoss(ai_settings, screen, bosss, player, pos)
        boss_bullet.add(bullet)
        if HPbar.Health < 0:
            bullet.kill()


def fire_extra_bullet(ai_settings, screen, bosss, player, pos, extra_bullet, HPbar):
    # fire_extra = pygame.mixer.Sound('C:/Users/Kamil/Pictures/hit2.wav')
    if len(extra_bullet) <= float(ai_settings.extra_bullet_allowed):
        extrabullet = BulletPlus(ai_settings, screen, bosss, player, pos)
        extra_bullet.add(extrabullet)
        if HPbar.Health < 0:
            extrabullet.kill()


def AniExplosion(explosion, bosss):
    animation = Explosion(bosss)
    explosion.add(animation)


def check_keyup_events(event, player):
    if event.key == pygame.K_DOWN:
        player.moving_down = False
    if event.key == pygame.K_UP:
        player.moving_up = False


def check_events(ai_settings, screen, player, new_bullet, boss_bullet, bosss, pos, HPbar,
                 extra_bullet, stats):
    milliseconds_delay = 1200  # 0.5 seconds
    bullet_event = pygame.USEREVENT + 1
    pygame.time.set_timer(bullet_event, milliseconds_delay // 60)
    milliseconds_delay2 = 1850
    bullet_event2 = pygame.USEREVENT + 2
    pygame.time.set_timer(bullet_event2, milliseconds_delay2 // 60)

    # Oczekiwwanie na nacisniecie klawisza lub przycisku myszy
    for event in pygame.event.get():
        pygame.time.set_timer(bullet_event, milliseconds_delay)
        pygame.time.set_timer(bullet_event2, milliseconds_delay2)

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, player, new_bullet, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)
        elif event.type == bullet_event:
            fire_boss_bullet(ai_settings, screen, bosss, boss_bullet, player, pos, HPbar)
        elif event.type == bullet_event2:
            fire_extra_bullet(ai_settings, screen, bosss, player, pos, extra_bullet, HPbar)


def get_number_rows(ai_settings, player_width, alien_width):
    # Ustalenie, ile rzędów obcych zmieści się na ekranie.
    available_space_y = (ai_settings.SCREEN_HEIGHT -
                         (4 * alien_width) - player_width)
    number_rows = int(available_space_y / (2 * alien_width))
    return number_rows


def get_number_rain(ai_settings, player_width, kropla_height):
    available_space_y = (ai_settings.SCREEN_HEIGHT -
                         (3 * kropla_height) - player_width)
    number_rows = int(available_space_y / (128 * kropla_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    # Ustalenie liczby obcych, którzy zmieszczą się w rzędzie
    available_space_x = ai_settings.SCREEN_HEIGHT - 2 / alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_randomnumber_rain(ai_settings, kropla_height):
    available_space_rain = ai_settings.SCREEN_WIDTH - 3 / kropla_height
    number_rain_x = int(available_space_rain / (3 * kropla_height))
    return number_rain_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_height = alien.rect.height
    alien.y = alien_height + 2.5 * alien_height * alien_number
    alien.rect.y = alien.y
    alien.rect.x -= alien.rect.width + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_boss(ai_settings, screen, bosss, player, boss_bullet, all_sprites):
    Boss = boss(ai_settings, screen, bosss, player, boss_bullet, all_sprites)
    boss_height = Boss.rect.height
    Boss.y = boss_height
    Boss.rect.y = Boss.y
    bosss.add(Boss)


def create_fleet(ai_settings, screen, player, aliens):
    # Utworzenie pełnej floty obcych statków.
    # Utworzenie obcego i ustalenie liczby obcych, którzy zmieszczą się w rzędzie.
    # Odległość między poszczególnymi obcymi jest równa długośći obcego.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, player.rect.height,
                                  alien.rect.width)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Utworzenie nowego obcego i umieszczenie go w rzędzie.
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


def create_fleet_drop(ai_settings, screen, player, deszcz):
    kropla = drop(ai_settings, screen)
    number_rain_x = get_randomnumber_rain(ai_settings, kropla.rect.width)
    number_rows_rain = get_number_rain(ai_settings, player.rect.width,
                                       kropla.rect.width)

    for rownumberss in range(number_rows_rain):
        for rain_number in range(number_rain_x):
            create_rain(ai_settings, screen, deszcz, rain_number,
                        rownumberss)


def create_rain(ai_settings, screen, deszcz, rain_number, rownumberss):
    kropla = drop(ai_settings, screen)
    kropla_width = kropla.rect.height
    kropla.x = kropla_width + 12 * kropla_width * rain_number
    kropla.rect.x = kropla.x
    kropla.rect.x += kropla.rect.width + 12 * kropla.rect.width * rownumberss
    deszcz.add(kropla)


def change_fleet_direction(ai_settings, aliens):
    # Przesunięcie całej floty w dół i zmiana kierunku, w któym się ona porusza
    for alien in aliens.sprites():
        alien.rect.x -= ai_settings.fleet_drop_speed
    ai_settings.fleet_direction /= -1


def check_fleet_edges(ai_settings, aliens):
    # Odpowiednia reakcja, gdzy obce dotrze do krawędzi ekranu
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_boss_fleet_edges(ai_settings, bosss):
    for BOSS in bosss.sprites():
        if BOSS.check_edges():
            change_boss_fleet_direction(ai_settings, bosss)
            break


def change_boss_fleet_direction(ai_settings, bosss):
    for BOSS in bosss.sprites():
        BOSS.rect.y -= ai_settings.fleet_drop_speed
    ai_settings.fleet_direction /= -1


def check_rain_down(ai_settings, deszcz):
    for kropla in deszcz.sprites():
        if kropla.check_rain_edges():
            drop_rain_down(ai_settings, deszcz)


def drop_rain_down(ai_settings, deszcz):
    for kropelka in deszcz.sprites():
        kropelka.rect.y += ai_settings.speed_drop_rain


def update_rain(ai_settings, deszcz):
    check_rain_down(ai_settings, deszcz)
    deszcz.update(deszcz, ai_settings)
    for rain in deszcz.copy():
        if rain.rect.top <= 0 or ai_settings.SCREEN_HEIGHT < rain.rect.top:
            deszcz.remove(rain)


def update_aliens(ai_settings, stats, sb, screen, player, aliens, new_bullet):
    # uaktualnienie położenia wszystkich obcych we flocie
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    hit_sound = pygame.mixer.Sound('C:/Users/Kamil/Pictures/hit.wav')
    # Wykrycie kolizji między statkiem a obcymi
    if pygame.sprite.spritecollideany(player, aliens):
        hit_sound.play()
        alien_hit_player(ai_settings, stats, sb, screen, player, aliens, new_bullet)

    check_aliens_left(ai_settings, stats, sb, screen, player, aliens, new_bullet)


def update_boss(ai_settings, bosss):
    check_boss_fleet_edges(ai_settings, bosss)
    bosss.update()


def update_animation(explosion):
    explosion.update()


def alien_hit_player(ai_settings, stats, sb, screen, player, aliens, new_bullet):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        new_bullet.empty()
    # Utworzenie całej floty obcych od nowa
        sleep(0.5)
        create_fleet(ai_settings, screen, player, aliens)
        player.player_center()


def create_bosss(ai_settings, screen, aliens, bosss, boss_bullet, new_bullet, extra_bullet, HPbar, player, explosion):
    destroy = pygame.mixer.Sound('C:/Users/Kamil/Pictures/BossDestroyed.wav')
    aliens.empty()
    bosss.draw(screen)
    boss_bullet.draw(screen)
    extra_bullet.draw(screen)
    HPbar.blitme(bosss)
    HPbar.hit(bosss, new_bullet, boss_bullet, ai_settings, extra_bullet)
    player.hit(bosss, boss_bullet, extra_bullet)
    if HPbar.Health <= 4:
        explosion.draw(screen)
        hit = pygame.sprite.groupcollide(new_bullet, bosss, False, False)
        if hit:
            AniExplosion(explosion, bosss)
            bosss.empty()
            boss_bullet.empty()
            extra_bullet.empty()
            destroy.play()


def check_aliens_left(ai_settings, stats, sb, screen, player, aliens, new_bullet):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.left <= screen_rect.left:
            alien_hit_player(ai_settings, stats, sb, screen, player, aliens, new_bullet)
        break


def time_txt(screen, txt, youlost):
    screen.blit(youlost, (0, 0))
    screen.blit(txt, (480, 500))


def update_screen(ai_settings, screen, player, bosss, deszcz, aliens, starr, new_bullet, boss_bullet,
                  HPbar, extra_bullet, explosion, stats, sb, pause_button):
    player.blitme(HPbar, screen)
    sb.show_score()
    for bullets in new_bullet.sprites():
        bullets.draw_pocisk()

    # deszcz.draw(screen)
    aliens.draw(screen)
    if not stats.game_active:
        pause_button.draw_button()

    if len(aliens) == 0:
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_ships()
        aliens.empty()
        if stats.level > 3 and stats.ships_left >= 0:
            create_bosss(ai_settings, screen, aliens, bosss, boss_bullet, new_bullet, extra_bullet, HPbar, player,
                         explosion)
        else:
            sleep(0.2)
            new_bullet.empty()
            create_fleet(ai_settings, screen, player, aliens)
            player.player_center()

    # Updated screen
    pygame.display.flip()
