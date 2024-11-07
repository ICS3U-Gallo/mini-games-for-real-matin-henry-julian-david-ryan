import pygame
import random

pygame.init()

#parameters
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#variables
bird_x = 50
bird_y = 300
bird_velocity = 0
bird_gravity = 0.5
bird_flap_strength = -10
bird_radius = 20
bird_flap = False

pipe_width = 60
pipe_gap = 150
pipe_velocity = 4
pipe_frequency = 1500  # in milliseconds

score = 0
font = pygame.font.SysFont('Arial', 32)

#frame rate
clock = pygame.time.Clock()

pipes = []
