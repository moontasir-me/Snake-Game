import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game constants
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 15

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Developed by Tanim")

# Initialize clock
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 30)


def display_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    win.blit(text, [10, 10])
    # Developer credit
    credit_text = small_font.render("Developed by Tanim", True, WHITE)
    win.blit(credit_text, [WIDTH - 200, HEIGHT - 30])


def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(win, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])


def message(msg, color):
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    win.blit(text, text_rect)

    # Developer credit
    credit_text = small_font.render("Developed by Tanim", True, WHITE)
    credit_rect = credit_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    win.blit(credit_text, credit_rect)

    pygame.display.update()


def game_loop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2
    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        while game_close:
            win.fill(BLACK)
            message("Game Over! Press C-Play Again or Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != BLOCK_SIZE:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx != -BLOCK_SIZE:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy != BLOCK_SIZE:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy != -BLOCK_SIZE:
                    dy = BLOCK_SIZE
                    dx = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += dx
        y += dy
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        display_score(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = (
                round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            )
            food_y = (
                round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE)
                * BLOCK_SIZE
            )
            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()


print("Snake Game - Developed by Tanim")
game_loop()
