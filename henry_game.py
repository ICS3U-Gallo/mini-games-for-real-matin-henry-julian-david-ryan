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
score_font = pygame.font.SysFont("Arial", 30)
instructional_font = pygame.font.SysFont("Times New Roman", 35)
instructional_font2 = pygame.font.SysFont("Arial", 20)

score = 10
lives = 3
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
    else:  # hard
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)

    operation = random.choice(["+", "-"])

    if operation == "+":
        answer = num1 + num2
        question = f"{num1} + {num2} = ?"
    else:
        if num1 < num2:
            num1, num2 = num2, num1
        answer = num1 - num2
        question = f"{num1} - {num2} = ?"

# main menu
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
    #grinch 1
    #head
    pygame.draw.ellipse(screen, GREEN, (80, 250, 120, 160))

    #hat
    pygame.draw.polygon(screen, RED, [(90, 270), (190, 270), (140, 190)])
    pygame.draw.circle(screen, WHITE, (140, 190), 10) 
    pygame.draw.rect(screen, WHITE, (80, 270, 120, 15))

    #eyes
    pygame.draw.circle(screen, WHITE, (115, 310), 12)
    pygame.draw.circle(screen, WHITE, (165, 310), 12)
    pygame.draw.circle(screen, BLACK, (115, 310), 6)
    pygame.draw.circle(screen, BLACK, (165, 310), 6)

    #nose
    pygame.draw.circle(screen, BLACK, (140, 340), 5)
    #smile
    pygame.draw.arc(screen, RED, (115, 355, 50, 20), 3.6, 6.3, 3)

    #eyebrows
    pygame.draw.line(screen, BLACK, (105, 285), (125, 295), 3)
    pygame.draw.line(screen, BLACK, (175, 285), (155, 295), 3)

    #body
    pygame.draw.rect(screen, GREEN, (120, 420, 40, 100))
    pygame.draw.circle(screen, RED, (140, 440), 5)
    pygame.draw.circle(screen, RED, (140, 460), 5)
    pygame.draw.circle(screen, RED, (140, 480), 5)

    #arms
    pygame.draw.line(screen, GREEN, (120, 430), (90, 480), 8)
    pygame.draw.line(screen, GREEN, (160, 430), (190, 480), 8)

    #grinch 2
    #head
    pygame.draw.ellipse(screen, GREEN, (610, 250, 120, 160))

    #hat
    pygame.draw.polygon(screen, RED, [(620, 270), (720, 270), (670, 190)])
    pygame.draw.circle(screen, WHITE, (670, 190), 10)
    pygame.draw.rect(screen, WHITE, (610, 270, 120, 15))

    #eyes
    pygame.draw.circle(screen, WHITE, (645, 310), 12)
    pygame.draw.circle(screen, WHITE, (695, 310), 12)
    pygame.draw.circle(screen, BLACK, (645, 310), 6)
    pygame.draw.circle(screen, BLACK, (695, 310), 6)
    pygame.draw.circle(screen, BLACK, (670, 340), 5)
    pygame.draw.arc(screen, RED, (645, 355, 50, 20), 3.6, 6.3, 3)

    #eyebrows
    pygame.draw.line(screen, BLACK, (635, 285), (655, 295), 3)
    pygame.draw.line(screen, BLACK, (705, 285), (685, 295), 3)

    #body
    pygame.draw.rect(screen, GREEN, (650, 420, 40, 100))
    pygame.draw.circle(screen, RED, (670, 440), 5)
    pygame.draw.circle(screen, RED, (670, 460), 5)
    pygame.draw.circle(screen, RED, (670, 480), 5)

    #arms
    pygame.draw.line(screen, GREEN, (650, 430), (620, 480), 8)
    pygame.draw.line(screen, GREEN, (690, 430), (720, 480), 8)
# Draw the instructions screen
def draw_instructions():
    screen.fill(BG)    
    pygame.draw.rect(screen, RED, (WIDTH // 2 - 50, HEIGHT - 100, 100, 50))
    back_text = small_font.render("Back", True, WHITE)
    screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 100))
