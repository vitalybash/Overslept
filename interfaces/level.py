import pygame as pg

import basic_functions as func
from developers_settings import *
from interfaces.main_character import MainCharacter
from interfaces.opponent import Opponent


class Level:
    def __init__(self, level):
        self.level = level
        self.clock = pg.time.Clock()
        self.fps = 10
        self.number_of_level_frames = 0
        self.frame = 0
        self.opponent_condition = 0
        self.main_character_condition = 3
        self.opponent = Opponent(level)
        self.main_character = MainCharacter()
        self.main_hero_health = 0
        self.opponent_health = 0
        self.pause_condition = 0

    def run(self, screen):
        running = True
        while running:
            pause_coords = PAUSE_BTN_COORDS

            self.render_level(screen)
            self.render_main_hero_health(screen)
            self.render_opponent_health(screen)
            self.render_pause_btn(screen)

            all_about_opponent = self.opponent.run(
                screen,
                self.opponent_condition, self.level)
            if not all_about_opponent:
                self.opponent_condition = 0
            if all_about_opponent:
                self.opponent_health = all_about_opponent[1]

            all_about_main_hero = self.main_character.run(
                screen,
                self.main_character_condition,
                self.level)
            if not all_about_main_hero[0]:
                self.main_character_condition = 0
            if all_about_main_hero:
                self.main_hero_health = all_about_main_hero[0]

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    if pause_coords[0] < mouse_x < pause_coords[2] and \
                            pause_coords[1] < mouse_y < pause_coords[3]:
                        self.pause_condition = 1
                    else:
                        self.pause_condition = 0

                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if pause_coords[0] < mouse_x < pause_coords[2] and \
                            pause_coords[1] < mouse_y < pause_coords[3]:
                        self.pause_condition = 2

                if event.type == pg.MOUSEBUTTONUP:
                    mouse_x, mouse_y = event.pos
                    if pause_coords[0] < mouse_x < pause_coords[2] and \
                            pause_coords[1] < mouse_y < pause_coords[3]:
                        self.pause_condition = 1
                    else:
                        self.pause_condition = 0

            self.clock.tick(self.fps)
            pg.display.flip()

    def render_level(self, screen):
        if self.level == 1:
            if self.frame == 206 or self.frame == 0:
                self.frame = 200
            screen.blit(func.load_image(PATHS[self.frame])[0],
                        func.load_image(PATHS[self.frame])[1])
            self.frame += 1

    def render_main_hero_health(self, screen):
        health_level = self.main_hero_health // 10
        health_frame = 216 - health_level
        if self.main_hero_health == 100:
            health_frame = 207
        screen.blit(func.load_health_bar(PATHS[health_frame], HEALTH_BAR)[0],
                    func.load_health_bar(PATHS[health_frame], HEALTH_BAR)[1])
        font = pg.font.SysFont('agencyfb', 40)
        text = font.render(f'{self.main_hero_health}', True, (250, 250, 250))
        screen.blit(text, (HEALTH_AMOUNT[0], HEALTH_AMOUNT[1]))

    def render_opponent_health(self, screen):
        health = 10
        if self.level == 1:
            health = 5
        health_level = self.opponent_health // health
        health_frame = 216 - health_level
        if self.opponent_health == health * 10:
            health_frame = 207
        screen.blit(func.load_health_bar(PATHS[health_frame],
                                         HEALTH_BAR_OP)[0],
                    func.load_health_bar(PATHS[health_frame],
                                         HEALTH_BAR_OP)[1])
        font = pg.font.SysFont('agencyfb', 40)
        text = font.render(f'{self.opponent_health}', True, (250, 250, 250))
        screen.blit(text, (HEALTH_AMOUNT_OP[0], HEALTH_AMOUNT_OP[1]))

    def render_pause_btn(self, screen):
        screen.blit(func.load_health_bar(PATHS[217 + self.pause_condition],
                                         PAUSE_BTN_FOR_LEVEL)[0],
                    func.load_health_bar(PATHS[217 + self.pause_condition],
                                         PAUSE_BTN_FOR_LEVEL)[1])
