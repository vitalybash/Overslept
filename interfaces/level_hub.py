import pygame as pg

import basic_functions as func
from developers_settings import *


#  Класс отвечающий за реализацию хаба уровней и всего что с ним звязанно
class LevelHub:

    def __init__(self):
        #  некоторые показатели
        #  уровней которые мы будем
        #  брать из текущего сохранения
        self.levels_had_been_done = 8
        ''' ^ Если хочется посмотреть на отображение конкретных уровней'''
        self.health = 100
        ''' ^ Если хочется посмотреть на отображение здоровья'''
        self.money = 100
        ''' ^ Если хочется посмотреть на отображение количества денег'''

        self.clock = pg.time.Clock()
        self.fps = 10
        #  кратность начального кадра теней и света
        self.number_of_frame = 3
        #  начальный кадр всех надписей уровня
        self.level_names_frame = 41
        #  флаг отвечающий за создание надписи Пионер
        self.all_levels_already_here = False
        #  начальный кадр путей
        self.way_frame = 101
        #  флаг отвечающий за создание путей
        self.ways_already_here_flag = False
        #  создание списка кадров обычного вида надписей уровней
        self.basic_level_names_list = []
        for i in LEVEL_NAMES_BASIC_FRAMES:
            self.basic_level_names_list.append([i, False])
        #  проверка сколько уровней было пройдено
        #  и установление количества проигрываемых надписей
        if self.levels_had_been_done:
            if self.levels_had_been_done == 1:
                self.end_of_level_names_frames = 54
                self.end_of_way_frames = 112
            if self.levels_had_been_done == 2:
                self.end_of_level_names_frames = 63
                self.end_of_way_frames = 119
            if self.levels_had_been_done == 3:
                self.end_of_level_names_frames = 70
                self.end_of_way_frames = 127
            if self.levels_had_been_done == 4:
                self.end_of_level_names_frames = 77
                self.end_of_way_frames = 135
            if self.levels_had_been_done == 5:
                self.end_of_level_names_frames = 83
                self.end_of_way_frames = 143
            if self.levels_had_been_done == 6:
                self.end_of_level_names_frames = 91
                self.end_of_way_frames = 151
            if self.levels_had_been_done == 7:
                self.end_of_level_names_frames = 98
                self.end_of_way_frames = 159
            if self.levels_had_been_done == 8:
                self.end_of_level_names_frames = 98
                self.end_of_way_frames = 161
        else:
            self.end_of_level_names_frames = 47
            self.end_of_way_frames = 104

    def render_map(self, screen):
        #  установка фона
        screen.blit(func.load_image(PATHS[32])[0],
                    func.load_image(PATHS[32])[1])
        #  установление порядкового номера кадра для теней и света
        self.number_of_frame = self.number_of_frame % 3 + 1
        frame_for_shadow = 33 + self.number_of_frame
        frame_for_light = 37 + self.number_of_frame
        #  установка теней
        screen.blit(func.load_image(PATHS[frame_for_shadow])[0],
                    func.load_image(PATHS[frame_for_shadow])[1])
        #  установка свет
        screen.blit(func.load_image(PATHS[frame_for_light])[0],
                    func.load_image(PATHS[frame_for_light])[1])

        #  установка путей
        if not self.ways_already_here_flag:
            if self.way_frame != self.end_of_way_frames:
                self.way_frame += 1
                if self.way_frame not in ACTION_WAY_FRAMES:
                    screen.blit(func.load_image(PATHS[self.way_frame])[0],
                                func.load_image(PATHS[self.way_frame])[1])
                else:
                    screen.blit(func.load_image(PATHS[self.way_frame - 1])[0],
                                func.load_image(PATHS[self.way_frame - 1])[1])
            else:
                self.ways_already_here_flag = True

        #  установка надписей
        if not self.all_levels_already_here:
            if self.level_names_frame != self.end_of_level_names_frames:
                self.level_names_frame += 1
                self.names_render(screen)
                if self.level_names_frame not in ACTION_BUTTONS_FRAMES:
                    screen.blit(func.load_image(
                        PATHS[self.level_names_frame])[0],
                                func.load_image(
                                    PATHS[self.level_names_frame])[1])

            else:
                self.all_levels_already_here = True

        #  закрепление уровней
        if self.ways_already_here_flag:
            screen.blit(func.load_image(PATHS[self.way_frame])[0],
                        func.load_image(PATHS[self.way_frame])[1])
        if self.all_levels_already_here:
            for i in self.basic_level_names_list:
                if i[1]:
                    screen.blit(func.load_image(PATHS[i[0]])[0],
                                func.load_image(PATHS[i[0]])[1])
        self.health_bar_render(screen)

    def run(self, screen):
        running = True
        while running:
            self.render_map(screen)
            #  принятие и обработка событий
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if self.all_levels_already_here:

                    #  отлов наведения мышки на кнопки
                    if event.type == pg.MOUSEMOTION:
                        mouse_x, mouse_y = event.pos
                        coords = LEVEL_HUB_BUTTONS_COORDINATES
                        #  проверка наведения на "пионер"
                        if coords[0][0] < mouse_x < coords[0][2] and \
                                coords[0][1] < mouse_y < coords[0][3]:
                            self.basic_level_names_list[0][0] = 48
                        else:
                            self.basic_level_names_list[0][0] = 47
                        #  проверка наведения на "крест"
                        if coords[1][0] < mouse_x < coords[1][2] and \
                                coords[1][1] < mouse_y < coords[1][3]:
                            self.basic_level_names_list[1][0] = 55
                        else:
                            self.basic_level_names_list[1][0] = 54
                        #  проверка наведения на "книжный"
                        if coords[2][0] < mouse_x < coords[2][2] and \
                                coords[2][1] < mouse_y < coords[2][3]:
                            self.basic_level_names_list[2][0] = 64
                        else:
                            self.basic_level_names_list[2][0] = 63
                        #  проверка наведения на "спорт"
                        if coords[3][0] < mouse_x < coords[3][2] and \
                                coords[3][1] < mouse_y < coords[3][3]:
                            self.basic_level_names_list[3][0] = 71
                        else:
                            self.basic_level_names_list[3][0] = 70
                        #  проверка наведения на "мойка"
                        if coords[4][0] < mouse_x < coords[4][2] and \
                                coords[4][1] < mouse_y < coords[4][3]:
                            self.basic_level_names_list[4][0] = 78
                        else:
                            self.basic_level_names_list[4][0] = 77
                        #  проверка наведения на "спас"
                        if coords[5][0] < mouse_x < coords[5][2] and \
                                coords[5][1] < mouse_y < coords[5][3]:
                            self.basic_level_names_list[5][0] = 84
                        else:
                            self.basic_level_names_list[5][0] = 83
                        #  проверка наведения на "фрунзе"
                        if coords[6][0] < mouse_x < coords[6][2] and \
                                coords[6][1] < mouse_y < coords[6][3]:
                            self.basic_level_names_list[6][0] = 92
                        else:
                            self.basic_level_names_list[6][0] = 91
                        #  проверка наведения на "врата"
                        if coords[7][0] < mouse_x < coords[7][2] and \
                                coords[7][1] < mouse_y < coords[7][3]:
                            self.basic_level_names_list[7][0] = 99
                        else:
                            self.basic_level_names_list[7][0] = 98

                    #  отлов нажатия мышки на кнопки
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        coords = LEVEL_HUB_BUTTONS_COORDINATES
                        #  проверка нажатия на "пионер"
                        if coords[0][0] < mouse_x < coords[0][2] and \
                                coords[0][1] < mouse_y < coords[0][3]:
                            self.basic_level_names_list[0][0] = 49
                        else:
                            self.basic_level_names_list[0][0] = 47
                        #  проверка нажатия на "крест"
                        if coords[1][0] < mouse_x < coords[1][2] and \
                                coords[1][1] < mouse_y < coords[1][3]:
                            self.basic_level_names_list[1][0] = 56
                        else:
                            self.basic_level_names_list[1][0] = 54
                        #  проверка нажатия на "книжный"
                        if coords[2][0] < mouse_x < coords[2][2] and \
                                coords[2][1] < mouse_y < coords[2][3]:
                            self.basic_level_names_list[2][0] = 65
                        else:
                            self.basic_level_names_list[2][0] = 63
                        #  проверка нажатия на "спорт"
                        if coords[3][0] < mouse_x < coords[3][2] and \
                                coords[3][1] < mouse_y < coords[3][3]:
                            self.basic_level_names_list[3][0] = 72
                        else:
                            self.basic_level_names_list[3][0] = 70
                        #  проверка нажатия на "мойка"
                        if coords[4][0] < mouse_x < coords[4][2] and \
                                coords[4][1] < mouse_y < coords[4][3]:
                            self.basic_level_names_list[4][0] = 79
                        else:
                            self.basic_level_names_list[4][0] = 77
                        #  проверка нажатия на "спас"
                        if coords[5][0] < mouse_x < coords[5][2] and \
                                coords[5][1] < mouse_y < coords[5][3]:
                            self.basic_level_names_list[5][0] = 85
                        else:
                            self.basic_level_names_list[5][0] = 83
                        #  проверка нажатия на "фрунзе"
                        if coords[6][0] < mouse_x < coords[6][2] and \
                                coords[6][1] < mouse_y < coords[6][3]:
                            self.basic_level_names_list[6][0] = 93
                        else:
                            self.basic_level_names_list[6][0] = 91
                        #  проверка нажатия на "врата"
                        if coords[7][0] < mouse_x < coords[7][2] and \
                                coords[7][1] < mouse_y < coords[7][3]:
                            self.basic_level_names_list[7][0] = 100
                        else:
                            self.basic_level_names_list[7][0] = 98

                    #  отлов отжатия мышки
                    if event.type == pg.MOUSEBUTTONUP:
                        mouse_x, mouse_y = event.pos
                        coords = LEVEL_HUB_BUTTONS_COORDINATES
                        #  проверка отжатия "пионер"
                        if coords[0][0] < mouse_x < coords[0][2] and \
                                coords[0][1] < mouse_y < coords[0][3]:
                            self.basic_level_names_list[0][0] = 48
                        else:
                            self.basic_level_names_list[0][0] = 47
                        #  проверка отжатия "крест"
                        if coords[1][0] < mouse_x < coords[1][2] and \
                                coords[1][1] < mouse_y < coords[1][3]:
                            self.basic_level_names_list[1][0] = 55
                        else:
                            self.basic_level_names_list[1][0] = 54
                        #  проверка отжатия "книжный"
                        if coords[2][0] < mouse_x < coords[2][2] and \
                                coords[2][1] < mouse_y < coords[2][3]:
                            self.basic_level_names_list[2][0] = 64
                        else:
                            self.basic_level_names_list[2][0] = 63
                        #  проверка отжатия "спорт"
                        if coords[3][0] < mouse_x < coords[3][2] and \
                                coords[3][1] < mouse_y < coords[3][3]:
                            self.basic_level_names_list[3][0] = 71
                        else:
                            self.basic_level_names_list[3][0] = 70
                        #  проверка отжатия "мойка"
                        if coords[4][0] < mouse_x < coords[4][2] and \
                                coords[4][1] < mouse_y < coords[4][3]:
                            self.basic_level_names_list[4][0] = 78
                        else:
                            self.basic_level_names_list[4][0] = 77
                        #  проверка отжатия "спас"
                        if coords[5][0] < mouse_x < coords[5][2] and \
                                coords[5][1] < mouse_y < coords[5][3]:
                            self.basic_level_names_list[5][0] = 84
                        else:
                            self.basic_level_names_list[5][0] = 83
                        #  проверка отжатия "фрунзе"
                        if coords[6][0] < mouse_x < coords[6][2] and \
                                coords[6][1] < mouse_y < coords[6][3]:
                            self.basic_level_names_list[6][0] = 92
                        else:
                            self.basic_level_names_list[6][0] = 91
                        #  проверка отжатия "врата"
                        if coords[7][0] < mouse_x < coords[7][2] and \
                                coords[7][1] < mouse_y < coords[7][3]:
                            self.basic_level_names_list[7][0] = 99
                        else:
                            self.basic_level_names_list[7][0] = 98

            #  задержка
            self.clock.tick(self.fps)
            pg.display.flip()

    def names_render(self, screen):
        if self.level_names_frame == 47:
            self.basic_level_names_list[0][1] = True
        if self.level_names_frame == 54:
            self.basic_level_names_list[1][1] = True
        if self.level_names_frame == 63:
            self.basic_level_names_list[2][1] = True
        if self.level_names_frame == 70:
            self.basic_level_names_list[3][1] = True
        if self.level_names_frame == 77:
            self.basic_level_names_list[4][1] = True
        if self.level_names_frame == 83:
            self.basic_level_names_list[5][1] = True
        if self.level_names_frame == 91:
            self.basic_level_names_list[6][1] = True
        if self.level_names_frame == 98:
            self.basic_level_names_list[7][1] = True
        for i in self.basic_level_names_list:
            if i[1]:
                screen.blit(func.load_image(PATHS[i[0]])[0],
                            func.load_image(PATHS[i[0]])[1])

    def health_bar_render(self, screen):
        health_level = self.health // 10
        health_frame = 163 + health_level
        if self.health == 0:
            health_frame = 164
        screen.blit(func.load_image(PATHS[health_frame])[0],
                    func.load_image(PATHS[health_frame])[1])
        font = pg.font.SysFont('agencyfb', 40)
        text = font.render(f'{self.health}', True, (250, 250, 250))
        screen.blit(text, (HEALTH_PLACE[0], HEALTH_PLACE[1]))
