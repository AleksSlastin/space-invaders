import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    "Initialize game"
    pygame.init()
    si_settings = Settings()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Space Invaders")

    Settings.music(si_settings)

    ship = Ship(si_settings, screen)
    stats = GameStats(si_settings)
    sb = Scoreboard(si_settings, screen, stats)
    play_button = Button(si_settings, screen, "Play")

    bullets = Group()
    aliens = Group()

    gf.create_fleet(si_settings, screen, ship, aliens)

    while True:
        gf.check_events(si_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(si_settings, screen, stats, sb, ship,
                              aliens, bullets)
            gf.update_aliens(si_settings, screen, stats, sb, ship, aliens,
                             bullets)
        gf.update_screen(si_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
