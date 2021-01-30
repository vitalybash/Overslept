import pygame as pg
from developers_settings import *
import basic_functions as func
from interfaces.opponent import Opponent
from interfaces.main_character import MainCharacter
from interfaces.web import Web


class Level:
    def __init__(self, level):
        self.level = level
        self.clock = pg.time.Clock()
        self.fps = 10
        self.number_of_level_frames = 0
        self.frame = 0
        self.opponent_condition = 3
        self.main_character_condition = 3
        self.opponent = Opponent(self.level)
        self.main_character = MainCharacter()
        self.web = Web()
        self.main_hero_pos = []
        self.opponent_health = 0
        self.main_hero_health = 0
        self.turn = 0

    def run(self, screen):
        running = True
        while running:
            self.render_level(screen)

            all_about_turn = self.web.run(screen, self.turn)

            all_about_main_hero = self.main_character.run(
                screen,
                self.main_character_condition,
                self.level)
            if not all_about_main_hero[0]:
                self.main_character_condition = 0
            if all_about_main_hero:
                self.main_hero_health = all_about_main_hero[0]

            all_about_opponent = self.opponent.run(
                screen,
                self.opponent_condition, self.level, all_about_main_hero[1])
            if not all_about_opponent:
                self.opponent_condition = 0
            if all_about_opponent:
                self.opponent_health = all_about_opponent[1]

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.clock.tick(self.fps)
            pg.display.flip()

    def render_level(self, screen):
        if self.level == 1:
            if self.frame == 206 or self.frame == 0:
                self.frame = 200
            screen.blit(func.load_image(PATHS[self.frame])[0],
                        func.load_image(PATHS[self.frame])[1])
            self.frame += 1
