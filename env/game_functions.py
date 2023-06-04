import sys

import pygame

def check_keydown_events(event, ship):
     """Respond to keypresses."""
     for event in pygame.event.get():
        if event.key == pygame.K_RIGHT:
         ship.moving_right = True
        elif event.key == pygame.K_LEFT:
         ship.moving_left = True

def check_keydup_events(event, ship):
     """Respond to keypresses."""
     for event in pygame.event.get():
        if event.key == pygame.K_RIGHT:
         ship.moving_right = False
        elif event.key == pygame.K_LEFT:
         ship.moving_left = False

def check_events(ship):
    """Respond to keypresses and mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True

        elif event.type == pygame.KEYUP:
             check_keydup_events(event, ship)
        if event.key == pygame.K_RIGHT:
             ship.moving_right = False
        elif event.key == pygame.K_LEFT:
             ship.moving_left = False
def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen and flip to the new screen.
    screen.fill(ai_settings.bg_color)
    ship.blit()

    # Make the most recently drawn screen visible.
    pygame.display.flip()