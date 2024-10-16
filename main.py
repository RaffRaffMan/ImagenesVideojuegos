import pygame

# Initialize window.
pygame.init()

# screen is a Surface (to render game onto).
# set_mode returns a Surface.
screen = pygame.display.set_mode((800, 600))
screen_rect = pygame.Rect(0, 0, 800, 600)

clock = pygame.time.Clock()

running = True

# hitboxes for the paddles
left_paddle = pygame.Rect(50, 255, 8, 90)
right_paddle = pygame.Rect(742, 255, 8, 90)

# ball hitbox (as rectangle)
ball_hitbox = pygame.Rect(400, 300, 16,16)
ball_hitbox.center = (400, 300)

# ball velocity
ball_velocity_x = 5
ball_velocity_y = -3

# Main game loop. Runs 60 times per second.
while running:
    # Poll for events. Iterate through every event in the queue.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with color to clear previous frame.
    screen.fill("black")


    # -------------- UPDATE THE GAME HERE -----------------


    # Get state of keys
    keys = pygame.key.get_pressed()


    # Paddles

    # Move left paddle
    if keys[pygame.K_w]:
        left_paddle.move_ip(0, -5)
    if keys[pygame.K_s]:
        left_paddle.move_ip(0, 5)

    # Move right paddle
    if keys[pygame.K_UP]:
        right_paddle.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        right_paddle.move_ip(0, 5)

    # clamp paddles
    left_paddle.clamp_ip(screen_rect)
    right_paddle.clamp_ip(screen_rect)

    # Ball

    # move ball
    ball_hitbox.move_ip(ball_velocity_x, ball_velocity_y)

    # ball border bounce
    if ball_hitbox.top < 0 or ball_hitbox.bottom > 600:
        ball_velocity_y = -ball_velocity_y

    # ball paddle bounce
    if ball_hitbox.colliderect(left_paddle) or ball_hitbox.colliderect(right_paddle):
        ball_velocity_x = -ball_velocity_x

    # ball game over
    if ball_hitbox.left < 0 or ball_hitbox.right > 800:
        ball_hitbox.center = (400, 300)


    # Drawing

    # Left paddle
    pygame.draw.rect(screen, "green", left_paddle)
    # Right paddle
    pygame.draw.rect(screen, "magenta", right_paddle)
    # Ping Ball
    pygame.draw.circle(screen, "yellow", ball_hitbox.center, 8)


    # -----------------------------------------------------


    # Flip display to render the new frame.
    pygame.display.flip()

    # Limit framerate to 60 FPS.
    clock.tick(60)

pygame.quit()
