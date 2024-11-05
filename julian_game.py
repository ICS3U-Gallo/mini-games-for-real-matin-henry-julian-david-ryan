#Run Away game to escape the grinch before he catches up to player. Collect presents and pick up snowballs to throw at the grinch to slow him down. Must collect at least 10 presents to give to Santa. 
# pygame template

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

#colours

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

# Tree and House positions
house_positions = [(WIDTH - 50, HEIGHT - 30) ]
tree_positions = [(WIDTH - 80, HEIGHT - 60) ]
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    for (x, y) in tree_positions:
        pygame.draw.rect(screen, BROWN, (x, y, 20, 100))  # Tree trunk
        pygame.draw.circle(screen, DARK_GREEN, (x + 10, y - 20), 30)  # Tree leaf

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
