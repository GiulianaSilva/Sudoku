"""
    Authors: Isabella Marin, Kaitlyn Kapalka, Giuliana Silva
"""
from constants import *
from cell import Cell
from sudoku_generator import generate_sudoku
import pygame


class Board:

    SKETCH_VALUES = {
        pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3, pygame.K_4: 4, pygame.K_5: 5, pygame.K_6: 6, pygame.K_7: 7,
        pygame.K_8: 8, pygame.K_9: 9}

    def __init__(self, rows, cols, width, height, screen, difficulty):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        #call generate_sudoku to try and get 2D array
        self.board = generate_sudoku(9, 30)
        print(self.board)

        self.cells = self.cell_maker()
        self.selected_cell = None
        self.draw()

    # makes the 2D cell array of the board
    def cell_maker(self):
        cell_list = []
        for row in range(NUM_ROWS):
            col_list = []
            for col in range(NUM_COLS):
                col_list.append(Cell(self.board[row][col], row, col, self.screen))
            cell_list.append(col_list)
        return cell_list

    def draw(self):

        for row in self.cells:
            for cell in row:
                cell.draw()

        # horizontal regular lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (self.width, i * SQUARE_SIZE), LINE_WIDTH)

        # vertical regular lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, 630), LINE_WIDTH)

        # horizontal bold lines
        for i in range(3, 9, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (self.width, i * SQUARE_SIZE), 8)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 9 * SQUARE_SIZE), (self.width, 9 * SQUARE_SIZE), 8)

        # vertical bold lines
        for i in range(3, 9, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, 630), 8)

        for row in self.cells:
            for cell in row:
                if cell.selected:
                    cell.draw()

    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value
        if self.selected_cell:
            self.selected_cell.set_selected(False)

        self.selected_cell = self.cells[row][col]
        self.selected_cell.set_selected(True)
        return row, col

    def click(self, x, y):
        # if a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the
        # (row, col) of the cell which was clicked. Otherwise, this function returns None.
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            return row, col
        else:
            return None

    def clear(self):
        # clears the value cell. note that the user can only remove the cell values and sketched value that are
        # filled by themselves.
        for row in self.cells:
            for cell in row:
                cell.set_cell_value(0)

    # resets board to its original state, replacing all inputted numbers to 0
    def reset_to_original(self):
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                cell = self.cells[row][col]
                if not cell.is_original:
                    cell.set_cell_value(0)
                    cell.set_sketched_value(0)

    # checks if the board if full or not
    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def check_board(self):

        # checks if the columns satisfy a win
        for i in range(9):
            for j in range(9):
                for col in range(self.cols):
                    if col != j and self.board[i][col] == self.board[i][j]:
                        return False

                # checks if the rows satisfy a win
                for row in range(self.rows):
                    if row !=i and self.board[row][j] == self.board[i][j]:
                        return False

                box_start_row = 3 * (i//3)
                box_start_col = 3 * (j//3)

                # checks if the 3x3 box satisfies a win
                for row in range(box_start_row, box_start_row + 3):
                    for col in range(box_start_col, box_start_col + 3):
                        if row != i and col != j and self.board[row][col] == self.board[i][j]:
                            return False

        return True
