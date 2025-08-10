# ------------------------ To store all settings of Alien Invasion --------------------

class Settings:
    """Class to store all settings of Alien Invasion"""
    
    def __init__(self):
        """Initialise game's static settings"""

        # ------------ Screen settings --------------
        self.screen_width = 1170
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Allows to fire max bullets uptp the value
        self.bullets_allowed = 5
        # self.bg_color = (0, 0, 255)               for blue screen

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.9
        self.bullet_width = 5           # If bullet size changes, it changes game in a fun way
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)        # These settings create dark gray bullets with a width of 3 pixels and a height of 15 pixels. The bullets will travel slightly slower than the ship

        # Alien settings
        self.alien_speed = 0.9
        self.fleet_drop_speed = 5

        # How quickly the game speeds up
        self.speedup_scale = 10

        # How fast alien point values increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings() 


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.9

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring --------
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings & alien points value"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)