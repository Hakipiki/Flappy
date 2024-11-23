```
import pygame
import sys

Initialize Pygame
pygame.init()

Set up some constants
WIDTH, HEIGHT = 640, 480
PIPE_WIDTH, PIPE_HEIGHT = 80, 600
BIRD_SIZE = 40
GRAVITY = 0.2
FLAP_VEL = 6

Set up some variables
bird_x, bird_y = WIDTH / 2, HEIGHT / 2
bird_vel = 0
pipe_x, pipe_y = WIDTH, HEIGHT / 2
score = 0
game_over = False

Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Set up the clock
clock = pygame.time.Clock()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_vel = -FLAP_VEL

    # Game logic
    if not game_over:
        bird_vel += GRAVITY
        bird_y += bird_vel

        pipe_x -= 2
        if pipe_x < -PIPE_WIDTH:
            pipe_x = WIDTH
            pipe_y = HEIGHT / 2 + (HEIGHT / 2) * (score / 10)

        if (bird_x + BIRD_SIZE > pipe_x and
            bird_x < pipe_x + PIPE_WIDTH and
            (bird_y < pipe_y - 150 or bird_y + BIRD_SIZE > pipe_y + 150)):
            game_over = True

        if bird_y > HEIGHT - BIRD_SIZE or bird_y < 0:
            game_over = True

        score += 1 / 60  # increment score by 1 every second

    # Drawing
    screen.fill((135, 206, 235))  # light blue sky
    pygame.draw.rect(screen, (50, 205, 50), (pipe_x, 0, PIPE_WIDTH, pipe_y - 150))  # top pipe
    pygame.draw.rect(screen, (50, 205, 50), (pipe_x, pipe_y + 150, PIPE_WIDTH, HEIGHT - pipe_y - 150))  # bottom pipe
    pygame.draw.rect(screen, (255, 255, 0), (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))  # bird

    # Display score
    font = pygame.font.Font(None, 72)
    text = font.render(str(int(score)), True, (0, 0, 0))
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 50))

    # Display game over message
    if game_over:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
```
