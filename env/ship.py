import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set it's starting position"""
        self.screen = screen

    # Load the ship image and get it's rest.
    self.image = pygame.image.load('images')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # Start each new ship at the bottom center of the screen.
    self.rect.centerx = self.screen_rect.centrex
    self.rect.bottom = self.screen_rect.bottom

def blitme(self):
    """"Draw the ship at it's current location"""
    self.screen.blitme(self.image, self.rect)