import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    for event in pygame.event.get():
        if event.key == pygame.K_RIGHT:
         ship.moving_right = True
        elif event.key == pygame.K_LEFT:
         ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Create a new bullet and add it to the bullets group.
            new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)
def check_keydup_events(event, ship):
     """Respond to keypresses."""
     for event in pygame.event.get():
        if event.key == pygame.K_RIGHT:
         ship.moving_right = False
        elif event.key == pygame.K_LEFT:
         ship.moving_left = False
def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
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
def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen and flip to the new screen.
    for bullet in bullets.sprint():
        bullet.draw_update()
    screen.fill(ai_settings.bg_color)
    ship.blit()
    # Make the most recently drawn screen visible.
pygame.display.flip()