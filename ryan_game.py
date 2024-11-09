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
#display of the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])
