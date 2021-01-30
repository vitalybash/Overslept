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
        self.damage_given = 0
        self.main_character_pos = []

    def run(self, screen, condition, level, main_character_pos):
        self.main_character_pos = main_character_pos
        self.kind = level
        posx = FIELD_BEGIN_COORDS[0] + CELL_WIDTH * self.cell_now[0]
        posy = FIELD_BEGIN_COORDS[1] + (CELL_HEIGHT * self.cell_now[1] + 1)
        position = [posx, posy]
        if condition == 0:
            self.damage_given = 0
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
            self.damage_given = self.damage
        if condition == 3:
            self.now_hit_frame += 1
            if self.now_hit_frame != 0:
                self.render_hit(screen, position, self.now_hit_frame)
            self.frame = 20
            self.ticker_for_vibe = self.ticker_for_vibe % 2 + 1
            self.render_vibing(screen, position)
            if self.now_hit_frame == 4:
                self.now_hit_frame = 0
                return False, self.cell_now, self.health - 15
        return self.damage_given, self.cell_now, self.health

    def think(self):
        list_of_x = [1, 1, 1, 0, 0, -1, -1, -1]
        list_of_y = [-1, 0, 1, -1, 1, -1, 0, 1]
        for row in range(3):
            for col in range(9):
                life_around_cell = 0
                for dx, dy in zip(list_of_x, list_of_y):
                    if col + dx < 0 or col + dx >= 9 or \
                            row + dy < 0 or row + dy >= 3:
                        continue

                if life_around_cell == 1:
                    # тут собака укусит
                    return True
                else:
                    if self.main_character_pos[1] != self.cell_now[1]:
                        self.cell_now[1] = self.main_character_pos[1]
                    if self.main_character_pos[0] < self.cell_now[0]:
                        self.cell_now[0] = self.cell_now[0] - 1

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
