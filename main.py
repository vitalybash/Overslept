import pygame

from developers_settings import *
from interfaces.main_menu import MainMenu


def load_image(img_path):
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.scale(image, (1024, 576))
    image_rect = image.get_rect(topleft=(0, 0))
    return [image, image_rect]


class Field:
    def __init__(self, width=5, height=5, cell_size=15):
        self.width, self.height = width, height
        self.cell_size = cell_size
        self.field = [[0 for j in range(width)] for i in range(height)]

    def render(self):
        for y in range(0, self.height * self.cell_size, self.cell_size):
            for x in range(0, self.width * self.cell_size, self.cell_size):
                pygame.draw.rect(screen, pygame.Color('white'),
                                 (x, y, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos  # Распаковка координат клика
        col = x // self.cell_size
        row = y // self.cell_size

        print(row, col)
        print(len(self.field), len(self.field[0]))
        if 0 <= row < len(self.field) and 0 <= col < len(self.field[0]):
            return row, col
        return None


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('OverSlept')
    screen = pygame.display.set_mode(SIZE)
    screen.fill((0, 0, 0))

    # Экземпляр
    MAIN_WND = MainMenu()
    running = True
    while running:
        running = MAIN_WND.render(screen)
    pygame.quit()

