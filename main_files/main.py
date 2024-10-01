import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR  # Adjust this line as needed


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")  # Set the window title

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Exit the program if the window is closed

    # Fill the background color (optional, can be done later)
    screen.fill(BACKGROUND_COLOR)  # Use a color defined in settings.py or a background image

    # Refresh the screen
    pygame.display.flip()  # Update the full display Surface to the screen
