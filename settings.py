import pygame
class Settings():
    'Space Invaders settings'
    def __init__(self):
        self.screen_width = 1366
        self.screen_height = 740
        self.background_image = pygame.image.load('images/space.jpg')

        self.fleet_drop_speed = 10
        self.ship_limit = 3
        # fleet_direction = 1 right motion; -1 left motion
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 200 , 230
        self.bullets_allowed = 3

    def cheat(self):
        self.bullets_allowed = 4
        self.bullet_width = 200
        self.bullet_color = 230, 0 , 230

    def music(self):
        pygame.mixer.music.load("music/01_brad_fiedel_main_title_from_"
                            "terminator_2_judgement_day_myzuka.mp3")
        pygame.mixer.music.play(-1,0.0)

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 6
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 5
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

