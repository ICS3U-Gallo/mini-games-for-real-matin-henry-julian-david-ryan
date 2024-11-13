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
SILVER     = (192, 192, 192)

# Font setup
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 48)

# Game state variables
running = True
in_menu = True
show_instructions = True
in_game = False
hearts = 3
presents_collected = 0

# Game variables
runner_x = WIDTH // 2
runner_y = HEIGHT // 2
runner_speed = 5
runner_radius = 10  # Smaller player size

# House setup
house_width = 30
house_height = 30
house1_x = 50
house2_x = WIDTH - house_width - 50

# Tree setup
tree_width = 30
tree_height = 40

# Tree and house scrolling
spacing = 200
scroll_speed = 5
house_tree_positions = [-spacing * i for i in range(3)]

# Snowball shooter variables
snowball_speed = 5
snowballs = []
shooters = [[WIDTH // 2, HEIGHT - 30, 2]]  # list of [x, y, direction] for each shooter

# Barrier setup
left_barrier = 50
right_barrier = WIDTH - 50 - house_width
top_barrier = 50
bottom_barrier = HEIGHT - 50

# Snowflakes setup
snowflakes = [[random.randint(0, WIDTH), random.randint(-HEIGHT, 0), random.randint(2, 5), random.uniform(1, 3)] for _ in range(100)]

# Presents setup
presents = []
present_spawn_chance = 0.01  # 1% chance to spawn a present each frame

# Main game loop
while running:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if in_menu:
        keys = pygame.key.get_pressed()

        if show_instructions:
            if keys[pygame.K_RETURN]:
                show_instructions = False
        else:
            if keys[pygame.K_RETURN]:
                in_menu = False
                in_game = True
                hearts = 3
                presents_collected = 0
                snowballs = []
                shooters = [[WIDTH // 2, HEIGHT - 30, 2]]  # Reset to one shooter
            elif keys[pygame.K_q]:
                running = False

        # --- DRAWING (Menu & Instructions) ---
        screen.fill(WHITE)

        # Snowflake effect on the menu
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
            # Draw Christmas tree in the menu
            pygame.draw.polygon(screen, DARK_GREEN, [(WIDTH // 2, HEIGHT // 4), (WIDTH // 2 - 40, HEIGHT // 2), (WIDTH // 2 + 40, HEIGHT // 2)])
            pygame.draw.polygon(screen, DARK_GREEN, [(WIDTH // 2, HEIGHT // 4 + 30), (WIDTH // 2 - 30, HEIGHT // 2 - 10), (WIDTH // 2 + 30, HEIGHT // 2 - 10)])
            pygame.draw.rect(screen, BROWN, (WIDTH // 2 - 10, HEIGHT // 2, 20, 20))
            pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 4), 8)  # Star on the tree

            title_text = large_font.render("Merry Christmas!", True, RED)
            start_text = font.render("Press Enter to Start", True, GREEN)
            quit_text = font.render("Press Q to Quit", True, GREEN)

            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4 + 70))
            screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 40))
            screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 80))

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

        # Update shooters and snowballs
        for shooter in shooters:
            shooter[0] += shooter[2]
            if shooter[0] <= left_barrier or shooter[0] >= right_barrier:
                shooter[2] *= -1
            if random.random() < 0.03:
                snowballs.append([shooter[0], shooter[1]])

        # Move snowballs
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
                if presents_collected >= 10:
                    win_text = large_font.render("You Win!", True, GREEN)
                    screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    in_game = False
                    in_menu = True

        # --- DRAWING ---
        screen.fill(WHITE)

        # Snowfall effect
        for snowflake in snowflakes:
            snowflake[1] += snowflake[3]
            if snowflake[1] > HEIGHT:
                snowflake[1] = random.randint(-HEIGHT, 0)
                snowflake[0] = random.randint(0, WIDTH)
            pygame.draw.circle(screen, WHITE, (int(snowflake[0]), int(snowflake[1])), snowflake[2])

        # Draw Christmas trees and houses
        for pos in house_tree_positions:
            pygame.draw.polygon(screen, DARK_GREEN, [(50, pos), (20, pos + 60), (80, pos + 60)])  # Christmas tree
            pygame.draw.polygon(screen, DARK_GREEN, [(50, pos + 20), (30, pos + 80), (70, pos + 80)])  # Lower branches
            pygame.draw.rect(screen, BROWN, (45, pos + 50, 10, 10))  # Trunk
            pygame.draw.rect(screen, LIGHT_BLUE, (house1_x, pos, house_width, house_height))
            pygame.draw.rect(screen, LIGHT_BLUE, (house2_x, pos, house_width, house_height))
            pygame.draw.rect(screen, RED, (house1_x + 5, pos + 10, 10, 10))  # Door on house
            pygame.draw.rect(screen, RED, (house2_x + 5, pos + 10, 10, 10))  # Door on house

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
            pygame.draw.circle(screen, SILVER   , (snowball[0], snowball[1]), 5)

        # Draw hearts
        for i in range(hearts):
            pygame.draw.circle(screen, RED, (20 + i * 30, 20), 10)

        # Draw presents collected
        presents_text = font.render("Presents: " + str(presents_collected), True, BLACK)
        screen.blit(presents_text, (WIDTH - presents_text.get_width() - 20, 20))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
