import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initialize pygame, settings, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    # Set the background color.

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        


        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()