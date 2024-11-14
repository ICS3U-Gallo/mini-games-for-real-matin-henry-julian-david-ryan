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
DARK_GREEN = (0, 100, 0)
SILVER = (192, 192, 192)
GREY = (169, 169, 169)
GOLD = (255, 215, 0)
DARK_RED = (139, 0, 0)
DARK_GREEN_2 = (0, 100, 0)
LIGHT_CHRISTMAS_GREEN = (144, 238, 144)

# Font setup
font = pygame.font.Font(None, 25)  # Reduced font size for better fit in instructions
large_font = pygame.font.Font(None, 35)  # Adjusted for title

# Game state variables
running = True
in_menu = True
show_instructions = False
in_game = False
hearts = 3
presents_collected = 0

# Snowflakes setup
snowflakes = [[random.randint(0, WIDTH), random.randint(-HEIGHT, 0), random.randint(2, 5), random.uniform(1, 3)] for _ in range(100)]

# Game variables
runner_x = WIDTH // 2
runner_y = HEIGHT // 2
runner_speed = 5
runner_radius = 10

# House setup
house_width = 40
house_height = 40
house1_x = 50
house2_x = WIDTH - house_width - 50

# Tree setup
tree_width = 40
tree_height = 60

# Tree and house scrolling
spacing = 250
scroll_speed = 3
house_tree_positions = [-spacing * i for i in range(3)]

