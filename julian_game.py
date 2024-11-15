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
GRAY = (169, 169, 169) 

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

# Define positions for each Grinch shooter (x, y) pairs
shooters = [
    [150, 100],  # Shooter 1 position
    [450, 150],  # Shooter 2 position
    [600, 250]   # Shooter 3 position
]

# Shooter speed
shooter_speed = 2  # Speed at which shooters move

# Snowflakes setup
snowflakes = [[random.randint(0, WIDTH), random.randint(-HEIGHT, 0), random.randint(2, 5), random.uniform(0.03, 0.5)] for _ in range(100)]

# Define light positions and colors
light_positions = [(x, 30) for x in range(50, WIDTH - 50, 50)]  # Positions spaced along the width
light_colors = [RED, GREEN, BLUE, YELLOW]  # Light colors for a festive look

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

# Ground dimensions
road_y = 300  # Y position for the top of the road
road_height = 200  # Height of the road
screen_width = 800  # Width of the screen
screen_height = 600  # Height of the screen

#Game Ground dimensions
road_width = 200  # Width of the road
sidewalk_width = (screen_width - road_width - 100) //2  # Width of each sidewalk

# Tree and house scrolling
spacing = 250
scroll_speed = 3
house_tree_positions = [-spacing * i for i in range(3)]

