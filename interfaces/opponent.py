import pygame as pg
import sys

import basic_functions as func
from developers_settings import *
from music.music import Music


class Opponent:
    def __init__(self, kind):
        self.kind = kind
        ''' ^ вид противника'''
        if self.kind == 1:
            self.health = 50
            self.damage = 30
        self.cell_now = [8, 2]
        self.frame = 0
        #  раскадровачные маятники для собаки
        self.ticker_for_vibe = 1
        self.ticker_for_go = 1
        self.ticker_for_punch = 1
        self.now_hit_frame = 0

    def run(self, screen, condition, level):
        self.kind = level
        posx = FIELD_BEGIN_COORDS[0] + CELL_WIDTH * self.cell_now[0]
        posy = FIELD_BEGIN_COORDS[1] + (CELL_HEIGHT * self.cell_now[1] + 1)
        position = [posx, posy]
        if condition == 0:
            self.frame = 20
            self.ticker_for_vibe = self.ticker_for_vibe % 2 + 1
            self.render_vibing(screen, position)
        if condition == 1:
            self.frame = 22
            self.ticker_for_go = self.ticker_for_go % 8 + 1
            self.render_going(screen, position)
        if condition == 2:
            self.frame = 30
            self.ticker_for_punch = self.ticker_for_punch % 6 + 1
            self.render_punching(screen, position)
        if condition == 3:
            self.now_hit_frame += 1
            if self.now_hit_frame != 0:
                self.render_hit(screen, position, self.now_hit_frame)
            self.frame = 20
            self.ticker_for_vibe = self.ticker_for_vibe % 2 + 1
            self.render_vibing(screen, position)
            if self.now_hit_frame == 4:
                self.now_hit_frame = 0
                return False
        return self.damage, self.health

    def render_vibing(self, screen, position):
        now_frame = self.frame + self.ticker_for_vibe
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])

    def render_going(self, screen, position):
        now_frame = self.frame + self.ticker_for_go
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])

    def render_punching(self, screen, position):
        now_frame = self.frame + self.ticker_for_punch
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])

    def render_hit(self, screen, position, now_frame):
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])