# Snowball shooter variables
snowball_speed = 5
snowballs = []
shooters = [[WIDTH // 2, HEIGHT - 30, 2]]

# Barrier setup
left_barrier = 105
right_barrier = WIDTH - 105 - house_width
top_barrier = 50
bottom_barrier = HEIGHT - 50

# Presents setup
presents = []
present_spawn_chance = 0.01

# Red Presents setup
red_presents = []
red_present_spawn_chance = 0.001

# Magic Presents setup
blue_presents = []
blue_present_spawn_chance = 0.00001

# Grinch setup
grinches = []
grinch_spawn_intervals = [5, 10, 13]

# Main game loop
while running:
   while running:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if in_menu:
        if keys[pygame.K_RETURN]:
            if show_instructions:
                show_instructions = False
            else:
                in_menu = False
                in_game = True
                hearts = 3
                presents_collected = 0
        elif keys[pygame.K_i]:
            show_instructions = not show_instructions
        elif keys[pygame.K_q]:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                show_instructions = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:  # Go back to the menu
                    show_instructions = False
                    in_menu = True

        # --- DRAWING (Menu & Instructions) ---
        screen.fill(LIGHT_BLUE)  # Light blue background for snow visibility

        # Present Drawing
        def draw_present(x, y):
            # Draw the box of the present
            pygame.draw.rect(screen, RED, (x, y, 20, 20))  # Main box (red)
            
            # Draw the ribbon crossing the present (horizontal and vertical)
            pygame.draw.rect(screen, GREEN, (x + 5, y, 10, 5))  # Horizontal ribbon
            pygame.draw.rect(screen, GREEN, (x + 5, y + 5, 5, 10))  # Vertical ribbon
            
            # Draw the bow on top of the present
            pygame.draw.circle(screen, YELLOW, (x + 10, y - 5), 5)  # Bow circle
            pygame.draw.line(screen, YELLOW, (x + 10, y - 5), (x + 10, y - 10), 3)  # Bow top line
            pygame.draw.line(screen, YELLOW, (x + 10, y - 5), (x + 5, y), 3)  # Left bow line
            pygame.draw.line(screen, YELLOW, (x + 10, y - 5), (x + 15, y), 3)  # Right bow line

        # Snowflake effect on the menu
        for snowflake in snowflakes:
            snowflake[1] += snowflake[3]
            if snowflake[1] > HEIGHT:
                snowflake[1] = random.randint(-HEIGHT, 0)
                snowflake[0] = random.randint(0, WIDTH)
            pygame.draw.circle(screen, WHITE, (int(snowflake[0]), int(snowflake[1])), snowflake[2])

        # Draw striped silver box in the middle
        box_width, box_height = 400, 300
        box_x, box_y = (WIDTH - box_width) // 2, (HEIGHT - box_height) // 2

        # Draw border layers
        pygame.draw.rect(screen, LIGHT_CHRISTMAS_GREEN, (box_x - 10, box_y - 10, box_width + 20, box_height + 20))  # Green border
        pygame.draw.rect(screen, DARK_RED, (box_x - 5, box_y - 5, box_width + 10, box_height + 10))      # Red border
        pygame.draw.rect(screen, WHITE, (box_x - 3, box_y - 3, box_width + 6, box_height + 6))      # White border

        if show_instructions:
            # Instructions screen
            title_text = large_font.render("Instructions", True, DARK_RED)
            instructions_text = font.render("Collect presents to give to Santa!", True, BLACK)
            instructions_text2 = font.render("Use arrow keys to move.", True, BLACK)
            instructions_text3 = font.render("Evade the snowballs being thrown at you!", True, BLACK)
            back_text = font.render("Press R to go back.", True, GOLD)

            # Display the instructions
            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, box_y + 20))
            screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, box_y + 80))
            screen.blit(instructions_text2, (WIDTH // 2 - instructions_text2.get_width() // 2, box_y + 160))
            screen.blit(instructions_text3, (WIDTH // 2 - instructions_text3.get_width() // 2, box_y + 120))
            screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, box_y + box_height - 60))
        else:
            # Main menu
            title_text = large_font.render("CHRISTMAS PRESENT PURSUIT!", True, GOLD)
            start_text = font.render("Press Enter to Start", True, GOLD)
            instructions_button = font.render("Press I for Instructions", True, GOLD)
            quit_text = font.render("Press Q to Quit", True, GOLD)

            # Display the main menu text
            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, box_y + 5))
            screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, box_y + box_height - 80))
            screen.blit(instructions_button, (WIDTH // 2 - instructions_button.get_width() // 2, box_y + box_height - 120))
            screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, box_y + box_height - 40))

            # Draw a smaller Christmas tree
            tree_x, tree_y = WIDTH // 2, box_y + 100
            pygame.draw.polygon(screen, DARK_GREEN_2, [(tree_x, tree_y - 30), (tree_x - 30, tree_y + 10), (tree_x + 30, tree_y + 10)])  # Top layer
            pygame.draw.polygon(screen, DARK_GREEN_2, [(tree_x, tree_y - 0), (tree_x - 40, tree_y + 30), (tree_x + 40, tree_y + 30)])  # Middle layer
            pygame.draw.polygon(screen, DARK_GREEN_2, [(tree_x, tree_y + 10), (tree_x - 50, tree_y + 50), (tree_x + 50, tree_y + 50)])  # Bottom layer
            pygame.draw.rect(screen, BROWN, (tree_x - 8, tree_y + 50, 16, 20))  # Tree trunk

            # Add ornaments (red and yellow)
            pygame.draw.circle(screen, RED, (tree_x - 15, tree_y), 6)  # Red ornament on left
            pygame.draw.circle(screen, YELLOW, (tree_x + 15, tree_y), 6)  # Yellow ornament on right
            pygame.draw.circle(screen, RED, (tree_x, tree_y - 25), 6)  # Red ornament on top layer
            pygame.draw.circle(screen, YELLOW, (tree_x - 20, tree_y + 25), 6)  # Yellow ornament on middle layer
            pygame.draw.circle(screen, RED, (tree_x + 20, tree_y + 45), 6)  # Red ornament on bottom layer

            draw_present(WIDTH // 2 + 60, HEIGHT // 2 - 5)  # First present beside the first tree
            draw_present(WIDTH // 2 - 80, HEIGHT // 2 - 5)

            # Star on top of the tree
            pygame.draw.circle(screen, GOLD, (tree_x, tree_y - 40), 8)  # Star on top

        pygame.display.flip()

    elif in_game:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and runner_y > top_barrier:
            runner_y -= runner_speed
        if keys[pygame.K_DOWN] and runner_y < bottom_barrier:
            runner_y += runner_speed
        if keys[pygame.K_LEFT] and runner_x > left_barrier:
            runner_x -= runner_speed
        if keys[pygame.K_RIGHT] and runner_x < right_barrier:
            runner_x += runner_speed

        # Scroll houses and trees
        for i in range(len(house_tree_positions)):
            house_tree_positions[i] += scroll_speed
            if house_tree_positions[i] > HEIGHT:
                house_tree_positions[i] = -spacing * (len(house_tree_positions) - 1)

        # Move and add shooters as presents are collected
        if presents_collected == 4 and len(shooters) == 1:
            shooters.append([WIDTH // 4, HEIGHT - 30, 2])
        if presents_collected == 7 and len(shooters) == 2:
            shooters.append([3 * WIDTH // 4, HEIGHT - 30, 2])

        # Add Grinches at specific intervals
        if presents_collected in grinch_spawn_intervals:
            grinches.append([random.randint(left_barrier, right_barrier), -30])

        # Update shooters and snowballs
        for shooter in shooters:
            shooter[0] += shooter[2]
            if shooter[0] <= left_barrier or shooter[0] >= right_barrier:
                shooter[2] *= -1
            if random.random() < 0.03:
                snowballs.append([shooter[0], shooter[1]])

        # Move snowballs and check for collisions
        for snowball in snowballs:
            snowball[1] -= snowball_speed
            if snowball[1] < 0:
                snowballs.remove(snowball)

        for snowball in snowballs[:]:
            if runner_x - runner_radius < snowball[0] < runner_x + runner_radius and runner_y - runner_radius < snowball[1] < runner_y + runner_radius:
                hearts -= 1
                snowballs.remove(snowball)
                if hearts <= 0:
                    in_game = False
                    in_menu = True

        # Spawn and collect presents
        if random.random() < present_spawn_chance:
            present_x = random.randint(left_barrier, right_barrier)
            present_y = random.randint(top_barrier, bottom_barrier)
            presents.append([present_x, present_y])

        for present in presents[:]:
            if runner_x - runner_radius < present[0] < runner_x + runner_radius and runner_y - runner_radius < present[1] < runner_y + runner_radius:
                presents_collected += 1
                presents.remove(present)
                if presents_collected % 2 == 0:
                    snowball_speed += 1
                if presents_collected == 14:
                    snowball_speed += 1  # Increase snowball size at 14 presents
                if presents_collected >= 15:
                    win_text = large_font.render("You Win!", True, GREEN)
                    screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    in_game = False
                    in_menu = True

        # --- DRAWING ---
        screen.fill(LIGHT_BLUE)

        # Snowfall effect
        for snowflake in snowflakes:
            snowflake[1] += snowflake[3]
            if snowflake[1] > HEIGHT:
                snowflake[1] = random.randint(-HEIGHT, 0)
                snowflake[0] = random.randint(0, WIDTH)
            pygame.draw.circle(screen, WHITE, (int(snowflake[0]), int(snowflake[1])), snowflake[2])

        for pos in house_tree_positions:
            # Draw houses with windows, door, roof, and snow
            pygame.draw.rect(screen, BROWN, (house1_x, pos, house_width, house_height))
            pygame.draw.rect(screen, BROWN, (house2_x, pos, house_width, house_height))
            pygame.draw.rect(screen, RED, (house1_x + 5, pos + 10, 10, 10))  # Door on house 1
            pygame.draw.rect(screen, RED, (house2_x + 5, pos + 10, 10, 10))  # Door on house 2
            pygame.draw.rect(screen, WHITE, (house1_x + 5, pos + 5, 10, 10))  # Window on house 1
            pygame.draw.rect(screen, WHITE, (house2_x + 5, pos + 5, 10, 10))  # Window on house 2
            pygame.draw.polygon(screen, BROWN, [(house1_x - 5, pos), (house1_x + house_width + 5, pos), (house1_x + house_width // 2, pos - 10)])  # Roof on house 1
            pygame.draw.polygon(screen, BROWN, [(house2_x - 5, pos), (house2_x + house_width + 5, pos), (house2_x + house_width // 2, pos - 10)])  # Roof on house 2

            # Draw trees above the houses
            pygame.draw.polygon(screen, DARK_GREEN, [(house1_x - 15, pos - 80), (house1_x + house_width + 15, pos - 80), (house1_x + house_width // 2, pos - 120)])  # Tree top
            pygame.draw.rect(screen, BROWN, (house1_x + house_width // 2 - 5, pos - 80, 10, 20))  # Tree trunk
            pygame.draw.polygon(screen, DARK_GREEN, [(house2_x - 15, pos - 80), (house2_x + house_width + 15, pos - 80), (house2_x + house_width // 2, pos - 120)])  # Tree top
            pygame.draw.rect(screen, BROWN, (house2_x + house_width // 2 - 5, pos - 80, 10, 20))  # Tree trunk

        # Draw shooter
        for shooter in shooters:
            pygame.draw.rect(screen, GREEN, (shooter[0] - 15, shooter[1] - 20, 30, 20))
            pygame.draw.circle(screen, RED, (shooter[0], shooter[1] - 10), 10)

        # Draw player (runner)
        pygame.draw.circle(screen, BLUE, (runner_x, runner_y), runner_radius)

        # Draw presents
        for present in presents:
            pygame.draw.rect(screen, YELLOW, (present[0] - 5, present[1] - 5, 10, 10))

        # Draw snowballs
        for snowball in snowballs:
            snowball_radius = 5
            if presents_collected >= 14:
                snowball_radius = 10  # Make snowballs larger at 14 presents
            pygame.draw.circle(screen, SILVER, (snowball[0], snowball[1]), snowball_radius)

        # Draw hearts
        for i in range(hearts):
            pygame.draw.circle(screen, RED, (20 + i * 30, 20), 10)

        # Draw presents collected
        presents_text = font.render("Presents: " + str(presents_collected), True, BLACK)
        screen.blit(presents_text, (WIDTH - presents_text.get_width() - 20, 20))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
