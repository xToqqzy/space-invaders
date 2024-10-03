# bullet.py

import pygame

class Bullet:
    def __init__(self, x, y, is_player_bullet=True):
        self.image = pygame.Surface((5, 10))  # Smaller size for bullets
        self.image.fill((255, 0, 0) if is_player_bullet else (255, 0, 0))  # Red color for both
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10 if is_player_bullet else 5  # Negative speed for player bullets, positive for enemy bullets

    def update(self):
        self.rect.y += self.speed  # Move the bullet
        return self.rect.bottom < 0 or self.rect.top > 600  # Returns True if the bullet goes off-screen

    def draw(self, screen):
        screen.blit(self.image, self.rect)
