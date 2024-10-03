import pygame
import sys
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS  # Import settings
from player import Player  # Import the Player class
from enemy import Enemy  # Import the Enemy class
from bullet import Bullet  # Import the Bullet class

# Initialize Pygame
pygame.init()

# Set up the display (screen size defined in settings.py)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")  # Set window title

# Create clock object for frame control (optional)
clock = pygame.time.Clock()

# Create player instance
player = Player()
player_bullets = []  # List for player bullets

# Create a list for enemies (initially empty)
enemies = []

# Game state
game_active = True
game_over = False
show_menu = False  # Flag for showing escape menu

# Initialize timers
player_shoot_timer = 0  # Timer for player's shooting
enemy_spawn_timer = 0  # Timer for enemy spawning
enemy_spawn_interval = 0.17  # Spawn enemies every ~0.17 seconds
max_enemies = 15  # Maximum number of enemies on the screen

# Main game loop
while True:
    delta_time = clock.tick(FPS) / 1000.0  # Delta time for shooting intervals

    # Handle events (like quitting the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Restart the game when pressing 'R'
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_active = True
                game_over = False
                player = Player()  # Reset player
                enemies = []  # Reset enemies
                player_bullets = []  # Reset player bullets

        # Quit the game when pressing 'Q'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        # Show the escape menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_menu = True
                game_active = False  # Pause the game

    if game_active:
        # Handle player input
        player.handle_input()

        # Update player movement
        player.update()

        # Player shooting logic
        player_shoot_timer += delta_time
        if player_shoot_timer >= 0.5:  # Shoot every 0.5 seconds
            bullet = Bullet(player.rect.centerx, player.rect.top)
            player_bullets.append(bullet)
            player_shoot_timer = 0  # Reset the timer

        # Update player bullets
        for bullet in player_bullets[:]:
            if bullet.update():  # Update bullet position
                player_bullets.remove(bullet)  # Remove bullet if it goes off-screen

        # Enemy spawning logic
        enemy_spawn_timer += delta_time
        if enemy_spawn_timer >= enemy_spawn_interval and len(enemies) < max_enemies:
            enemy = Enemy()
            enemies.append(enemy)
            enemy_spawn_timer = 0

        # Update enemies
        for enemy in enemies:
            enemy.update(delta_time)

            # Check for collisions between player and enemies
            if player.rect.colliderect(enemy.rect):
                game_active = False  # Set game to inactive
                game_over = True  # Show game over screen

            # Check for collisions between player bullets and enemies
            for bullet in player_bullets[:]:
                if bullet.rect.colliderect(enemy.rect):
                    player.add_points(250)  # Add points when an enemy is hit
                    enemy.is_alive = False  # Mark enemy as dead
                    player_bullets.remove(bullet)  # Remove bullet
                    break

            # Check for collisions between enemy bullets and player
            for bullet in enemy.bullets[:]:
                if bullet.rect.colliderect(player.rect):
                    player.take_damage(20)  # Reduce health by 20
                    enemy.bullets.remove(bullet)  # Remove enemy bullet

                    if player.health <= 0:  # Check if player is dead
                        game_active = False
                        game_over = True
                    break

        # Fill the screen with the background color
        screen.fill(BACKGROUND_COLOR)

        # Draw the player on the screen
        player.draw(screen)

        # Draw the bullets
        for bullet in player_bullets:
            bullet.draw(screen)

        # Draw the enemies on the screen
        for enemy in enemies:
            enemy.draw(screen)

    if game_over:
        # Display the death screen
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        # Display the points scored
        score_text = font.render(f"Score: {player.points}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(score_text, score_rect)

        font = pygame.font.Font(None, 36)
        restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(restart_text, restart_rect)

    if show_menu:
        # Display escape menu
        font = pygame.font.Font(None, 74)
        text = font.render("Paused", True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        continue_text = font.render("Press C to Continue", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(continue_text, continue_rect)

        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(restart_text, restart_rect)

        quit_text = font.render("Press Q to Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        screen.blit(quit_text, quit_rect)

        # Handle menu actions
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:  # Continue
            show_menu = False
            game_active = True
        if keys[pygame.K_r]:  # Restart
            game_active = True
            game_over = False
            player = Player()  # Reset player
            enemies = []  # Reset enemies
            player_bullets = []  # Reset player bullets
            show_menu = False
        if keys[pygame.K_q]:  # Quit
            pygame.quit()
            sys.exit()

    # Update the full display (refresh the screen)
    pygame.display.flip()
