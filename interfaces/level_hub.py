import pygame as pg

from developers_settings import *

import basic_functions as func


class LevelHub:
    def __init__(self):
        self.levels_had_been_done = 0
        self.clock = pg.time.Clock()
        self.fps = 2
        self.running = True
        self.number_of_frame = 3

    def render(self, screen):
        screen.blit(func.load_image(PATHS[12])[0],
                    func.load_image(PATHS[12])[1])
        self.number_of_frame = self.number_of_frame % 3 + 1
        frame_for_shadow = 12 + self.number_of_frame
        frame_for_light = 15 + self.number_of_frame
        screen.blit(func.load_image(PATHS[frame_for_shadow])[0],
                    func.load_image(PATHS[frame_for_shadow])[1])
        screen.blit(func.load_image(PATHS[frame_for_light])[0],
                    func.load_image(PATHS[frame_for_light])[1])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        self.clock.tick(self.fps)
        pg.display.flip()
        return self.running