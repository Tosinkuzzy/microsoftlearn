import pygame
from bullet import Bullet
import sys

def check_keydown_events(ai_settings, bullets, event, ship, screen):
    """Respond to keypresses."""
    for event in pygame.event.get():
        if event.key == pygame.K_RIGHT:
         ship.moving_right = True
        elif event.key == pygame.K_LEFT:
         ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached."""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, ship, screen)
        bullets.add(new_bullet)

def check_keydup_events(event, ship):
    """Respond to keypresses."""
    for event in pygame.event.get():
        if event.key == pygame.K_RIGHT:
          ship.moving_right = False
        elif event.key == pygame.K_LEFT:
          ship.moving_left = False

def check_events(ai_settings, bullets, ship, screen):
    """Respond to keypresses and mouse."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys()
                
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(ai_settings, bullets, event, ship, screen)
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

def update_screen(ai_settings, bullets, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen and flip to the new screen.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

def update_bullets(bullets):
   """Update position of bullets and get rid of the old bullets."""
   # Update bullet positions.
   bullets.update()

   # Get rid of bullets that have disappear.
   for bullet in bullets.copy():
      if bullet.rect.bottom <= 0:
         bullets.remove(bullet)