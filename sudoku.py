"""
    Authors: Isabella Marin, Kaitlyn Kapalka, Giuliana Silva
"""
import pygame
import sys
from constants import *
from board import Board


def draw_game_start(screen, WIDTH, HEIGHT):
    # Background color
    screen.fill(BG_COLOR)

    # Initialize title page fonts
    sudoku_title_font = pygame.font.Font(None, 90)
    button_font = pygame.font.Font(None, 60)
    game_mode_font = pygame.font.Font(None, 85)

    # Initialize and draw title
    title_surface = sudoku_title_font.render("Welcome to Sudoku", 0, CLARET)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(title_surface, title_rectangle)

    # Initialize and provide game mode options
    game_mode_surface = game_mode_font.render("Select Game Mode:", 0, CLARET)
    game_mode_rectangle = game_mode_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25))
    screen.blit(game_mode_surface, game_mode_rectangle)

    # Initialize button text
    easy_text = button_font.render("Easy", 0, TEXT_COLOR)
    medium_text = button_font.render("Medium", 0, TEXT_COLOR)
    hard_text = button_font.render("Hard", 0, TEXT_COLOR)

    # Initialize button background color and rectangle

    # Easy mode
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(CLARET)
    easy_surface.blit(easy_text, (10, 10))
    easy_rect = easy_surface.get_rect(center=(WIDTH * (1 / 4), HEIGHT // 2 + 100))

    # Medium mode
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(CLARET)
    medium_surface.blit(medium_text, (10, 10))
    medium_rect = medium_surface.get_rect(center=(WIDTH * (2 / 4), HEIGHT // 2 + 100))

    # Hard mode
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(CLARET)
    hard_surface.blit(hard_text, (10, 10))
    hard_rect = hard_surface.get_rect(center=(WIDTH * (3 / 4), HEIGHT // 2 + 100))

    # Draw the 3 mode buttons
    screen.blit(easy_surface, easy_rect)
    screen.blit(medium_surface, medium_rect)
    screen.blit(hard_surface, hard_rect)

    # choosing the game mode loop
    mode = True
    while mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # verify if user clicks easy mode
                global empty_cells
                if easy_rect.collidepoint(event.pos):
                    empty_cells = 30
                    return empty_cells

                # verify if user clicks medium mode
                elif medium_rect.collidepoint(event.pos):
                    empty_cells = 40
                    return empty_cells

                # verify if user clicks hard mode
                elif hard_rect.collidepoint(event.pos):
                    empty_cells = 50
                    return empty_cells

        pygame.display.update()


def draw_buttons(screen):
    button_font = pygame.font.Font(None, 70)

    # Initialize button text
    reset_text = button_font.render("Reset", 0, TEXT_COLOR)
    restart_text = button_font.render("Restart", 0, TEXT_COLOR)
    exit_text = button_font.render("Exit", 0, TEXT_COLOR)

    # Draw reset button
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(CLARET)
    reset_surface.blit(reset_text, (10, 10))
    reset_rect = reset_surface.get_rect(center=(WIDTH * (1 / 4) - 20, HEIGHT // 2 + 315))

    # Draw restart button
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(CLARET)
    restart_surface.blit(restart_text, (10, 10))
    restart_rect = restart_surface.get_rect(center=(WIDTH * (2 / 4), HEIGHT // 2 + 315))

    # Draw exit button
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(CLARET)
    exit_surface.blit(exit_text, (10, 10))
    exit_rect = exit_surface.get_rect(center=(WIDTH * (3 / 4), HEIGHT // 2 + 315))

    # Draw the 3 buttons
    screen.blit(reset_surface, reset_rect)
    screen.blit(restart_surface, restart_rect)
    screen.blit(exit_surface, exit_rect)

    return reset_surface, reset_rect, restart_surface, restart_rect, exit_surface, exit_rect


def draw_game_over(screen, won):
    # Background color
    screen.fill(BG_COLOR)

    # Initialize game won and over font
    endgame_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # game won condition
    if won == True:
        # initialize and draw game won text
        endgame_surface = endgame_font.render("Game Won!", 0, CLARET)
        endgame_rectangle = endgame_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(endgame_surface, endgame_rectangle)

        # Initialize exit button text
        exit_text = button_font.render("EXIT", 0, TEXT_COLOR)

        # Initialize exit button background color and rectangle
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(CLARET)
        exit_surface.blit(exit_text, (10, 10))
        exit_rect = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        # Draw the exit button
        screen.blit(exit_surface, exit_rect)

        # exit game loop
        exit_game = True
        while exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # verify if user clicks restart mode
                    if exit_rect.collidepoint(event.pos):
                        exit_game = False
                        return True  # exits game

            pygame.display.update()

    # game over condition
    elif won == False:
        # initialize and draw game over text
        endgame_surface = endgame_font.render("Game Over :(", 0, CLARET)
        endgame_rectangle = endgame_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(endgame_surface, endgame_rectangle)

        # Initialize restart button text
        restart_text = button_font.render("RESTART", 0, TEXT_COLOR)

        # Initialize restart button background color and rectangle
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(CLARET)
        restart_surface.blit(restart_text, (10, 10))
        restart_rect = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        # Draw the restart button
        screen.blit(restart_surface, restart_rect)

        # restart game loop
        restart = True
        while restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # verify if user clicks restart mode
                    if restart_rect.collidepoint(event.pos):
                        restart = False
                        return True  # restarts game

            pygame.display.update()


# method to handle key presses
def key_press(event, board):
    selected_cell = board.selected_cell

    # Handle arrow key presses unconditionally
    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
        arrow_key_press(event, board)
        return True

    #saves the number inserted by the user in insertNum

    if selected_cell.value == 0 or selected_cell.sketched:
        if event.key in board.SKETCH_VALUES:
            selected_cell.sketched = True
            selected_cell.set_sketched_value(board.SKETCH_VALUES[event.key])
            sketch_val = board.SKETCH_VALUES[event.key]
            global insertNum
            insertNum = sketch_val

        #allows inserted number to be erased
        elif event.key == pygame.K_BACKSPACE:
            selected_cell.set_sketched_value(0)

        #when user clickes enter the inputed number is shown in the pygame window
        elif event.key == pygame.K_RETURN:
            print(sudoku_board.board)
            index = (selected_cell.row, selected_cell.col)
            x = index[-2]
            y = index[-1]
            x = int(x)
            y = int(y)
            new_value = insertNum
            sudoku_board.board[x][y] = new_value
            print(sudoku_board.board)

            for row in sudoku_board.board:
                print(row)

            selected_cell.sketched = False
            selected_cell.selected = False

            #checks for win if board is full
            if board.is_full():
                win = board.check_board()
                draw_game_over(screen, win)
                return False

        arrow_key_press(event, board)

    return True


# method to handle mouse clicks
def mouse_click(event, board, reset_rect, restart_rect, exit_rect):
    # verify if reset button was clicked
    if reset_rect.collidepoint(event.pos):
        board.reset_to_original()
        board.draw()
        screen.blit(reset_surf, reset_rect)
        screen.blit(restart_surf, restart_rect)
        screen.blit(exit_surf, exit_rect)

    elif restart_rect.collidepoint(event.pos):
        # stops game if restart is clicked
        return False
    elif exit_rect.collidepoint(event.pos):
        # exits game
        sys.exit()
    else:
        # coordinates of mouse click
        x_coordinate, y_coordinate = event.pos
        # verify that the mouse click is within the board
        if x_coordinate < WIDTH and y_coordinate < HEIGHT:
            board.click(x_coordinate, y_coordinate)
            clicked_row, clicked_col = sudoku_board.click(x_coordinate, y_coordinate)
            if clicked_row is not None and clicked_col is not None:
                selected_coordinates = board.select(clicked_row, clicked_col)
                print(selected_coordinates)
                print(board.board[clicked_row][clicked_col])
                global positionMouse
                positionMouse = selected_coordinates

    # continues loop of game
    return True


# method to handle arrow key presses
def arrow_key_press(event, board):
    selected_cell = board.selected_cell

    # get row and column of the selected cell
    if selected_cell is not None:
        row, col = selected_cell.row, selected_cell.col

    # row and col updated according to arrow key pressed
    if event.key == pygame.K_UP:
        row = (row - 1) % 9
    elif event.key == pygame.K_DOWN:
        row = (row + 1) % 9
    elif event.key == pygame.K_LEFT:
        col = (col - 1) % 9
    elif event.key == pygame.K_RIGHT:
        col = (col + 1) % 9

    board.select(row, col)
    board.draw()


# method for game running loop
def game_run(screen, board, reset_rect, restart_rect, exit_rect):
    num_font = pygame.font.Font(None, 60)
    screen.fill(BG_COLOR)
    board.draw()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                run = mouse_click(event, board, reset_rect, restart_rect, exit_rect)

            elif event.type == pygame.KEYDOWN:
                run = key_press(event, board)

        # redraw buttons and update display in loop
        board.draw()
        screen.blit(reset_surf, reset_rect)
        screen.blit(restart_surf, restart_rect)
        screen.blit(exit_surf, exit_rect)
        pygame.display.update()

    pygame.display.update()


if __name__ == "__main__":
    # initialize pygame
    pygame.init()

    # dimensions of screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # make screen caption
    pygame.display.set_caption('Sudoku')

    # game loop run variable
    run = True

    # game loop
    while run:

        # for loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                run = False
        # Fill the background color to the screen
        screen.fill(BG_COLOR)

        difficulty = draw_game_start(screen, WIDTH, HEIGHT)

        # create sudoku board based on difficulty chosen
        sudoku_board = Board(NUM_ROWS, NUM_COLS, WIDTH, HEIGHT, screen, difficulty)

        # draw first sudoku board
        sudoku_board.draw()

        # draw the 3 buttons at bottom of main board
        reset_surf, reset_rect, restart_surf, restart_rect, exit_surf, exit_rect = draw_buttons(screen)

        # update changes to display
        pygame.display.flip()

        # run game loop
        game_run(screen, sudoku_board, reset_rect, restart_rect, exit_rect)

    pygame.display.update()

