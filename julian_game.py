import pygame
import random

pygame.init()

# Screen and clock setup
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Colors
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
BLUE        = (0, 0, 255)
YELLOW      = (255, 255, 0)
CYAN        = (0, 255, 255)
MAGENTA     = (255, 0, 255)
GRAY        = (128, 128, 128)
DARK_GRAY   = (64, 64, 64)
LIGHT_GRAY  = (192, 192, 192)
ORANGE      = (255, 165, 0)
PINK        = (255, 192, 203)
PURPLE      = (128, 0, 128)
BROWN       = (165, 42, 42)
GOLD        = (255, 215, 0)
SILVER      = (192, 192, 192)
NAVY        = (0, 0, 128)
LIME        = (50, 205, 50)
TEAL        = (0, 128, 128)
MAROON      = (128, 0, 0)
OLIVE       = (128, 128, 0)
TURQUOISE   = (64, 224, 208)
INDIGO      = (75, 0, 130)
VIOLET      = (238, 130, 238)
CHOCOLATE   = (210, 105, 30)
SALMON      = (250, 128, 114)
TOMATO      = (255, 99, 71)
CORAL       = (255, 127, 80)
AQUA        = (0, 255, 255)
LIGHT_BLUE  = (173, 216, 230)
DARK_BLUE   = (0, 0, 139)
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN  = (0, 100, 0)
LIGHT_YELLOW= (255, 255, 224)
DARK_RED    = (139, 0, 0)

# Character 
runner_x = WIDTH // 2
runner_y = HEIGHT // 2
runner_speed = 5

# Housea
house_width = 30
house_height = 30
house1_x = 0
house1_y = random.randint(-HEIGHT, 0)
house2_x = WIDTH - house_width
house2_y = random.randint(-HEIGHT, 0)

# Barrier setup (50 pixels away from the edges)
left_barrier = 50
right_barrier = WIDTH - 50 - house_width  # 50 pixels from the right edge
top_barrier = 50
bottom_barrier = HEIGHT - 50

# Game loop
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    keys = pygame.key.get_pressed()

    # Move the character (runner) while respecting barriers
    if keys[pygame.K_UP] and runner_y > top_barrier:
        runner_y -= runner_speed
    if keys[pygame.K_DOWN] and runner_y < bottom_barrier:
        runner_y += runner_speed
    if keys[pygame.K_LEFT] and runner_x > left_barrier:
        runner_x -= runner_speed  # Prevent moving past the left barrier
    if keys[pygame.K_RIGHT] and runner_x < right_barrier:
        runner_x += runner_speed  # Prevent moving past the right barrier

    # Move the houses relative to the character's movement
    house1_y += runner_speed
    house2_y += runner_speed

    # Reset house position to create an infinite scrolling effect
    if house1_y > HEIGHT:
        house1_y = -house_height
    if house2_y > HEIGHT:
        house2_y = -house_height

    # DRAWING
    screen.fill(WHITE)  # Background color

    # Draw the houses on the sides
    pygame.draw.rect(screen, BLACK, (house1_x, house1_y, house_width, house_height))  # House body
    pygame.draw.polygon(screen, BLACK, [(house1_x, house1_y), 
    (house1_x + house_width // 2, house1_y - 20), 
    (house1_x + house_width, house1_y)])  # Roof

    pygame.draw.rect(screen, BLACK, (house2_x, house2_y, house_width, house_height))  # House body
    pygame.draw.polygon(screen, BLACK, [(house2_x, house2_y), 
    (house2_x + house_width // 2, house2_y - 20), 
    (house2_x + house_width, house2_y)])  # Roof

    # Draw the runner (centered square)
    pygame.draw.rect(screen, BLACK, (runner_x - 10, runner_y - 10, 20, 20))

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
