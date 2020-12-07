import pygame
from developers_settings import *
from basic_functions import load_image


class MainMenu:
    """Класс для работы с интерфейсом главного меню, и посредственно его
       настройки."""
    def __init__(self):
        self.buttons_condition = PATHS[2]
        self.coords = MAIN_MENU_BUTTONS_COORDINATES
        self.is_pressed = False
        self.running = True

    def render(self, screen):
        # Установка спрайта фона
        screen.blit(load_image(PATHS[1])[0], load_image(PATHS[1])[1])
        # Установка спрайта кнопок в зависимости от выбранной кнопки
        # Переменная зависимости - buttons_condition
        screen.blit(load_image(self.buttons_condition)[0],
                    load_image(self.buttons_condition)[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Обработка наведения на кнопки
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                coords = MAIN_MENU_BUTTONS_COORDINATES
                if coords[0][0] < mouse_x < coords[0][2] and \
                        coords[0][1] < mouse_y < coords[0][3]:
                    if self.is_pressed:
                        self.buttons_condition = PATHS[4]
                    else:
                        self.buttons_condition = PATHS[3]
                elif coords[1][0] < mouse_x < coords[1][2] and \
                        coords[1][1] < mouse_y < coords[1][3]:
                    if self.is_pressed:
                        self.buttons_condition = PATHS[6]
                    else:
                        self.buttons_condition = PATHS[5]
                elif coords[2][0] < mouse_x < coords[2][2] and \
                        coords[2][1] < mouse_y < coords[2][3]:
                    if self.is_pressed:
                        self.buttons_condition = PATHS[8]
                    else:
                        self.buttons_condition = PATHS[7]
                elif coords[3][0] < mouse_x < coords[3][2] and \
                        coords[3][1] < mouse_y < coords[3][3]:
                    if self.is_pressed:
                        self.buttons_condition = PATHS[10]
                    else:
                        self.buttons_condition = PATHS[9]
            # Обработка нажатия кнопки
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_pressed = True
                mouse_x, mouse_y = event.pos
                coords = MAIN_MENU_BUTTONS_COORDINATES
                if coords[0][0] < mouse_x < coords[0][2] and \
                        coords[0][1] < mouse_y < coords[0][3]:
                    self.buttons_condition = PATHS[4]
                elif coords[1][0] < mouse_x < coords[1][2] and \
                        coords[1][1] < mouse_y < coords[1][3]:
                    self.buttons_condition = PATHS[6]
                elif coords[2][0] < mouse_x < coords[2][2] and \
                        coords[2][1] < mouse_y < coords[2][3]:
                    self.buttons_condition = PATHS[8]
                elif coords[3][0] < mouse_x < coords[3][2] and \
                        coords[3][1] < mouse_y < coords[3][3]:
                    self.buttons_condition = PATHS[10]
                else:
                    self.buttons_condition = PATHS[2]

            # Обработка нажатия кнопки(отпуск клавиши)
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_pressed = False
                mouse_x, mouse_y = event.pos
                coords = MAIN_MENU_BUTTONS_COORDINATES
                if coords[0][0] < mouse_x < coords[0][2] and \
                        coords[0][1] < mouse_y < coords[0][3]:
                    self.buttons_condition = PATHS[3]
                elif coords[1][0] < mouse_x < coords[1][2] and \
                        coords[1][1] < mouse_y < coords[1][3]:
                    self.buttons_condition = PATHS[5]
                elif coords[2][0] < mouse_x < coords[2][2] and \
                        coords[2][1] < mouse_y < coords[2][3]:
                    self.buttons_condition = PATHS[7]
                elif coords[3][0] < mouse_x < coords[3][2] and \
                        coords[3][1] < mouse_y < coords[3][3]:
                    self.buttons_condition = PATHS[9]
                    self.running = False
                else:
                    self.buttons_condition = PATHS[2]
        pygame.display.flip()
        return self.running