def draw_lose_screen():
    screen.fill(BG)
    lose_text = font.render("You Lost!", True, RED)
    screen.blit(lose_text, (WIDTH // 2 - lose_text.get_width() // 2, HEIGHT // 3))
    grinch_won = instructional_font2.render("The Grinch Stole Everyone's presents", True, RED)
    screen.blit(grinch_won,(200,280))
    grinch_won2 = instructional_font2.render("Everybodies Christmas is ruined", True, RED)
    screen.blit(grinch_won2,(200,300))
    grinch_won2 = instructional_font2.render("You have failed all of us...", True, RED)
    screen.blit(grinch_won2,(200,320))
    restart_text = small_font.render("Press R to Restart", True, BLACK)
    screen.blit(restart_text, (200,380))
    
    pygame.display.flip()

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
                if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and HEIGHT // 2 - 50 <= mouse_y <= HEIGHT // 2:
                    game_state = "game"
                elif WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and HEIGHT // 2 + 20 <= mouse_y <= HEIGHT // 2 + 70:
                    game_state = "instructions"

            elif game_state == "instructions":
                if WIDTH // 2 - 50 <= mouse_x <= WIDTH // 2 + 50 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    game_state = "menu"
            elif game_state == "game":
                if WIDTH // 2 - 50 <= mouse_x <= WIDTH // 2 + 50 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    game_state = "menu"

        elif event.type == pygame.KEYDOWN:
            if game_state == "lose" and event.key == pygame.K_r:
                game_state = "menu"
                score = 10
                lives = 3
                difficulty = "easy"
                user_answer = ""
                generate_question(difficulty)
            elif game_state == "game":
                if event.key == pygame.K_RETURN:
                    if user_answer.isdigit() and int(user_answer) == answer:
                        score -= 1
                        user_answer = ""
                        if score <= 5:
                            difficulty = "hard"
                        generate_question(difficulty)
                        if difficulty == "hard":
                            hard_text = instructional_font2.render("HARD MODE!!!", True, BLACK)
                            screen.blit(hard_text, (300, 50))
                    else:
                        lives -= 1
                        user_answer = ""
                        if lives <= 0:
                            game_state = "lose"
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                elif event.unicode.isdigit():
                    user_answer += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]  
                elif event.unicode.isdigit():
                    user_answer += event.unicode  

    if game_state == "menu":
        draw_menu()
    elif game_state == "instructions":

        draw_instructions()

        transparent_rect = pygame.Surface((750, 650), pygame.SRCALPHA)
        transparent_rect.fill((255, 255, 255, 100))
        screen.blit(transparent_rect, (20, 20))
    
        instructions_text = instructional_font.render("Welcome to The Grinches Math Game!", True, RED)
        screen.blit(instructions_text, (120,50))

        line1 = instructional_font2.render("The grinch has captured you and stolen Christmas! In order to save ", True, RED)
        line2 = instructional_font2.render ("Christmas Day and be the world's hero you must complete these math questions", True, RED)
        line3 = instructional_font2.render("Each question right is equal to 1 damage to The Grinch", True, RED)
        line4 = instructional_font2.render("Each question wrong is equal to one live lost for you", True, RED ) 
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
        pygame.draw.rect(screen, GREEN, (145, 50, 20, 800))
        pygame.draw.rect(screen, RED, (195, 50, 20, 800))
        pygame.draw.rect(screen, GREEN, (245, 50, 20, 800))
        pygame.draw.rect(screen, RED, (295, 50, 20, 800))
        pygame.draw.rect(screen, GREEN, (345, 50, 20, 800))
        pygame.draw.rect(screen, RED, (395, 50, 20, 800))
        pygame.draw.rect(screen, GREEN, (445, 0, 20, 800))
        pygame.draw.rect(screen, RED, (495, 0, 20, 800))
        pygame.draw.rect(screen, GREEN, (545, 0, 20, 800))
        pygame.draw.rect(screen, RED, (595, 0, 20, 800))
        pygame.draw.rect(screen, GREEN, (645, 0, 20, 800))
        pygame.draw.rect(screen, RED, (695, 0, 20, 800))
        pygame.draw.rect(screen, GREEN, (745, 0, 20, 800))
        pygame.draw.rect(screen, RED, (795, 0, 20, 800))

        # Left to Right
        pygame.draw.rect(screen, GREEN, (0, 50, 445, 10))
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

        # Display grinch health
        score_text = score_font.render(f"Grinch Health: {score}", True, BLACK)
        screen.blit(score_text, (0, 10))
        
        #lives
        lives_text = score_font.render(f"Lives: {lives}", True, BLACK)
        screen.blit(lives_text,(300,10))



        if difficulty == "hard":
            hard_text = font.render("HARD MODE!!!", True, BLACK)
            pygame.draw.rect(screen, RED, (200, 60, 400, 80))
            screen.blit(hard_text, (240, 60))

    elif game_state == "lose":
        draw_lose_screen()


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
