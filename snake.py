import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
window_width = 640
window_height = 480
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the size of each grid block
block_size = 20

# Initialize the clock
clock = pygame.time.Clock()

# Define the Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.positions = [((window_width // 2), (window_height // 2))]
        self.direction = None
        self.color = WHITE

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        if self.direction:
            cur = self.get_head_position()
            x, y = self.direction

            new = (((cur[0] + (x * block_size)) % window_width), (cur[1] + (y * block_size)) % window_height)
            if len(self.positions) > 2 and new in self.positions[2:]:
                self.reset()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.size:
                    self.positions.pop()

    def reset(self):
        self.size = 1
        self.positions = [((window_width // 2), (window_height // 2))]
        self.direction = None

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], block_size, block_size))

# Define the Apple class
class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (window_width - block_size) // block_size) * block_size,
                         random.randint(0, (window_height - block_size) // block_size) * block_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], block_size, block_size))

# Create instances of the Snake and Apple classes
snake = Snake()
apple = Apple()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w] and snake.direction != (0, 1):
                snake.direction = (0, -1)
            elif event.key in [pygame.K_DOWN, pygame.K_s] and snake.direction != (0, -1):
                snake.direction = (0, 1)
            elif event.key in [pygame.K_LEFT, pygame.K_a] and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            elif event.key in [pygame.K_RIGHT, pygame.K_d] and snake.direction != (-1, 0):
                snake.direction = (1, 0)

    snake.update()

    if snake.get_head_position() == apple.position:
        snake.size += 1
        apple.randomize_position()

    window.fill(BLACK)
    snake.draw(window)
    apple.draw(window)
    pygame.display.update()
    clock.tick(10)  # Controls the speed of the game

# Quit the game
pygame.quit()