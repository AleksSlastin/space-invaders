import sys
import pygame
from pygame.sprite import Group

from settings import Settings
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

    bullets = Group()

    while True:
        gf.check_events(si_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(si_settings, screen, ship, bullets)

run_game()
