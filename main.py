import pygame

from developers_settings import *


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
    #  field = Field(6, 3, cell_size=150)
    #  field.render()

    #  тоже самое, что и снизу, смысл создания сетки мне непонятен
    #  но я пока оставил

    buttons_condition = PATHS[2]
    #  установление начального вида кнопок по средством переменной
    running = True
    while running:
        for event in pygame.event.get():
            main_menu_background = pygame.image.load(PATHS[1])
            main_menu_background = pygame.transform.scale(main_menu_background,
                                                          (1024, 576))
            main_menu_rect = main_menu_background.get_rect(topleft=(0, 0))
            screen.blit(main_menu_background, main_menu_rect)
            #  установка спрайта фона
            main_menu_buttons = pygame.image.load(buttons_condition)
            main_menu_buttons = pygame.transform.scale(main_menu_buttons,
                                                       (1024, 576))
            main_buttons_rect = main_menu_background.get_rect(topleft=(0, 0))
            screen.blit(main_menu_buttons, main_buttons_rect)
            #  установка спрайта кнопок
            #  в зависимости от выбранной кнопки
            #  переменная зависимости - buttons_condition

            coords = MAIN_MENU_BUTTONS_COORDINATES
            #  список координат кнопок

            if event.type == pygame.QUIT:
                running = False
            #  if event.type == pygame.MOUSEBUTTONDOWN:
            #      print(field.get_cell(event.pos))

            #  я чёт не понял зачем ты тут с полем игрался ¯\(°_o)/¯
            if event.type == pygame.MOUSEMOTION:
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
                else:
                    buttons_condition = PATHS[2]
            #  обработка наведения на кнопки
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                    running = False
            #  обработка нажатий на кнопки
        pygame.display.flip()
    pygame.quit()
