import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

snake_block = 10
snake_speed = 20


