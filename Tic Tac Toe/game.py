import pygame
from sys import exit
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
WHITE_RGB = (255, 255, 255)
BLACK_RGB = (0, 0, 0)
RED_RGB = (255, 0, 0)
BLUE_RGB = (0, 0, 255)
GREY_RGB = (170, 170, 170)
SQUARE_SIDE = 200
font = pygame.font.Font('Pixeltype.ttf', 50)

title_text = font.render("Tic Tac Toe", True, BLACK_RGB)
title_text_rect = title_text.get_rect(center=(300, 22))


Xwon_message = font.render("Player 1 - X Won", True, RED_RGB)
Xwon_message_rect = Xwon_message.get_rect(center=(200, 670))

Owon_message = font.render("Player 2 - O Won", True, BLUE_RGB)
Owon_message_rect = Owon_message.get_rect(center=(200, 670))

Tie_message = font.render("It's a TIE", True, BLACK_RGB)
Tie_message_rect = Tie_message.get_rect(center=(200, 670))

font2 = pygame.font.Font('SunnyspellsRegular.otf', 35)
play_again_text = font2.render('Play Again', True, BLACK_RGB)
text_rect = play_again_text.get_rect(center=(450, 670))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE_RGB)

def check_x_o(board_pos_value):
    if board_pos_value== 'X' or board_pos_value == 'O':
        return True
    return False

def check_winner(logic_board, no_of_sq_filled):

    # checking rows
    for i in range(0, 9, 3):
        if logic_board[i] == logic_board[i+1] == logic_board[i+2]:
            if check_x_o(logic_board[i]):
                draw_win_line(play_board[i], play_board[i+2])
                return logic_board[i]
            
    # checking columns
    for i in range(3):
        if logic_board[i] == logic_board[i + 3] == logic_board[i + 6]:
            if check_x_o(logic_board[i]):
                draw_win_line(play_board[i], play_board[i+6])
                return logic_board[i]

    # checkings diagonals
    if logic_board[0] == logic_board[4] == logic_board[8]:
        if check_x_o(logic_board[0]):
            draw_win_line(play_board[0], play_board[8])
            return logic_board[4]

    if logic_board[2] == logic_board[4] == logic_board[6]:
        if check_x_o(logic_board[2]):
            draw_win_line(play_board[2], play_board[6])
            return logic_board[4]

    if no_of_sq_filled == 9:
        return 'Tie'

    return None

def draw_x(square):
    top_left = square.topleft
    bottom_right = square.bottomright
    bottom_left = square.bottomleft
    top_right = square.topright

    line1_start_pos = (top_left[0] + 40, top_left[1] + 40)
    line1_end_post = (bottom_right[0] - 40, bottom_right[1] - 40)
    pygame.draw.line(screen, RED_RGB, line1_start_pos, line1_end_post, 50)

    line2_start_pos = (bottom_left[0] + 40, bottom_left[1] - 40)
    line2_end_pos = (top_right[0] - 40, top_right[1] + 40)
    pygame.draw.line(screen, RED_RGB, line2_start_pos, line2_end_pos, 50)


def draw_o(square):
    top_left = square.topleft
    bottom_right = square.bottomright

    midx = (top_left[0] + bottom_right[0]) / 2
    midy = (top_left[1] + bottom_right[1]) / 2
    pygame.draw.circle(screen, BLUE_RGB, (midx, midy), 80, 40)

def draw_win_line(start_sq, end_sq):
    start_pos = start_sq.center
    end_pos = end_sq.center
    pygame.draw.line(screen, BLACK_RGB, start_pos, end_pos, 20)


def board():
    play_board_squares = []
    counter = 0
    counter2 = 0.2
    for _ in range(9):
        sq = pygame.draw.rect(screen, BLACK_RGB, (SQUARE_SIDE * counter, SQUARE_SIDE*counter2, SQUARE_SIDE, SQUARE_SIDE), 1)
        play_board_squares.append(sq)

        counter += 1
        if counter > 2:
            counter = 0
            counter2 += 1

    return play_board_squares
    # pygame.draw.rect(screen, BLACK_RGB, (0, 40, 200, 200), 1)  # sq1
    # pygame.draw.rect(screen, BLACK_RGB, (200, 40, 200, 200), 1)  # sq2
    # pygame.draw.rect(screen, BLACK_RGB, (400, 40, 200, 200), 1)  # sq3
    # pygame.draw.rect(screen, BLACK_RGB, (0, 240, 200, 200), 1)  # sq4
    # pygame.draw.rect(screen, BLACK_RGB, (200, 240, 200, 200), 1)  # sq5
    # pygame.draw.rect(screen, BLACK_RGB, (400, 240, 200, 200), 1)  # sq6
    # pygame.draw.rect(screen, BLACK_RGB, (0, 440, 200, 200), 1)  # sq7
    # pygame.draw.rect(screen, BLACK_RGB, (200, 440, 200, 200), 1)  # sq8
    # pygame.draw.rect(screen, BLACK_RGB, (400, 440, 200, 200), 1)  # sq9



def show_result(game_winner):
    if game_winner == 'X':
        screen.blit(Xwon_message, Xwon_message_rect)
    elif game_winner == 'O':
        screen.blit(Owon_message, Owon_message_rect)
    else:
        screen.blit(Tie_message, Tie_message_rect)
    
    play_again_bt_backround = text_rect.scale_by(1.2)
    bt_rect = pygame.draw.rect(screen, GREY_RGB, play_again_bt_backround)
    screen.blit(play_again_text, text_rect)

    return bt_rect



play_board = board()
logical_board = [''] * 9
is_player_1 = True
no_of_sq_filled = 0
is_result = False
result = None

while True:
    screen.blit(title_text, title_text_rect)

    if is_result:
        play_again_bt = show_result(result)
        if pygame.mouse.get_pressed()[0] and play_again_bt.collidepoint(pygame.mouse.get_pos()):
            print('Play again')
            screen.fill(WHITE_RGB)
            play_board = board()
            is_result = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not is_result:
            for sq_num, square in enumerate(play_board):
                if square.collidepoint(event.pos):
                    if is_player_1:
                        if logical_board[sq_num] == '':
                            draw_x(square)
                            logical_board[sq_num] = 'X'
                            no_of_sq_filled += 1
                            is_player_1 = False

                    else:
                        if logical_board[sq_num] == '':
                            draw_o(square)
                            logical_board[sq_num] = 'O'
                            no_of_sq_filled += 1
                            is_player_1 = True
            result = check_winner(logical_board, no_of_sq_filled)

            if result is not None:
                logical_board = ['']*9
                is_player_1 = True
                no_of_sq_filled = 0
                is_result = True


    pygame.display.update()































