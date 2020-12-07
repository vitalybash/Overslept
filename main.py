import pygame

from developers_settings import *


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

    # установление начального вида кнопок по средством переменной
    buttons_condition = PATHS[2]
    # список координат кнопок
    coords = MAIN_MENU_BUTTONS_COORDINATES
    is_pressed = False  # Флаг зажатой клавиши мыши
    running = True
    while running:
        # Установка спрайта фона
        screen.blit(load_image(PATHS[1])[0], load_image(PATHS[1])[1])
        # Установка спрайта кнопок в зависимости от выбранной кнопки
        # Переменная зависимости - buttons_condition
        screen.blit(load_image(buttons_condition)[0],
                    load_image(buttons_condition)[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Обработка наведения на кнопки
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                coords = MAIN_MENU_BUTTONS_COORDINATES
                if coords[0][0] < mouse_x < coords[0][2] and \
                        coords[0][1] < mouse_y < coords[0][3]:
                    if is_pressed:
                        buttons_condition = PATHS[4]
                    else:
                        buttons_condition = PATHS[3]
                elif coords[1][0] < mouse_x < coords[1][2] and \
                        coords[1][1] < mouse_y < coords[1][3]:
                    if is_pressed:
                        buttons_condition = PATHS[6]
                    else:
                        buttons_condition = PATHS[5]
                elif coords[2][0] < mouse_x < coords[2][2] and \
                        coords[2][1] < mouse_y < coords[2][3]:
                    if is_pressed:
                        buttons_condition = PATHS[8]
                    else:
                        buttons_condition = PATHS[7]
                elif coords[3][0] < mouse_x < coords[3][2] and \
                        coords[3][1] < mouse_y < coords[3][3]:
                    if is_pressed:
                        buttons_condition = PATHS[10]
                    else:
                        buttons_condition = PATHS[9]
            # Обработка нажатия кнопки
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_pressed = True
                mouse_x, mouse_y = event.pos
                coords = MAIN_MENU_BUTTONS_COORDINATES
                if coords[0][0] < mouse_x < coords[0][2] and \
                        coords[0][1] < mouse_y < coords[0][3]:
                    buttons_condition = PATHS[4]
                elif coords[1][0] < mouse_x < coords[1][2] and \
                        coords[1][1] < mouse_y < coords[1][3]:
                    buttons_condition = PATHS[6]
                elif coords[2][0] < mouse_x < coords[2][2] and \
                        coords[2][1] < mouse_y < coords[2][3]:
                    buttons_condition = PATHS[8]
                elif coords[3][0] < mouse_x < coords[3][2] and \
                        coords[3][1] < mouse_y < coords[3][3]:
                    buttons_condition = PATHS[10]
                else:
                    buttons_condition = PATHS[2]

            # Обработка нажатия кнопки(отпуск клавиши)
            if event.type == pygame.MOUSEBUTTONUP:
                is_pressed = False
                mouse_x, mouse_y = event.pos
                coords = MAIN_MENU_BUTTONS_COORDINATES
                if coords[0][0] < mouse_x < coords[0][2] and \
                        coords[0][1] < mouse_y < coords[0][3]:
                    buttons_condition = PATHS[3]
                elif coords[1][0] < mouse_x < coords[1][2] and \
                        coords[1][1] < mouse_y < coords[1][3]:
                    buttons_condition = PATHS[5]
                elif coords[2][0] < mouse_x < coords[2][2] and \
                        coords[2][1] < mouse_y < coords[2][3]:
                    buttons_condition = PATHS[7]
                elif coords[3][0] < mouse_x < coords[3][2] and \
                        coords[3][1] < mouse_y < coords[3][3]:
                    buttons_condition = PATHS[9]
                    running = False
                else:
                    buttons_condition = PATHS[2]

        pygame.display.flip()
    pygame.quit()
