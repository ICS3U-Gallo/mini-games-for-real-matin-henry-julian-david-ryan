import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Christmas Flappy Bird")

# Colors and game assets
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BIRD_SIZE = 40
PIPE_WIDTH = 60
PIPE_HEIGHT = 400
GAP_SIZE = 150
BIRD_X = 100
BIRD_Y = SCREEN_HEIGHT // 2

# Game variables
bird_y = BIRD_Y
bird_velocity = 0
gravity = 0.5
flap_strength = -8
score = 0
game_active = False

pipes = []
pipe_speed = 3
pipe_frequency = 1500  # milliseconds
last_pipe = pygame.time.get_ticks()

# Font for score
font = pygame.font.Font(None, 36)

# Helper function to create pipes
def create_pipe():
    y_pos = random.randint(GAP_SIZE, SCREEN_HEIGHT - GAP_SIZE)
    top_pipe = {"x": SCREEN_WIDTH, "y": y_pos - PIPE_HEIGHT, "color": RED}
    bottom_pipe = {"x": SCREEN_WIDTH, "y": y_pos + GAP_SIZE, "color": RED}
    return top_pipe, bottom_pipe

# Function to display start screen with a "Play" button
def start_screen():
    screen.fill(WHITE)
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Christmas Flappy Bird", True, RED)
    play_text = font.render("Play", True, WHITE)
    
    # Positioning text and button
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))
    
    play_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 50)
    pygame.draw.rect(screen, GREEN, play_button)
    screen.blit(play_text, (play_button.x + play_button.width // 2 - play_text.get_width() // 2,
                            play_button.y + play_button.height // 2 - play_text.get_height() // 2))
    
    pygame.display.flip()
    return play_button

# Main game loop
running = True
clock = pygame.time.Clock()

# Initial start screen
while running:
    clock.tick(60)
    play_button = start_screen()
    
    # Wait for user to press "Play"
    while not game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_active = True  # End inner loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game_active = True  # Start the game

    # Game loop
    while game_active:
        clock.tick(60)
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_velocity = flap_strength

        # Bird movement
        bird_velocity += gravity
        bird_y += bird_velocity
        bird_rect = pygame.Rect(BIRD_X, bird_y, BIRD_SIZE, BIRD_SIZE)

        # Draw bird as a circle with an eye
        pygame.draw.circle(screen, YELLOW, (BIRD_X + BIRD_SIZE // 2, int(bird_y) + BIRD_SIZE // 2), BIRD_SIZE // 2)
        pygame.draw.circle(screen, BLACK, (BIRD_X + BIRD_SIZE // 2 + 10, int(bird_y) + BIRD_SIZE // 2 - 10), 5)  # Eye

        # Create new pipes
        current_time = pygame.time.get_ticks()
        if current_time - last_pipe > pipe_frequency:
            pipes.extend(create_pipe())
            last_pipe = current_time

        # Move and draw pipes
        for pipe in pipes:
            pipe["x"] -= pipe_speed
            pipe_rect = pygame.Rect(pipe["x"], pipe["y"], PIPE_WIDTH, PIPE_HEIGHT)
            pygame.draw.rect(screen, pipe["color"], pipe_rect)

            # Collision check
            if bird_rect.colliderect(pipe_rect):
                game_active = False  # End game on collision

        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if pipe["x"] > -PIPE_WIDTH]

        # Scoring
        for pipe in pipes:
            if pipe["x"] + PIPE_WIDTH < BIRD_X and "scored" not in pipe:
                score += 1
                pipe["scored"] = True  # Mark this pipe as scored

        # Draw score
        score_text = font.render(f"Score: {score}", True, RED)
        screen.blit(score_text, (10, 10))

        # Check for out-of-bounds bird
        if bird_y < 0 or bird_y > SCREEN_HEIGHT - BIRD_SIZE:
            game_active = False  # End game if bird goes off-screen

        pygame.display.flip()

    # Reset variables if the game restarts
    bird_y = BIRD_Y
    bird_velocity = 0
    pipes.clear()
    score = 0
    game_active = False

# Quit Pygame
pygame.quit()
