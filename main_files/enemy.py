# enemy.py

import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from bullet import Bullet  # Import the Bullet class

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("main_files/assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Adjust the size
        self.rect = self.image.get_rect()
        self.reset()  # Position the enemy at the top
        self.shoot_timer = random.uniform(0, 2)  # Random initial shoot timer for staggered shooting
        self.bullets = []  # List to store enemy bullets
        self.is_alive = True  # Track if the enemy is alive

    def reset(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)  # Start off-screen

    def update(self, delta_time):
        if not self.is_alive:
            return

        self.rect.y += 3  # Move the enemy down the screen
        if self.rect.top > SCREEN_HEIGHT:  # If the enemy goes off-screen
            self.reset()  # Reset to the top

        # Enemy shooting logic
        self.shoot_timer += delta_time
        if self.shoot_timer >= 2.0:  # Shoot every 2 seconds
            self.shoot_bullet()
            self.shoot_timer = 0

        # Update enemy bullets
        self.update_bullets()

    def shoot_bullet(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom, is_player_bullet=False)  # Indicate enemy bullet
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets[:]:
            if bullet.update():  # Update bullet position
                self.bullets.remove(bullet)  # Remove bullet if it goes off-screen

    def draw(self, screen):
        if self.is_alive:
            screen.blit(self.image, self.rect)
            for bullet in self.bullets:  # Draw enemy bullets
                bullet.draw(screen)
