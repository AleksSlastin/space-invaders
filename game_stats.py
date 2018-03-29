class GameStats():

    def __init__(self, si_settings):
        self.si_settings = si_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.si_settings.ship_limit
        self.score = 0
        self.level = 1
