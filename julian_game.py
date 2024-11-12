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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (165, 42, 42)
LIGHT_BLUE = (173, 216, 230)

# Font setup
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 48)

# Game state variables
running = True
in_menu = True
show_instructions = True
in_game = False
hearts = 3

# Game variables
runner_x = WIDTH // 2
runner_y = HEIGHT // 2
runner_speed = 5
runner_radius = 10  # Smaller player size

# House setup
house_width = 30
house_height = 30
house1_x = 50  # House 1 on the left
house2_x = WIDTH - house_width - 50  # House 2 on the right

# Tree setup
tree_width = 40
tree_height = 40  # Size of the trees

# Tree and house scrolling
spacing = 200  # Space between each house and tree set
scroll_speed = 5
house_tree_positions = [-spacing * i for i in range(3)]  # Three sets of positions, spaced out

# Snowball shooter variables
snowball_speed = 5
snowballs = []
shooter_x = WIDTH // 2
shooter_y = HEIGHT - 30
shooter_direction = 2  # Shooter's movement speed

# Barrier setup
left_barrier = 50
right_barrier = WIDTH - 50 - house_width
top_barrier = 50
bottom_barrier = HEIGHT - 50

# Snowflakes setup
snowflakes = []
for _ in range(100):
    snowflake_x = random.randint(0, WIDTH)
    snowflake_y = random.randint(-HEIGHT, 0)
    snowflake_size = random.randint(2, 5)
    snowflake_speed = random.uniform(1, 3)
    snowflakes.append([snowflake_x, snowflake_y, snowflake_size, snowflake_speed])

# Function to reset the game
def reset_game():
    global hearts, snowballs
    hearts = 3
    snowballs = []
    runner_x, runner_y = WIDTH // 2, HEIGHT // 2

