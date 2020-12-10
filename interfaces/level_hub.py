import sys
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
        self.number_of_frame = 3

    def run(self, screen):
        running = True
        while running:
            #  установка фона
            screen.blit(func.load_image(PATHS[12])[0],
                        func.load_image(PATHS[12])[1])
            #  установление порядкового номера кадра для теней и света
            self.number_of_frame = self.number_of_frame % 3 + 1
            frame_for_shadow = 12 + self.number_of_frame
            frame_for_light = 15 + self.number_of_frame
            #  установка теней
            screen.blit(func.load_image(PATHS[frame_for_shadow])[0],
                        func.load_image(PATHS[frame_for_shadow])[1])

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    return
            #  задержка
            self.clock.tick(self.fps)
            pg.display.flip()
        pg.quit()
