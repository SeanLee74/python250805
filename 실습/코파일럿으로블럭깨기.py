import pygame
import sys

# 초기화
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기")
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (153, 0, 255)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)
PINK = (255, 51, 153)

BLOCK_COLORS = [BLUE, RED, GREEN, YELLOW, PURPLE, ORANGE, CYAN, PINK]

# 패들
PADDLE_WIDTH, PADDLE_HEIGHT = 300, 15  # 폭을 기존의 3배로 변경
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 10

# 공
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [5, -5]

# 블럭
BLOCK_ROWS, BLOCK_COLS = 6, 10
BLOCK_WIDTH = WIDTH // BLOCK_COLS
BLOCK_HEIGHT = 30
blocks = []
block_colors = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT + 60, BLOCK_WIDTH - 2, BLOCK_HEIGHT - 2)
        blocks.append(block)
        # 각 행마다 다른 색상 적용
        color = BLOCK_COLORS[row % len(BLOCK_COLORS)]
        block_colors.append(color)

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # 공 이동
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= HEIGHT:
        # 게임 오버
        font = pygame.font.SysFont(None, 72)
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (WIDTH // 2 - 180, HEIGHT // 2 - 36))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # 패들 충돌
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 블럭 충돌
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        hit_block = blocks.pop(hit_index)
        ball_speed[1] = -ball_speed[1]

    # 블럭 그리기
    for i, block in enumerate(blocks):
        pygame.draw.rect(screen, block_colors[i], block)

    # 패들, 공 그리기
    pygame.draw.rect(screen, GREEN, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # 승리 조건
    if not blocks:
        font = pygame.font.SysFont(None, 72)
        text = font.render("YOU WIN!", True, GREEN)
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 36))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()