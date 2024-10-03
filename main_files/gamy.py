import pygame
import random  # Import random module
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self):
        # Load the enemy image
        self.image = pygame.image.load("main_files/assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Adjust the size as needed
        self.rect = self.image.get_rect()
        self.reset()  # Position the enemy at the top

    def reset(self):
        # Set enemy starting position at the top and a random horizontal position
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)  # Start off-screen

    def update(self):
        # Move the enemy down the screen
        self.rect.y += 5  # Adjust speed as necessary
        if self.rect.top > SCREEN_HEIGHT:  # If the enemy goes off-screen
            self.reset()  # Reset to the top

    def draw(self, screen):
        # Draw the enemy on the screen
        screen.blit(self.image, self.rect)