# Snowball shooter variables
snowball_speed = 5
snowballs = []
shooters = [[WIDTH // 2, HEIGHT - 30, 2]]

# Barrier setup
left_barrier = 115
right_barrier = WIDTH - 80 - house_width
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
blue_present_spawn_chance = 0.0001

#grinch Presents setup
grinch_presents = []
grinch_present_spawn_chance = 0.002

# Grinch setup
grinches = []
grinch_spawn_intervals = [5, 10, 13]

#Shooter setup
initial_shooters = [[WIDTH // 2, HEIGHT - 30, 2]]
initial_snowball_speed = 5

def reset_game():
    global shooters, snowball_speed, presents_collected, hearts, snowballs, presents
    shooters = initial_shooters.copy()  # Reset to one shooter at the center
    snowball_speed = initial_snowball_speed  # Reset snowball speed to the starting value
    presents_collected = 0
    hearts = 3
    snowballs.clear()  # Clear all active snowballs
    presents.clear()   # Clear any presents on the screen
    grinch_presents.clear()
    blue_presents.clear()
    red_presents.clear()

# Main game loop
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
                    reset_game()

        # --- DRAWING (Menu & Instructions) ---
        screen.fill(LIGHT_BLUE)  # Light blue background for snow visibility

        # Draw the snowy grass (top section)
        pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, screen_width, road_y))

        # Draw the road (bottom section)
        pygame.draw.rect(screen, GRAY, (0, road_y, screen_width, road_height))

        # Draw the black border line separating the snowy grass and the road
        pygame.draw.line(screen, BLACK, (0, road_y), (screen_width, road_y), 5)

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

        # Draw the string (a line)
        pygame.draw.line(screen, BLACK, (0, 30), (WIDTH, 30), 2)

        # Draw the lights along the string
        for i, pos in enumerate(light_positions):
            pygame.draw.circle(screen, light_colors[i % len(light_colors)], pos, 10)  # Cycle through colors

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
            back_text = font.render("Press Enter to start the Game.", True, GOLD)

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

            # Spawn and collect red presents for extra heart
        if random.random() < red_present_spawn_chance:
            red_present_x = random.randint(left_barrier, right_barrier)
            red_present_y = random.randint(top_barrier, bottom_barrier)
            red_presents.append([red_present_x, red_present_y])

        # Spawn and collect blue presents for removing a shooter
        if random.random() < blue_present_spawn_chance:
            blue_present_x = random.randint(left_barrier, right_barrier)
            blue_present_y = random.randint(top_barrier, bottom_barrier)
            blue_presents.append([blue_present_x, blue_present_y])

        # Spawn and collect presents
        if random.random() < present_spawn_chance:
            present_x = random.randint(left_barrier, right_barrier)
            present_y = random.randint(top_barrier, bottom_barrier)
            presents.append([present_x, present_y])

        # Collision detection for red presents
        for red_present in red_presents[:]:
            if runner_x - runner_radius < red_present[0] < runner_x + runner_radius and runner_y - runner_radius < red_present[1] < runner_y + runner_radius:
                hearts += 1  # Increase hearts by 1
                red_presents.remove(red_present)  # Remove collected red present

        # Collision detection for blue presents
        for blue_present in blue_presents[:]:
            if runner_x - runner_radius < blue_present[0] < runner_x + runner_radius and runner_y - runner_radius < blue_present[1] < runner_y + runner_radius:
                if shooters:  # Remove a shooter if any exist
                    shooters.pop()
                blue_presents.remove(blue_present)  # Remove collected blue present

                # Spawn Grinch presents with a 0.5% chance
        if random.random() < grinch_present_spawn_chance:
            grinch_x = random.randint(left_barrier, right_barrier)
            grinch_y = random.randint(top_barrier, bottom_barrier)
            grinch_presents.append([grinch_x, grinch_y])

        # Detect collision and apply effects for Grinch presents
        for grinch_present in grinch_presents[:]:
            if (runner_x - runner_radius < grinch_present[0] < runner_x + runner_radius and 
                runner_y - runner_radius < grinch_present[1] < runner_y + runner_radius):
                presents_collected = max(0, presents_collected - 2)  # Reduce by 2, no negative values
                grinch_presents.remove(grinch_present)


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
                    reset_game()

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
                    reset_game()

        # --- DRAWING ---
        screen.fill(LIGHT_BLUE)
                # Draw the left sidewalk starting from left_barrier to the road
        pygame.draw.rect(screen, LIGHT_BLUE, (left_barrier, 0, road_width, screen_height))

        # Draw the road (center vertical section)
        pygame.draw.rect(screen, GRAY, (left_barrier, 0, right_barrier, screen_height))

        # Draw the right sidewalk starting from the end of the road to right_barrier
        pygame.draw.rect(screen, LIGHT_BLUE, (right_barrier, 0, road_width, screen_height))
        
        # Draw black border lines separating the road and sidewalks
        pygame.draw.line(screen, BLACK, (left_barrier, 0), (left_barrier, screen_height), 5)  # Left border of road
        pygame.draw.line(screen, BLACK, (right_barrier, 0), (right_barrier, screen_height), 5)  # Right border of road

        # Draw shooter
        for shooter in shooters:
            # Grinch's head
            pygame.draw.circle(screen, GREEN, (shooter[0], shooter[1]), 10)  # Head
            pygame.draw.circle(screen, BLACK, (shooter[0] - 3, shooter[1] - 3), 2)  # Left eye
            pygame.draw.circle(screen, BLACK, (shooter[0] + 3, shooter[1] - 3), 2)  # Right eye

            # Grinch's mischievous smile
            pygame.draw.arc(screen, BLACK, (shooter[0] - 5, shooter[1] + 2, 10, 5), 0, 3.14, 2)

            # Grinch's body
            pygame.draw.rect(screen, GREEN, (shooter[0] - 8, shooter[1] + 10, 16, 25))

            # Grinch's legs
            pygame.draw.line(screen, GREEN, (shooter[0] - 5, shooter[1] + 35), (shooter[0] - 10, shooter[1] + 45), 3)  # Left leg
            pygame.draw.line(screen, GREEN, (shooter[0] + 5, shooter[1] + 35), (shooter[0] + 10, shooter[1] + 45), 3)  # Right leg

            # Grinch's arms
            pygame.draw.line(screen, GREEN, (shooter[0] - 10, shooter[1] + 15), (shooter[0] - 18, shooter[1] + 25), 3)  # Left arm
            pygame.draw.line(screen, GREEN, (shooter[0] + 10, shooter[1] + 15), (shooter[0] + 18, shooter[1] + 25), 3)  # Right arm

            # Grinch's hat
            pygame.draw.polygon(screen, RED, [(shooter[0] - 8, shooter[1] - 10), (shooter[0] + 8, shooter[1] - 10), (shooter[0], shooter[1] - 25)])
            pygame.draw.circle(screen, WHITE, (shooter[0], shooter[1] - 25), 3)  # White tip of the hat

        # Draw Santa (player) character at the defined position
        pygame.draw.circle(screen, RED, (runner_x, runner_y), 10)  # Head
        pygame.draw.rect(screen, RED, (runner_x - 8, runner_y + 10, 16, 20))  # Body
        pygame.draw.arc(screen, WHITE, (runner_x - 6, runner_y + 15, 12, 8), 3.14, 0, 3)  # Beard
        pygame.draw.polygon(screen, RED, [(runner_x - 10, runner_y - 8), (runner_x + 10, runner_y - 8), (runner_x, runner_y - 20)])  # Hat
        pygame.draw.rect(screen, WHITE, (runner_x - 6, runner_y - 12, 12, 4))  # Hat band


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

        # Standard Present
        for present in presents:
            x, y = present[0], present[1]
            pygame.draw.rect(screen, YELLOW, (x - 10, y - 10, 20, 20))  # Box
            pygame.draw.line(screen, WHITE, (x - 10, y), (x + 10, y), 2)  # Horizontal ribbon
            pygame.draw.line(screen, WHITE, (x, y - 10), (x, y + 10), 2)  # Vertical ribbon

        # Draw red presents (extra heart)
        for red_present in red_presents:
            x, y = red_present[0], red_present[1]
            pygame.draw.rect(screen, RED, (x - 10, y - 10, 20, 20))  # Box
            pygame.draw.line(screen, WHITE, (x - 10, y), (x + 10, y), 2)  # Horizontal ribbon
            pygame.draw.line(screen, WHITE, (x, y - 10), (x, y + 10), 2)  # Vertical ribbon
            # Heart symbol
            pygame.draw.polygon(screen, RED, [(x, y - 3), (x - 4, y + 4), (x + 4, y + 4)])
            
        # Draw blue presents (eliminate a shooter)
        for blue_present in blue_presents:
            x, y = blue_present[0], blue_present[1]
            pygame.draw.rect(screen, BLUE, (x - 10, y - 10, 20, 20))  # Box
            pygame.draw.line(screen, WHITE, (x - 10, y), (x + 10, y), 2)  # Horizontal ribbon
            pygame.draw.line(screen, WHITE, (x, y - 10), (x, y + 10), 2)  # Vertical ribbon
            # Star or dot symbol
            pygame.draw.circle(screen, YELLOW, (x, y), 3)

        #Grinch presents 
        for grinch_present in grinch_presents:
            x, y = grinch_present[0], grinch_present[1]
            pygame.draw.rect(screen, GREEN, (x - 10, y - 10, 20, 20))  # Box
            pygame.draw.line(screen, WHITE, (x - 10, y), (x + 10, y), 2)  # Horizontal ribbon
            pygame.draw.line(screen, WHITE, (x, y - 10), (x, y + 10), 2)  # Vertical ribbon
            # Grinch face details
            pygame.draw.rect(screen, BLACK, (x - 2, y - 5, 4, 1))  # Eyes
            pygame.draw.line(screen, BLACK, (x - 5, y + 5), (x + 5, y + 5), 1)  # Mouth

        # Draw hearts (existing code)
        for i in range(hearts):
            pygame.draw.circle(screen, RED, (20 + i * 30, 20), 10)

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
