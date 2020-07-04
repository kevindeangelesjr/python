#!/usr/bin/python

### IMPORTS ###

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

### FUNCTIONS ###

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events()
        # Redraw screen
        gf.update_screen(ai_settings, screen, ship)

### MAIN LOGIC ###

run_game()