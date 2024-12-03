import pygame
import sys
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS
from player import Player
from enemy import Enemy
from bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

player = Player()
player_bullets = []

enemies = []

game_active = True
game_over = False
show_menu = False

player_shoot_timer = 0
enemy_spawn_timer = 0
enemy_spawn_interval = 0.17
max_enemies = 15

while True:
    delta_time = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            game_active = True
            game_over = False
            player = Player()
            enemies = []
            player_bullets = []

        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            show_menu = True
            game_active = False

    if game_active:
        player.handle_input()

        player.update()

        player_shoot_timer += delta_time
        if player_shoot_timer >= 0.5:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            player_bullets.append(bullet)
            player_shoot_timer = 0

        for bullet in player_bullets[:]:
            if bullet.update():
                player_bullets.remove(bullet)

        enemy_spawn_timer += delta_time
        if enemy_spawn_timer >= enemy_spawn_interval and len(enemies) < max_enemies:
            enemy = Enemy()
            enemies.append(enemy)
            enemy_spawn_timer = 0

        for enemy in enemies:
            enemy.update(delta_time)

            if player.rect.colliderect(enemy.rect):
                game_active = False
                game_over = True

            for bullet in player_bullets[:]:
                if bullet.rect.colliderect(enemy.rect):
                    player.add_points(250)
                    enemy.is_alive = False
                    player_bullets.remove(bullet)
                    break

            for bullet in enemy.bullets[:]:
                if bullet.rect.colliderect(player.rect):
                    player.take_damage(20)
                    enemy.bullets.remove(bullet)

                    if player.health <= 0:
                        game_active = False
                        game_over = True
                    break

        screen.fill(BACKGROUND_COLOR)

        player.draw(screen)
        for bullet in player_bullets:
            bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        score_text = font.render(
            f"Score: {player.points}", True, (255, 255, 255))
        score_rect = score_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(score_text, score_rect)

        font = pygame.font.Font(None, 36)
        restart_text = font.render(
            "Press R to Restart or Q to Quit", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(restart_text, restart_rect)

    if show_menu:
        font = pygame.font.Font(None, 74)
        text = font.render("Paused", True, (255, 0, 0))
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        continue_text = font.render(
            "Press C to Continue", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(continue_text, continue_rect)

        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(restart_text, restart_rect)

        quit_text = font.render("Press Q to Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        screen.blit(quit_text, quit_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            show_menu = False
            game_active = True
        if keys[pygame.K_r]:
            game_active = True
            game_over = False
            player = Player()
            enemies = []
            player_bullets = []
            show_menu = False
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
