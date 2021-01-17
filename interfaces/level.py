import pygame as pg
from developers_settings import *
import basic_functions as func


class Level:
    def __init__(self, level):
        self.level = level
        self.clock = pg.time.Clock()
        self.fps = 10
        self.number_of_level_frames = 0
        self.frame = 0

    def run(self, screen):
        running = True
        while running:
            self.render_level(screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    print(1)
                    running = False
            self.clock.tick(self.fps)
            pg.display.flip()

    def render_level(self, screen):
        if self.level == 1:
            if self.frame == 198 or self.frame == 0:
                self.frame = 192
            screen.blit(func.load_image(PATHS[self.frame])[0],
                        func.load_image(PATHS[self.frame])[1])
            self.frame += 1
