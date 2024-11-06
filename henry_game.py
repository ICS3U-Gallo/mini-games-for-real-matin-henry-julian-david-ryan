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
BG = (189, 255, 190)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (3, 128, 40)
RED = (245, 95, 95)

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
    screen.fill(BG) # Background color
    pygame.draw.rect(screen, GREEN, (25, 50, 20, 800))
    pygame.draw.rect(screen, RED, (85, 50, 20, 800))
    pygame.draw.rect(screen, GREEN, (145, 0, 20, 800))
    pygame.draw.rect(screen, RED, (195, 0, 20, 800))
    pygame.draw.rect(screen, GREEN, (245, 0, 20, 800))
    pygame.draw.rect(screen, RED, (295, 0, 20, 800))
    pygame.draw.rect(screen, GREEN, (345, 0, 20, 800))
    pygame.draw.rect(screen, RED, (395, 0, 20, 800))
    pygame.draw.rect(screen, GREEN, (445, 0, 20, 800))
    pygame.draw.rect(screen, RED, (495, 0, 20, 800))
    pygame.draw.rect(screen, GREEN, (545, 0, 20, 800))
    pygame.draw.rect(screen, RED, (595, 0, 20, 800))
    pygame.draw.rect(screen, GREEN, (645, 0, 20, 800))
    pygame.draw.rect(screen, RED, (695, 0, 20, 800))
    pygame.draw.rect(screen, GREEN, (745, 0, 20, 800))
    pygame.draw.rect(screen, RED, (795, 0, 20, 800))

    # Left to Right
    pygame.draw.rect(screen, GREEN, (0, 50, 145, 10))
    pygame.draw.rect(screen, RED, (0, 110, 195, 10))
    pygame.draw.rect(screen, GREEN, (0, 170, 245, 10))
    pygame.draw.rect(screen, RED, (0, 230, 295, 10))
    pygame.draw.rect(screen, GREEN, (0, 290, 345, 10))
    pygame.draw.rect(screen, RED, (0, 350, 395, 10))
    pygame.draw.rect(screen, GREEN, (0, 410, 445, 10))
    pygame.draw.rect(screen, RED, (0, 470, 495, 10))
    pygame.draw.rect(screen, GREEN, (0, 530, 545, 10))
    pygame.draw.rect(screen, RED, (0, 590, 595, 10))
    pygame.draw.rect(screen, GREEN, (0, 650, 645, 10))

    #Right to left:
    pygame.draw.rect(screen, RED, (655, 50, 145, 10))
    pygame.draw.rect(screen, GREEN, (605, 110, 195, 10))
    pygame.draw.rect(screen, RED, (555, 170, 245, 10))
    pygame.draw.rect(screen, GREEN, (505, 230, 295, 10))
    pygame.draw.rect(screen, RED, (455, 290, 345, 10))
    pygame.draw.rect(screen, GREEN, (405, 350, 395, 10))
    pygame.draw.rect(screen, RED, (355, 410, 445, 10))
    pygame.draw.rect(screen, GREEN, (305, 470, 495, 10))
    pygame.draw.rect(screen, RED, (255, 530, 545, 10))
    pygame.draw.rect(screen, GREEN, (205, 590, 595, 10))


    # Display question and user input
    transparent_rect = pygame.Surface((400, 200), pygame.SRCALPHA)
    transparent_rect.fill((255, 255, 255, 220))
    pygame.draw.rect(screen, WHITE, (320, 290, 150, 50))


    screen.blit(transparent_rect, (200, 180))  # Position for the transparent box
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
