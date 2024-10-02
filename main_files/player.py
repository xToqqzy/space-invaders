# player.py

import pygame

class Player:
    def __init__(self):
        # Load the player image and scale it to 40x32 pixels
        self.image = pygame.image.load("main_files/assets/player.png")
        self.image = pygame.transform.scale(self.image, (40, 32))

        # Get the player's rectangle for position
        self.rect = self.image.get_rect()

        # Start player at the bottom center of the screen
        self.rect.centerx = 400  # Horizontal position (center)
        self.rect.bottom = 580   # Vertical position

        # Movement speed and direction control
        self.speed_x = 0
        self.speed = 5  # Speed of movement (adjustable)

    # Method to handle player input (moving left/right)
    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.speed_x = -self.speed  # Move left
        elif keys[pygame.K_RIGHT]:
            self.speed_x = self.speed   # Move right
        else:
            self.speed_x = 0  # No key pressed, stop moving

    # Method to update player position based on input
    def update(self):
        self.rect.x += self.speed_x

        # Keep player within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:  # Assuming screen width is 800
            self.rect.right = 800

    # Method to draw player on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
