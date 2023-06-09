import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        super().__init__()
        """Initialize the ship and set it's starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
# Load the ship image and get it's rest.
        pygame.init()
        self.image = pygame.image.load('images/alien_invasion.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
# Start each new ship at the bottom center of the screen
        self.center = float(self.rect.centerx)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
            # Update rect object from self.center
            self.rect.centerx = self.center
            
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        