import sys
import pygame
from src.game.pygame.Ball import Ball

# initialize pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
FPS = 60

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)
ball = Ball(WIDTH / 2, HEIGHT / 2, 5, 5, 20)

# Set up the paddles
paddle1_y = paddle2_y = HEIGHT / 2 - PADDLE_HEIGHT / 2

# Set up the score
score_player_left = 0
score_player_right = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= 5
    if keys[pygame.K_s]:
        paddle1_y += 5
    if keys[pygame.K_UP]:
        paddle2_y -= 5
    if keys[pygame.K_DOWN]:
        paddle2_y += 5

    # Move the ball
    ball.move()

    # Collision with walls (up and down)
    if ball.y < 0 or ball.y > HEIGHT - ball.radius:
        ball.bounce_y()

    # Collision of the ball with paddles
    if ball.x < PADDLE_WIDTH + ball.radius and paddle1_y < ball.y < paddle1_y + PADDLE_HEIGHT:
        ball.bounce_x()
    elif ball.x > WIDTH - PADDLE_WIDTH - ball.radius and paddle2_y < ball.y < paddle2_y + PADDLE_HEIGHT:
        ball.bounce_x()

    # scoring the ball
    if ball.x < 0:
        score_player_right += 1
        ball.reset(WIDTH / 2, HEIGHT / 2)
    elif ball.x > WIDTH - ball.radius:
        score_player_left += 1
        ball.reset(WIDTH / 2, HEIGHT / 2)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # paddle on left
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # paddle on right
    pygame.draw.circle(screen, WHITE, (ball.x, ball.y), ball.radius)
    text = font.render(f"{score_player_left} - {score_player_right}", True, WHITE)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
