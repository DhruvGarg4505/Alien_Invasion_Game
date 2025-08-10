# -------------------- Creating an alien ship -------------------------

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """"Class to denote single alien in fleet"""

    def __init__(self, ai_game):
        """Initialise the alien & set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image & set its rect value
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien at near top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horizontal pos
        self.x = float(self.rect.x)


    def update(self):
        """Move alien to right"""
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        """Returns True if alien is at edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        