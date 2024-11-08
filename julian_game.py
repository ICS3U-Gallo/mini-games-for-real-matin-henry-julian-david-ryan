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

# Font setup
font = pygame.font.Font(None, 36)

# Game state variables
running = True
in_menu = True

# Game variables
runner_x = WIDTH // 2
runner_y = HEIGHT // 2
runner_speed = 5

house_width = 30
house_height = 30
house1_x = 0
house1_y = random.randint(-HEIGHT, 0)
house2_x = WIDTH - house_width
house2_y = random.randint(-HEIGHT, 0)

# Barrier setup
left_barrier = 50
right_barrier = WIDTH - 50 - house_width
top_barrier = 50
bottom_barrier = HEIGHT - 50

# Main game loop with menu
while running:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if in_menu:
        # Handle key presses in the menu
        keys = pygame.key.get_pressed()

        # Main menu interaction
        if keys[pygame.K_RETURN]:  # Start game
            in_menu = False
            # Reset game variables
            runner_x = WIDTH // 2
            runner_y = HEIGHT // 2
            house1_y = random.randint(-HEIGHT, 0)
            house2_y = random.randint(-HEIGHT, 0)

        elif keys[pygame.K_i]:  # Instructions
            show_instructions = True
            while show_instructions:
                screen.fill(WHITE)
                instructions_title = font.render("Instructions", True, BLACK)
                controls_text = font.render("Use Arrow keys to move: Up, Down, Left, Right", True, BLACK)
                gameplay_text = font.render("Avoid obstacles and reach the goal!", True, BLACK)
                back_text = font.render("Press 'B' to go back", True, BLACK)

                screen.blit(instructions_title, (WIDTH // 2 - instructions_title.get_width() // 2, HEIGHT // 4))
                screen.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT // 2 - 40))
                screen.blit(gameplay_text, (WIDTH // 2 - gameplay_text.get_width() // 2, HEIGHT // 2))
                screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT // 2 + 40))

                pygame.display.flip()

                # Handle back action
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        show_instructions = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_b:  # Go back to the menu
                            show_instructions = False
                            in_menu = True

        elif keys[pygame.K_q]:  # Quit game
            running = False

        # --- DRAWING (Main Menu) ---
        screen.fill(WHITE)
        title_text = font.render("Main Menu", True, BLACK)
        start_text = font.render("Press Enter to Start", True, BLACK)
        instructions_text = font.render("Press I for Instructions", True, BLACK)
        quit_text = font.render("Press Q to Quit", True, BLACK)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 40))

        pygame.display.flip()

    else:  # --- GAME STATE UPDATES (If not in menu) ---
        keys = pygame.key.get_pressed()

        # Move the character (runner) while respecting barriers
        if keys[pygame.K_UP] and runner_y > top_barrier:
            runner_y -= runner_speed
        if keys[pygame.K_DOWN] and runner_y < bottom_barrier:
            runner_y += runner_speed
        if keys[pygame.K_LEFT] and runner_x > left_barrier:
            runner_x -= runner_speed
        if keys[pygame.K_RIGHT] and runner_x < right_barrier:
            runner_x += runner_speed

        # Move the houses relative to the character's movement
        house1_y += runner_speed
        house2_y += runner_speed

        # Reset house position to create an infinite scrolling effect
        if house1_y > HEIGHT:
            house1_y = -house_height
        if house2_y > HEIGHT:
            house2_y = -house_height

        # --- DRAWING (Game Loop) ---
        screen.fill(WHITE)

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

        pygame.display.flip()
        clock.tick(30)

pygame.quit()
