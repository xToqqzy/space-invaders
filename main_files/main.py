# main.py

import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS  # Import settings
from player import Player  # Import the Player class

# Initialize Pygame
pygame.init()

# Set up the display (screen size defined in settings.py)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")  # Set window title

# Create clock object for frame control (optional)
clock = pygame.time.Clock()

# Create player instance
player = Player()

# Main game loop
while True:
    # Handle events (like quitting the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player input
    player.handle_input()

    # Update player movement
    player.update()

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the player on the screen
    player.draw(screen)

    # Update the full display (refresh the screen)
    pygame.display.flip()

    # Control the game frame rate (optional)
    clock.tick(FPS)
