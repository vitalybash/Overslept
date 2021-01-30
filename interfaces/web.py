import pygame
from developers_settings import *


class Web:
    def __init__(self):
        self.turn = 0
        self.board = [[0] * 9 for _ in range(3)]
        self.top_right_coords = FIELD_BEGIN_COORDS
        self.height_cell = CELL_HEIGHT
        self.width_cell = CELL_WIDTH
        self.size = [9, 3]

    def run(self, screen, turn):
        #  if turn % 2 == 0:
        #    return
        #  else:
        self.render_web(screen)

    def render_web(self, screen):
        color = pygame.Color('white')
        for row in range(3):
            for col in range(9):
                pygame.draw.rect(screen, color, (
                    self.top_right_coords[0] + self.width_cell * col,
                    self.top_right_coords[1] + self.height_cell * row,
                    self.width_cell,
                    self.height_cell),
                                 4)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        # Если пользователь щелкнул мимо сетки по горизонтали
        cell_x = (x - self.top_right_coords[0]) // self.width_cell
        cell_y = (y - self.top_right_coords[1]) // self.height_cell
        if cell_x < 0 or cell_x >= 9 or \
                cell_y < 0 or cell_y >= 3:
            return None
        return [cell_x, cell_y]
