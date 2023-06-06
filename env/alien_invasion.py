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
        gf.check_events(ai_settings, bullets, screen, ship)
        ship.update()
        bullets.update()

        ship.blitme()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, bullets, screen, ship)
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()
run_game()