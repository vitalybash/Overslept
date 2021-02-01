import basic_functions as func
from developers_settings import *


class MainCharacter:
    def __init__(self):
        self.kind = 0
        self.health = 100
        self.damage = 20
        self.cell_now = []
        self.frame = 0
        self.ticker_for_vibe = 1
        self.ticker_for_go = 1
        self.ticker_for_punch = 1
        self.now_hit_frame = 0
        self.now_punch_frame = 0
        self.now_go_frame = 0
        self.damage_given = 0

    def run(self, screen, condition, level, pos):
        self.cell_now = pos
        self.kind = level
        posx = FIELD_BEGIN_COORDS[0] + CELL_WIDTH * self.cell_now[0] - 115
        posy = FIELD_BEGIN_COORDS[1] + \
               (CELL_HEIGHT * self.cell_now[1] + 1) + 10
        position = [posx, posy]
        if condition == 0:
            self.frame = 5
            self.ticker_for_vibe = self.ticker_for_vibe % 2 + 1
            self.render_vibing(screen, position)
        if condition == 1:
            self.now_go_frame += 1
            if self.now_go_frame != 0:
                self.render_going(screen, position, self.now_go_frame + 7)
            self.frame = 7
            self.ticker_for_go = self.ticker_for_go % 5 + 1
            if self.now_go_frame == 5:
                self.now_go_frame = 0
                return [self.health, self.cell_now, self.damage_given, False]
        if condition == 2:
            self.now_punch_frame += 1
            if self.now_punch_frame != 0:
                self.render_punching(screen, position, self.now_punch_frame + 12)
            self.frame = 12
            self.ticker_for_punch = self.ticker_for_punch % 7 + 1
            if self.now_punch_frame == 7:
                self.now_punch_frame = 0
                return [self.health, self.cell_now, self.damage_given, False]
        if condition == 3:
            self.now_hit_frame += 1
            if self.now_hit_frame != 0:
                self.render_hit(screen, position, self.now_hit_frame)
            self.frame = 5
            self.ticker_for_vibe = self.ticker_for_vibe % 2 + 1
            self.render_vibing(screen, position)
            if self.now_hit_frame == 4:
                self.now_hit_frame = 0
                return [self.health, self.cell_now, self.damage_given, False]
        return [self.health, self.cell_now, self.damage_given, True]

    def render_vibing(self, screen, position):
        now_frame = self.frame + self.ticker_for_vibe
        screen.blit(func.load_main_hero(HEROES_PATHS[now_frame],
                                        position)[0],
                    func.load_main_hero(HEROES_PATHS[now_frame],
                                        position)[1])

    def render_going(self, screen, position, now_frame):
        screen.blit(func.load_main_hero(HEROES_PATHS[now_frame],
                                        position)[0],
                    func.load_main_hero(HEROES_PATHS[now_frame],
                                        position)[1])

    def render_punching(self, screen, position, now_frame):
        screen.blit(func.load_main_hero(HEROES_PATHS[now_frame],
                                        position)[0],
                    func.load_main_hero(HEROES_PATHS[now_frame],
                                        position)[1])

    def render_hit(self, screen, position, now_frame):
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])
