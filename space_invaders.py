import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf

def run_game():
    "Initialize game"
    pygame.init()
    si_settings = Settings()
    screen = pygame.display.set_mode(
        (si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(si_settings, screen)
    stats = GameStats(si_settings)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(si_settings, screen, ship, aliens)

    while True:
        gf.check_events(si_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(si_settings, screen, ship, aliens, bullets)
            gf.update_aliens(si_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(si_settings, screen, ship, aliens, bullets)

run_game()
