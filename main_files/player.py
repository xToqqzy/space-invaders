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
        self.rect.centerx = 400  # Horizontal position (center of the screen)
        self.rect.bottom = 580   # Vertical position (near bottom of the screen)

        # Movement speed
        self.speed_x = 0  # Speed for horizontal movement
        self.speed_y = 0  # Speed for vertical movement
        self.speed = 5    # Movement speed for both directions

    # Method to handle player input (moving in four directions)
    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Horizontal movement (left/right)
        if keys[pygame.K_LEFT]:
            self.speed_x = -self.speed  # Move left
        elif keys[pygame.K_RIGHT]:
            self.speed_x = self.speed   # Move right
        else:
            self.speed_x = 0  # No horizontal movement

        # Vertical movement (up/down)
        if keys[pygame.K_UP]:
            self.speed_y = -self.speed  # Move up
        elif keys[pygame.K_DOWN]:
            self.speed_y = self.speed   # Move down
        else:
            self.speed_y = 0  # No vertical movement

    # Method to update player position based on input
    def update(self):
        # Update position based on speed
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Keep player within screen bounds (horizontal)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

        # Keep player within screen bounds (vertical)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

    # Method to draw player on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
