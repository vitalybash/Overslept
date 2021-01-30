import pygame
from developers_settings import *
from basic_functions import load_image
from interfaces.level_hub import LevelHub
from interfaces.save_hub import SaveHub
from interfaces.settings import Settings
from music.music import Music


class MainMenu:
    """Класс для работы с интерфейсом главного меню, и посредственно его
       настройки."""

    def __init__(self):
        self.buttons_condition = PATHS[3]  # Состояние кнопок по умолчанию
        self.coords = MAIN_MENU_BUTTONS_COORDINATES  # Распаковка координат
        # кнопок
        self.is_pressed = False  # Флаг зажатой клавиши мыши

    def run(self, screen):
        """Игровой цикл"""
        running = True
        # Установка музыки главного меню
        music_menu = Music('main_menu_melody.ogg')
        music_menu.run()

        while running:
            # Установка спрайта фона
            screen.blit(load_image(PATHS[2])[0], load_image(PATHS[2])[1])
            # Установка спрайта кнопок в зависимости от выбранной кнопки
            # Переменная зависимости - buttons_condition
            screen.blit(load_image(self.buttons_condition)[0],
                        load_image(self.buttons_condition)[1])
            """Кнопки: Button-0 = Играть, Button-1 = Сохранения,
               Button-2 = Настройки, Button-3 = Выход. 
            """
            button = None  # Кнопка которую нажали(если нажали)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Обработка наведения на кнопки
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    coords = MAIN_MENU_BUTTONS_COORDINATES
                    if coords[0][0] < mouse_x < coords[0][2] and \
                            coords[0][1] < mouse_y < coords[0][3]:
                        if self.is_pressed:
                            self.buttons_condition = PATHS[5]
                        else:
                            self.buttons_condition = PATHS[4]
                    elif coords[1][0] < mouse_x < coords[1][2] and \
                            coords[1][1] < mouse_y < coords[1][3]:
                        if self.is_pressed:
                            self.buttons_condition = PATHS[7]
                        else:
                            self.buttons_condition = PATHS[6]
                    elif coords[2][0] < mouse_x < coords[2][2] and \
                            coords[2][1] < mouse_y < coords[2][3]:
                        if self.is_pressed:
                            self.buttons_condition = PATHS[9]
                        else:
                            self.buttons_condition = PATHS[8]
                    elif coords[3][0] < mouse_x < coords[3][2] and \
                            coords[3][1] < mouse_y < coords[3][3]:
                        if self.is_pressed:
                            self.buttons_condition = PATHS[11]
                        else:
                            self.buttons_condition = PATHS[10]
                    else:
                        self.buttons_condition = PATHS[3]
                # Обработка нажатия кнопки
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.is_pressed = True
                    mouse_x, mouse_y = event.pos
                    coords = MAIN_MENU_BUTTONS_COORDINATES
                    if coords[0][0] < mouse_x < coords[0][2] and \
                            coords[0][1] < mouse_y < coords[0][3]:
                        self.buttons_condition = PATHS[5]
                    elif coords[1][0] < mouse_x < coords[1][2] and \
                            coords[1][1] < mouse_y < coords[1][3]:
                        self.buttons_condition = PATHS[7]
                    elif coords[2][0] < mouse_x < coords[2][2] and \
                            coords[2][1] < mouse_y < coords[2][3]:
                        self.buttons_condition = PATHS[9]
                    elif coords[3][0] < mouse_x < coords[3][2] and \
                            coords[3][1] < mouse_y < coords[3][3]:
                        self.buttons_condition = PATHS[11]
                    else:
                        self.buttons_condition = PATHS[3]

                # Обработка нажатия кнопки(отпуск клавиши)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.is_pressed = False
                    mouse_x, mouse_y = event.pos
                    coords = MAIN_MENU_BUTTONS_COORDINATES
                    if coords[0][0] < mouse_x < coords[0][2] and \
                            coords[0][1] < mouse_y < coords[0][3]:
                        self.buttons_condition = PATHS[4]
                        button = 0  # Кнопка "Играть"
                    elif coords[1][0] < mouse_x < coords[1][2] and \
                            coords[1][1] < mouse_y < coords[1][3]:
                        button = 1  # Кнопка "Сохранения"
                        self.buttons_condition = PATHS[6]
                    elif coords[2][0] < mouse_x < coords[2][2] and \
                            coords[2][1] < mouse_y < coords[2][3]:
                        self.buttons_condition = PATHS[8]
                        button = 2  # Кнопка "Настройки"
                    elif coords[3][0] < mouse_x < coords[3][2] and \
                            coords[3][1] < mouse_y < coords[3][3]:
                        self.buttons_condition = PATHS[10]
                        running = False
                    else:
                        self.buttons_condition = PATHS[3]
            pygame.display.flip()
            if button == 0:
                # Выключение музыки главного меню
                music_menu.stop()
                LevelHub().run(screen)
            elif button == 1:
                SaveHub().run(screen)
            elif button == 2:
                Settings().run(screen, music_menu)
