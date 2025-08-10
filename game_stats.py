# ------------------------- Respond to Alien-Ship collision ----------------------

class GameStats:
    """Track stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset
        self.high_score = 0
    
    def reset_stats(self):
        """Inititalises stats that change during game"""
        self.ships_left = self.settings.ship_limit

        # Setting Score
        self.score = 0

        # Show level
        self.level = 1