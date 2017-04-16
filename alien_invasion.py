# alien_invasion.py
# Much of this program is copied from a tutorial in the book
#  Python Crash Course, by Eric Matthes.

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        # Draw the current screen.
        gf.update_screen(ai_settings, screen, ship)

run_game()
