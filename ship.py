# ---------------------- Creating Ship -----------------------
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Class to manage ship"""

    def __init__(self, ai_game):
        """Initialise ship & set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image ------------
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at bottom of center line -----------------
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        """Updates ship's position based on movement flag"""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x


    def blitme(self):                   # Its blit me in reading
        """Draws ship at current loc"""
        self.screen.blit(self.image, self.rect)


    # To center the ship ---------------
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)