import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grinches Math Game")
clock = pygame.time.Clock()

BG = (189, 255, 190)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (3, 128, 40)
RED = (245, 95, 95)

font = pygame.font.SysFont("comicsansms", 50)
small_font = pygame.font.SysFont("comicsansms", 30)
score_font = pygame.font.SysFont("Arial", 35)
instructional_font = pygame.font.SysFont("Times New Roman", 35)
instructional_font2 = pygame.font.SysFont("Arial", 20)

score = 0
question = ""
answer = 0
user_answer = ""
difficulty = "easy"
game_state = "menu" 

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

# Draw the main menu
def draw_menu():
    screen.fill(BG)
    title_text = font.render("Grinches Math Game", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

    # Start Game button
    pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50))
    start_text = small_font.render("Start Game", True, WHITE)
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - 40))

    # Instructions button
    pygame.draw.rect(screen, RED, (WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50))
    instructions_text = small_font.render("Instructions", True, WHITE)
    screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2 + 30))

# Draw the instructions screen
def draw_instructions():
    screen.fill(BG)    
    pygame.draw.rect(screen, RED, (WIDTH // 2 - 50, HEIGHT - 100, 100, 50))
    back_text = small_font.render("Back", True, WHITE)
    screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 100))

# Game loop
running = True
generate_question(difficulty)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if game_state == "menu":
                # Check if Start Game button is clicked
                if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and HEIGHT // 2 - 50 <= mouse_y <= HEIGHT // 2:
                    game_state = "game"
                # Check if Instructions button is clicked
                elif WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and HEIGHT // 2 + 20 <= mouse_y <= HEIGHT // 2 + 70:
                    game_state = "instructions"

            elif game_state == "instructions":
                if WIDTH // 2 - 50 <= mouse_x <= WIDTH // 2 + 50 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    game_state = "menu"
            elif game_state == "game":
                if WIDTH // 2 - 50 <= mouse_x <= WIDTH // 2 + 50 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    game_state = "menu"

        elif event.type == pygame.KEYDOWN and game_state == "game":
            if event.key == pygame.K_RETURN:
                # Check if answer is correct
                if user_answer.isdigit() and int(user_answer) == answer:
                    score += 1
                    user_answer = ""
                    generate_question(difficulty)
                else:
                    user_answer = "" 
            elif event.key == pygame.K_BACKSPACE:
                user_answer = user_answer[:-1]  
            elif event.unicode.isdigit():
                user_answer += event.unicode  

    if game_state == "menu":
        draw_menu()
    elif game_state == "instructions":
        draw_instructions()
        instructions_text = instructional_font.render("Welcome to The Grinches Math Game!", True, RED)
        screen.blit(instructions_text, (120,50))
        line1 = instructional_font2.render("The grinch has captured you and stolen Christmas! In order to save ", True, RED)
        line2 = instructional_font2.render ("Christmas Day and be the world's hero you must complete these math questions", True, RED)
        line3 = instructional_font2.render("Each question right is equal to 1 damage to The Grinch", True, RED)
        line4 = instructional_font2.render("Each question right is equal to one live lost for you", True, RED ) 
        line5 = instructional_font2.render("The Grinch has 10 Health and you have 3 lives", True, RED)
        line6 = instructional_font.render("Goodluck on your adventure, Warrior", True, RED)

        screen.blit(line1, (30, 150))
        screen.blit(line2, (30, 180))
        screen.blit(line3, (30, 250))
        screen.blit(line4, (30, 280))
        screen.blit(line5, (30, 310))
        screen.blit(line6, (120, 370))


    elif game_state == "game":
        screen.fill(BG)
        #Top to Bottom
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

        # Right to Left:
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

        pygame.draw.rect(screen, RED, (WIDTH // 2 - 50, HEIGHT - 100, 100, 50))
        back_text = small_font.render("Back", True, WHITE)
        screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 100))

        # Display question and user input
        transparent_rect = pygame.Surface((400, 200), pygame.SRCALPHA)
        transparent_rect.fill((255, 255, 255, 220))
        pygame.draw.rect(screen, WHITE, (320, 300, 150, 75))
        screen.blit(transparent_rect, (200, 180))
        
        question_text = font.render(question, True, BLACK)
        screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, HEIGHT // 3))


        user_text = font.render(user_answer, True, BLACK if user_answer else BLACK)
        screen.blit(user_text, (WIDTH // 2 - user_text.get_width() // 2, HEIGHT // 2))

        # Display score
        score_text = score_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (0, 10))


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
