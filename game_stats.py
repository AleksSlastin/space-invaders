class GameStats():

    def __init__(self, si_settings):
        self.si_settings = si_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.si_settings.ship_limit
