import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and create a screen object.
    pygame.init()
    # Make a ship.
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    # Set the background color.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        bullets.update()
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blit()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()