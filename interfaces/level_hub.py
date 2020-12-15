import pygame as pg

import basic_functions as func
from developers_settings import *


#  Класс отвечающий за реализацию хаба уровней и всего что с ним звязанно
class LevelHub:

    def __init__(self):
        self.levels_had_been_done = 'некоторый показатель ' \
                                    'уровней который мы будем ' \
                                    'брать из текущего сохранения'
        self.clock = pg.time.Clock()
        self.fps = 10
        #  кратность начального кадра теней и света
        self.number_of_frame = 3
        #  флаг отвечающий за создание надписи пионер
        self.pioner_already_here_flag = False
        #  начальный кадр надписи пионер
        self.pioner_frame = 41
        #  флаг отвечающий за создание путей
        self.ways_already_here_flag = False
        #  начальный кадр путей
        self.way_frame = 108
        #  проверка сколько уровней было пройдено
        #  и установление количества проигрываемых надписей
        if self.levels_had_been_done:
            self.end_of_pioner_frames = self.pioner_frame + 6
            self.end_of_way_frames = self.way_frame + 2

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
                screen.blit(func.load_image(PATHS[self.way_frame])[0],
                            func.load_image(PATHS[self.way_frame])[1])
            else:
                self.ways_already_here_flag = True
        if self.ways_already_here_flag:
            screen.blit(func.load_image(PATHS[self.way_frame])[0],
                        func.load_image(PATHS[self.way_frame])[1])

        #  установка надписей
        if not self.pioner_already_here_flag:
            if self.pioner_frame != self.end_of_pioner_frames:
                self.pioner_frame += 1
                screen.blit(func.load_image(PATHS[self.pioner_frame])[0],
                            func.load_image(PATHS[self.pioner_frame])[1])
            else:
                self.pioner_already_here_flag = True
        if self.pioner_already_here_flag:
            screen.blit(func.load_image(PATHS[self.pioner_frame])[0],
                        func.load_image(PATHS[self.pioner_frame])[1])

    def run(self, screen):
        running = True
        while running:
            self.render_map(screen)
            #  принятие и обработка событий
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if self.pioner_already_here_flag:

                    #  отлов наведения мышки на кнопки
                    if event.type == pg.MOUSEMOTION:
                        mouse_x, mouse_y = event.pos
                        coords = LEVEL_HUB_BUTTONS_COORDINATES
                        #  проверка наведения на "пионер"
                        if coords[0][0] < mouse_x < coords[0][2] and \
                                coords[0][1] < mouse_y < coords[0][3]:
                            self.pioner_frame = 48
                        else:
                            self.pioner_frame = 47

                    #  отлов нажатия мышки на кнопки
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        coords = LEVEL_HUB_BUTTONS_COORDINATES
                        #  проверка нажатия на "пионер"
                        if coords[0][0] < mouse_x < coords[0][2] and \
                                coords[0][1] < mouse_y < coords[0][3]:
                            self.pioner_frame = 49
                        else:
                            self.pioner_frame = 47
                    #  отлов отжатия мышки
                    if event.type == pg.MOUSEBUTTONUP:
                        mouse_x, mouse_y = event.pos
                        coords = LEVEL_HUB_BUTTONS_COORDINATES
                        #  проверка отжатия "пионер"
                        if coords[0][0] < mouse_x < coords[0][2] and \
                                coords[0][1] < mouse_y < coords[0][3]:
                            self.pioner_frame = 48
                        else:
                            self.pioner_frame = 47
            #  задержка
            self.clock.tick(self.fps)
            pg.display.flip()
