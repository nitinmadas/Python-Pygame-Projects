import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock Paper Scissor Game")

background_image = pygame.image.load('graphics/blue.png').convert()
font = pygame.font.Font('font/SunnyspellsRegular.otf', 33)
play_message = font.render("Welcome to Rock Paper Scissor Game", True, (255, 235, 193))
play_message2 = font.render("Pick you Weapon to start playing", True, (255, 235, 193))

tie_message = font.render("It's a Tie", True, (255, 235, 193))
won_message = font.render("You Won", True, (124, 252, 0))
lost_message = font.render("You Lost", True, (255, 0, 0))

score_font = pygame.font.Font('font/SunnyspellsRegular.otf', 25)
user_score_message = score_font.render("Your Score 0", True, (255, 235, 193))
comp_score_message = score_font.render("Comp Score 0", True, (255, 235, 193))

button_rock = pygame.image.load('graphics/button_rock.png')
button_paper = pygame.image.load('graphics/button_paper.png')
button_scissor = pygame.image.load('graphics/button_scissor.png')

rock_rect = button_rock.get_rect(topleft=(25, 330))
paper_rect = button_rock.get_rect(topleft=(225, 330))
scissor_rect = button_rock.get_rect(topleft=(425, 330))

rock = pygame.image.load('graphics/rock.png')
paper = pygame.image.load('graphics/paper.png')
scissor = pygame.image.load('graphics/scissor.png')
weapon_choices = [rock, paper, scissor]
weapon_choice_text = ['R', 'P', 'S']

is_start = False
user_weapon = None
comp_weapon = None
is_user_weapon = False
is_show_weapon = False
user_score = 0
comp_score = 0
user_weapon_text = None
comp_weapon_text = None
result_message = None

def pick_weapon(user_weapon_index):
    global is_start, user_weapon, comp_weapon, is_user_weapon, is_show_weapon, user_weapon_text, comp_weapon_text
    is_start = True
    user_weapon = weapon_choices[user_weapon_index]
    user_weapon_text = weapon_choice_text[user_weapon_index]
    is_user_weapon = True
    is_show_weapon = False
    comp_weapon_index = random.randint(0, 2)
    comp_weapon = weapon_choices[comp_weapon_index]
    comp_weapon_text = weapon_choice_text[comp_weapon_index]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if rock_rect.collidepoint(event.pos):
                pick_weapon(0)
                print("rock")

            elif paper_rect.collidepoint(event.pos):
                pick_weapon(1)
                print('paper')

            elif scissor_rect.collidepoint(event.pos):
                pick_weapon(2)
                print("scissor")

    screen.blit(background_image, (0, 0))
    screen.blit(user_score_message, (50, 20))
    screen.blit(comp_score_message, (420, 20))

    if is_start is False:
        screen.blit(play_message, (100, 170))
        screen.blit(play_message2, (120, 200))

    if is_show_weapon:
        screen.blit(user_weapon, (60, 70))
        screen.blit(comp_weapon, (350, 70))
        screen.blit(result_message, (250, 20))
        is_user_weapon = False

    if is_user_weapon:
        is_show_weapon = True
        if comp_weapon_text == user_weapon_text:
            result_message = tie_message

        elif user_weapon_text == "R" and comp_weapon_text == "S":
            result_message = won_message
            user_score += 1

        elif user_weapon_text == "R" and comp_weapon_text == "P":
            result_message = lost_message
            comp_score += 1

        elif user_weapon_text == "S" and comp_weapon_text == "R":
            result_message = lost_message
            comp_score += 1

        elif user_weapon_text == "S" and comp_weapon_text == "P":
            result_message = won_message
            user_score += 1

        elif user_weapon_text == "P" and comp_weapon_text == "R":
            result_message = won_message
            user_score += 1

        elif user_weapon_text == "P" and comp_weapon_text == "S":
            result_message = lost_message
            comp_score += 1

        user_score_message = score_font.render("Your Score " + str(user_score), True, (255, 235, 193))
        comp_score_message = score_font.render("Comp Score " + str(comp_score), True, (255, 235, 193))

    screen.blit(button_rock, rock_rect)
    screen.blit(button_paper, paper_rect)
    screen.blit(button_scissor, scissor_rect)

    pygame.display.update()
    clock.tick(10)
