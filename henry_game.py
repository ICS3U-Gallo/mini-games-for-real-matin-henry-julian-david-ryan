import pygame
import random

pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Grinches Math Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 48)

# Math game variables
score = 0
question = ""
answer = 0
user_answer = ""
difficulty = "easy"

# Generate a math question
def generate_question(difficulty):
    global question, answer
    if difficulty == "easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-"])
    else:  # hard
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)
        operation = random.choice(["+", "-"])

    if operation == "+":
        answer = num1 + num2
        question = f"{num1} + {num2} = ?"
    else:
        answer = num1 - num2
        question = f"{num1} - {num2} = ?"

# Game loop
running = True
generate_question(difficulty)
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Check if the answer is correct
                if user_answer.isdigit() and int(user_answer) == answer:
                    score += 1
                    user_answer = ""
                    generate_question(difficulty)
                else:
                    user_answer = ""  # Clear answer if incorrect
            elif event.key == pygame.K_BACKSPACE:
                # Remove the last digit
                user_answer = user_answer[:-1]
            else:
                # Add typed number to user_answer if it’s a digit
                if event.unicode.isdigit():
                    user_answer += event.unicode

    # Draw everything
    screen.fill(WHITE) # Background color
    pygame.draw.rect(screen, RED, (25, 50, 20,1000))
    pygame.draw.rect(screen,GREEN, (85, 50, 20, 1000 ))
    pygame.draw.rect(screen,RED, (145, 0, 20, 1000 ))
    pygame.draw.rect(screen, GREEN, (195, 0, 20, 1000 ))
    pygame.draw.rect(screen,RED, (245, 0, 20, 1000 ))
    pygame.draw.rect(screen, GREEN, (0, 50, 145, 10))

    # Display question and user input
    question_text = font.render(question, True, BLACK)
    screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, HEIGHT // 3))

    # Display user answer
    user_text = font.render(user_answer, True, BLACK if user_answer else BLACK)
    screen.blit(user_text, (WIDTH // 2 - user_text.get_width() // 2, HEIGHT // 2))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update screen
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
