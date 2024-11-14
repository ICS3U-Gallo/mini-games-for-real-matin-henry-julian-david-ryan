import pygame
import random

pygame.init()
#display for the game
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
#colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
#speed of snake
snake_block = 10
snake_speed = 20
#font style
font_style = pygame.font.SysFont("bahnschrift", 25)
#drawing the apples(AKA presents)
def draw_present(x, y):

    pygame.draw.rect(screen, blue, [x, y, snake_block, snake_block])  
    pygame.draw.rect(screen, orange, [x + 2, y + 4, snake_block - 4, 2])  
    pygame.draw.rect(screen, orange, [x + 4, y + 2, 2, snake_block - 4]) 
#drawing out the snake, also makes the snake green when eating the block
def draw_snake(snake_list):
    for i, (x, y) in enumerate(snake_list):
        color = red if i % 2 == 0 else green  
        pygame.draw.rect(screen, color, [x, y, snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])
    def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Spawn present on game start
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    score = 0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(white)
            message("Merry Christmas! Press (P)Play Again or (Q)Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change == 0: 
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
        # wall collisions
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)

        # present
        draw_present(foodx, foody) 

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Self colision
        for x, y in snake_List[:-1]:
            if [x, y] == snake_Head:
                game_close = True

        draw_snake(snake_List)

        if x1 == foodx and y1 == foody:

            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1 
            score += 10  
