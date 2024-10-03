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

        # Health and points
        self.health = 100  # Player's health
        self.points = 0  # Player's score

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
        self.draw_health_bar(screen)  # Draw health bar beneath player

    # Method to draw the health bar
    def draw_health_bar(self, screen):
        # Set the dimensions and position of the health bar
        bar_width = 40  # Width of the health bar
        bar_height = 5  # Height of the health bar
        health_ratio = self.health / 100  # Ratio of current health to max health

        # Draw the background of the health bar
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.centerx - bar_width // 2, self.rect.bottom + 5, bar_width, bar_height))

        # Draw the current health
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.centerx - bar_width // 2, self.rect.bottom + 5, bar_width * health_ratio, bar_height))

    # Method to take damage
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    # Method to add points
    def add_points(self, points):
        self.points += points
