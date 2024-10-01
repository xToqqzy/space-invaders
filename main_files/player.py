


keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    char_rect.x -= movement_speed
if keys[pygame.K_RIGHT]:
    char_rect.x += movement_speed
if keys[pygame.K_UP]:
    char_rect.y -= movement_speed
if keys[pygame.K_DOWN]:
    char_rect.y += movement_speed