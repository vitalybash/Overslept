import basic_functions as func
from developers_settings import *


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
        self.now_go_frame = 0
        self.now_punch_frame = 0
        self.damage_given = 0
        self.main_character_pos = []

    def run(self, screen, condition, level, where, health):
        self.health = health
        self.main_character_pos = where
        self.kind = level
        print(self.cell_now)
        posx = FIELD_BEGIN_COORDS[0] + CELL_WIDTH * self.cell_now[0]
        posy = FIELD_BEGIN_COORDS[1] + (CELL_HEIGHT * self.cell_now[1] + 1)
        position = [posx, posy]
        if condition == 0:
            self.damage_given = 0
            self.frame = 20
            self.ticker_for_vibe = self.ticker_for_vibe % 2 + 1
            self.render_vibing(screen, position)
        if condition == 1:
            self.now_go_frame += 1
            if self.now_go_frame != 0:
                self.render_going(screen, position, self.now_go_frame + 22)
            self.ticker_for_go = self.ticker_for_go % 8 + 1
            if self.now_go_frame == 8:
                self.now_go_frame = 0
                return [self.health, self.cell_now, self.damage_given, False]
        if condition == 2:
            self.now_punch_frame += 1
            if self.now_punch_frame != 0:
                self.render_punching(screen, position,
                                     self.now_punch_frame + 30)
            self.ticker_for_punch = self.ticker_for_punch % 6 + 1
            if self.now_punch_frame == 6:
                self.now_punch_frame = 0
                self.damage_given = self.damage
                return [self.health, self.cell_now, self.damage_given, False]
        if condition == 3:
            self.now_hit_frame += 1
            if self.now_hit_frame != 0:
                self.render_hit(screen, position, self.now_hit_frame)
            self.ticker_for_vibe = self.ticker_for_vibe % 2 + 1
            self.render_vibing(screen, position)
            if self.now_hit_frame == 4:
                self.now_hit_frame = 0
                return [self.health, self.cell_now, self.damage_given, False]
        return [self.health, self.cell_now, self.damage_given, True]

    def think(self, turns, main_hero_pos):
        life_around_cell = 0
        self.main_character_pos = main_hero_pos
        list_of_x = [1, 1, 1, 0, 0, -1, -1, -1]
        list_of_y = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(8):
            if self.cell_now[0] + list_of_x[i] == \
                    self.main_character_pos[0] and \
                    self.cell_now[1] + list_of_y[i] == \
                    self.main_character_pos[1]:
                life_around_cell = 1
        if life_around_cell == 1:
            # тут собака укусит
            return 2, self.cell_now
        else:
            return 1, self.where_is_the_character(main_hero_pos)

    def where_is_the_character(self, char_pos):
        new_pos = []
        if char_pos[1] == self.cell_now:
            if char_pos[0] < self.cell_now[0]:
                new_pos = [self.cell_now[0] - 1, self.cell_now[1]]
            elif char_pos[0] > self.cell_now[0]:
                new_pos = [self.cell_now[0] + 1, self.cell_now[1]]
        else:
            if char_pos[1] < self.cell_now[1]:
                if char_pos[0] < self.cell_now[0]:
                    new_pos = [self.cell_now[0] - 1, self.cell_now[1] - 1]
                elif char_pos[0] > self.cell_now[0]:
                    new_pos = [self.cell_now[0] + 1, self.cell_now[1] - 1]
            elif char_pos[1] > self.cell_now[1]:
                if char_pos[0] < self.cell_now[0]:
                    new_pos = [self.cell_now[0] - 1, self.cell_now[1] + 1]
                elif char_pos[0] > self.cell_now[0]:
                    new_pos = [self.cell_now[0] + 1, self.cell_now[1] + 1]
        self.cell_now = new_pos
        return new_pos

    def render_vibing(self, screen, position):
        now_frame = self.frame + self.ticker_for_vibe
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])

    def render_going(self, screen, position, now_frame):
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])

    def render_punching(self, screen, position, now_frame):
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])

    def render_hit(self, screen, position, now_frame):
        screen.blit(func.load_hero(HEROES_PATHS[now_frame],
                                   position)[0],
                    func.load_hero(HEROES_PATHS[now_frame],
                                   position)[1])
