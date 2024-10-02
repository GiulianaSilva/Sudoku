"""
    Authors: Isabella Marin, Kaitlyn Kapalka, Giuliana Silva
"""
from constants import*
import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.is_original = value != 0
        self.screen = screen
        self.selected = False
        self.sketched = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def set_selected(self, state):
        self.selected = state

    def draw(self):
        #for r_index, row in enumerate(self.cells):
            #for c_index, cell in enumerate(row):
        cell_rect = pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(self.screen, BG_COLOR, cell_rect)


        # verify that self.value is not 0
        if self.value != 0:

            value_color = LIGHT_GRAY if self.sketched else BLACK
            value_font = pygame.font.Font(None, 80)
            value_surf = value_font.render(str(self.value), 0, value_color)
            value_rect = value_surf.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2,
                                                     SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            self.screen.blit(value_surf, value_rect)


        # draws red outline around selected box
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), cell_rect, 3)