#!/usr/bin/python

import pygame
import sys

def draw_screen(screen, bg_color):
    """Drawn the screen."""
    screen.fill(bg_color)
    
    # Make the most recently drawn screen visible
    pygame.display.flip()


while True:
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    bg_color = (0, 0, 255)
    pygame.display.set_caption("Blue Sky")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            draw_screen(screen, bg_color)