# Main game loop
while running:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if in_menu:
        keys = pygame.key.get_pressed()

        # Show instructions screen before game starts
        if show_instructions:
            if keys[pygame.K_RETURN]:  # Continue to main menu
                show_instructions = False
        else:
            if keys[pygame.K_RETURN]:  # Start game
                in_menu = False
                in_game = True
                reset_game()

            elif keys[pygame.K_q]:  # Quit game
                running = False

        # --- DRAWING (Menu & Instructions) ---
        screen.fill(WHITE)

        # Draw snowflakes in menu
        for snowflake in snowflakes:
            snowflake[1] += snowflake[3]
            if snowflake[1] > HEIGHT:
                snowflake[1] = random.randint(-HEIGHT, 0)
                snowflake[0] = random.randint(0, WIDTH)
            pygame.draw.circle(screen, WHITE, (int(snowflake[0]), int(snowflake[1])), snowflake[2])

        if show_instructions:
            instructions_text = font.render("Use Arrow Keys to Move", True, BLUE)
            avoid_text = font.render("Avoid Snowballs from the Shooter!", True, RED)
            hearts_text = font.render("You have 3 hearts. Good luck!", True, GREEN)
            continue_text = font.render("Press Enter to Continue", True, BLACK)

            screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 4))
            screen.blit(avoid_text, (WIDTH // 2 - avoid_text.get_width() // 2, HEIGHT // 4 + 40))
            screen.blit(hearts_text, (WIDTH // 2 - hearts_text.get_width() // 2, HEIGHT // 4 + 80))
            screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 2))

        else:
            title_text = large_font.render("Merry Christmas!", True, RED)
            start_text = font.render("Press Enter to Start", True, GREEN)
            quit_text = font.render("Press Q to Quit", True, GREEN)

            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
            screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - 40))
            screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 40))

        pygame.display.flip()

    elif in_game:
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

        # Update positions of houses and trees for even spacing and infinite scrolling
        for i in range(len(house_tree_positions)):
            house_tree_positions[i] += scroll_speed
            if house_tree_positions[i] > HEIGHT:
                house_tree_positions[i] = -spacing * (len(house_tree_positions) - 1)

        # Move the shooter side to side
        shooter_x += shooter_direction
        if shooter_x <= 50 or shooter_x >= WIDTH - 50:
            shooter_direction *= -1  # Reverse direction at the edges

        # Snowball shooting mechanism
        if random.random() < 0.03:  # 3% chance to shoot a snowball each frame
            snowballs.append([shooter_x, shooter_y])

        # Update snowball positions
        for snowball in snowballs:
            snowball[1] -= snowball_speed
            if snowball[1] < 0:
                snowballs.remove(snowball)

        # Check for collisions between runner and snowballs
        for snowball in snowballs[:]:
            if runner_x - runner_radius < snowball[0] < runner_x + runner_radius and runner_y - runner_radius < snowball[1] < runner_y + runner_radius:
                hearts -= 1
                snowballs.remove(snowball)
                if hearts <= 0:
                    in_game = False
                    in_menu = True

        # --- DRAWING (Game Loop) ---
        screen.fill(WHITE)

        # Draw snowflakes
        for snowflake in snowflakes:
            snowflake[1] += snowflake[3]
            if snowflake[1] > HEIGHT:
                snowflake[1] = random.randint(-HEIGHT, 0)
                snowflake[0] = random.randint(0, WIDTH)
            pygame.draw.circle(screen, WHITE, (int(snowflake[0]), int(snowflake[1])), snowflake[2])

        # Draw houses and trees beyond the barrier
        for y_position in house_tree_positions:
            # Draw house 1 on the left, beyond the barrier
            pygame.draw.rect(screen, BROWN, (house1_x - 50, y_position, house_width, house_height))  # House body
            pygame.draw.polygon(screen, BROWN, [(house1_x - 50, y_position), 
                                               (house1_x - 50 + house_width // 2, y_position - 20), 
                                               (house1_x - 50 + house_width, y_position)])  # Roof
            pygame.draw.rect(screen, YELLOW, (house1_x - 50 + 5, y_position + 5, 10, 10))  # Window

            # Draw tree above house 1
            tree1_x = house1_x - 50 + (house_width // 2) - (tree_width // 2)  # Center the tree above the house
            tree1_y = y_position - tree_height - 10  # Position the tree higher above the house
            pygame.draw.polygon(screen, GREEN, [(tree1_x, tree1_y), 
                                                (tree1_x + tree_width // 2, tree1_y - tree_height), 
                                                (tree1_x + tree_width, tree1_y)])  # Tree top
            pygame.draw.rect(screen, BROWN, (tree1_x + (tree_width // 2) - 5, tree1_y, 10, 20))  # Tree trunk

            # Draw house 2 on the right, beyond the barrier
            pygame.draw.rect(screen, BROWN, (house2_x + 50, y_position, house_width, house_height))  # House body
            pygame.draw.polygon(screen, BROWN, [(house2_x + 50, y_position), 
                                               (house2_x + 50 + house_width // 2, y_position - 20), 
                                               (house2_x + 50 + house_width, y_position)])  # Roof
            pygame.draw.rect(screen, YELLOW, (house2_x + 50 + 5, y_position + 5, 10, 10))  # Window

            # Draw tree above house 2
            tree2_x = house2_x + 50 + (house_width // 2) - (tree_width // 2)  # Center the tree above the house
            tree2_y = y_position - tree_height - 10  # Position the tree higher above the house
            pygame.draw.polygon(screen, GREEN, [(tree2_x, tree2_y), 
                                                (tree2_x + tree_width // 2, tree2_y - tree_height), 
                                                (tree2_x + tree_width, tree2_y)])  # Tree top
            pygame.draw.rect(screen, BROWN, (tree2_x + (tree_width // 2) - 5, tree2_y, 10, 20))  # Tree trunk

        # Draw snowballs
        for snowball in snowballs:
            pygame.draw.circle(screen, LIGHT_BLUE, (int(snowball[0]), int(snowball[1])), 5)

        # Draw shooter at the bottom of the screen
        pygame.draw.rect(screen, BROWN, (shooter_x - 15, shooter_y, 30, 10))  # Shooter base
        pygame.draw.polygon(screen, BROWN, [(shooter_x - 5, shooter_y - 10), 
                                            (shooter_x + 5, shooter_y - 20), 
                                            (shooter_x + 15, shooter_y - 10)])  # Shooter nozzle

        # Draw runner (player)
        pygame.draw.circle(screen, BLUE, (runner_x, runner_y), runner_radius)

        # Display hearts
        hearts_text = font.render(f"Hearts: {hearts}", True, RED)
        screen.blit(hearts_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
