import pygame as pg
import sys

import basic_functions as func
from developers_settings import *
from music.music import Music
from interfaces.level import Level


#  Класс отвечающий за реализацию хаба уровней и всего что с ним звязанно
class LevelHub:

    def __init__(self):
        #  некоторые показатели
        #  уровней которые мы будем
        #  брать из текущего сохранения
        self.levels_had_been_done = 8
        ''' ^ Если хочется посмотреть на отображение конкретных уровней'''
        self.health = 100
        ''' ^ Если хочется посмотреть на отображение здоровья'''
        self.money = 100
        ''' ^ Если хочется посмотреть на отображение количества денег'''
        self.exp_count = 0
        ''' ^ Счёт опыта игрока'''
        self.accuracy = 0
        ''' ^ Уровень меткости'''
        self.defence = 0
        ''' ^ Уровень защиты'''
        self.speed = 0
        ''' ^ Уровень скорости'''
        self.clock = pg.time.Clock()
        self.fps = 60
        #  кратность начального кадра теней и света
        self.number_of_frame = 3
        #  начальный кадр всех надписей уровня
        self.level_names_frame = 41
        #  флаг отвечающий за создание надписи Пионер
        self.all_levels_already_here = False
        #  начальный кадр путей
        self.way_frame = 101
        #  флаг отвечающий за создание путей
        self.ways_already_here_flag = False
        #  создание списка кадров обычного вида надписей уровней
        self.basic_level_names_list = []
        for i in LEVEL_NAMES_BASIC_FRAMES:
            self.basic_level_names_list.append([i, False])
        #  проверка сколько уровней было пройдено
        #  и установление количества проигрываемых надписей
        if self.levels_had_been_done:
            if self.levels_had_been_done == 1:
                self.end_of_level_names_frames = 54
                self.end_of_way_frames = 112
            if self.levels_had_been_done == 2:
                self.end_of_level_names_frames = 63
                self.end_of_way_frames = 119
            if self.levels_had_been_done == 3:
                self.end_of_level_names_frames = 70
                self.end_of_way_frames = 127
            if self.levels_had_been_done == 4:
                self.end_of_level_names_frames = 77
                self.end_of_way_frames = 135
            if self.levels_had_been_done == 5:
                self.end_of_level_names_frames = 83
                self.end_of_way_frames = 143
            if self.levels_had_been_done == 6:
                self.end_of_level_names_frames = 91
                self.end_of_way_frames = 151
            if self.levels_had_been_done == 7:
                self.end_of_level_names_frames = 98
                self.end_of_way_frames = 159
            if self.levels_had_been_done == 8:
                self.end_of_level_names_frames = 98
                self.end_of_way_frames = 161
        else:
            self.end_of_level_names_frames = 47
            self.end_of_way_frames = 104
        #  кадр обычного вида кнопки паузы
        self.pause_button_frame = 175
        #  флаг появления магазина оружия
        self.visible_guns = False
        #  флаг появления магазина еды
        self.visible_food = False
        #  флаг появления магазина умений
        self.visible_skills = False
        #  тригер паузы
        self.pause_trigger = False
        #  подсчёт кадров для смены кадра тени и света
        self.light_frame = 0
        #  начальный кадр теней
        self.frame_for_shadow = 34
        #  начальный кадр света
        self.frame_for_light = 38
        #  тригер магазина
        self.shop_trigger = False

    def render_map(self, screen):
        #  установка фона
        screen.blit(func.load_image(PATHS[32])[0],
                    func.load_image(PATHS[32])[1])

        #  отрисовка теней и света
        self.light_render(screen)

        #  установка путей
        if not self.ways_already_here_flag:
            if self.way_frame != self.end_of_way_frames:
                self.way_frame += 1
                if self.way_frame not in ACTION_WAY_FRAMES:
                    screen.blit(func.load_image(PATHS[self.way_frame])[0],
                                func.load_image(PATHS[self.way_frame])[1])
                else:
                    screen.blit(func.load_image(PATHS[self.way_frame - 1])[0],
                                func.load_image(PATHS[self.way_frame - 1])[1])
            else:
                self.ways_already_here_flag = True

        #  установка надписей
        if not self.all_levels_already_here:
            if self.level_names_frame != self.end_of_level_names_frames:
                self.level_names_frame += 1
                self.names_render(screen)
                if self.level_names_frame not in ACTION_BUTTONS_FRAMES:
                    screen.blit(func.load_image(
                        PATHS[self.level_names_frame])[0],
                                func.load_image(
                                    PATHS[self.level_names_frame])[1])

            else:
                self.all_levels_already_here = True

        #  закрепление уровней
        if self.ways_already_here_flag:
            screen.blit(func.load_image(PATHS[self.way_frame])[0],
                        func.load_image(PATHS[self.way_frame])[1])
        if self.all_levels_already_here:
            for i in self.basic_level_names_list:
                if i[1]:
                    screen.blit(func.load_image(PATHS[i[0]])[0],
                                func.load_image(PATHS[i[0]])[1])
        self.health_bar_render(screen)

    def light_render(self, screen):
        if self.light_frame % 6 == 0:
            #  установление порядкового номера кадра для теней и света
            if not self.pause_trigger:
                self.number_of_frame = self.number_of_frame % 3 + 1
                self.frame_for_shadow = 33 + self.number_of_frame
                self.frame_for_light = 37 + self.number_of_frame
            else:
                self.frame_for_shadow = 34
                self.frame_for_light = 38

        #  установка теней
        screen.blit(func.load_image(PATHS[self.frame_for_shadow])[0],
                    func.load_image(PATHS[self.frame_for_shadow])[1])
        #  установка свет
        screen.blit(func.load_image(PATHS[self.frame_for_light])[0],
                    func.load_image(PATHS[self.frame_for_light])[1])

    def run(self, screen):
        # Установка музыки карты
        music_map = Music('map_melody.ogg')
        music_map.run()
        pause_condition = 0
        shop_condition = 0
        running = True
        while running:
            #  отрисовка карты уровней и уровня здоровья
            self.render_map(screen)
            #  отрисовка баланса и кнопки паузы
            self.money_and_pauseBtn_render(screen)
            #  отрисовка отображения магазинов
            if not self.pause_trigger and not self.shop_trigger:
                self.shops_render(screen)
            #  отслеживание потребности в паузе
            if self.pause_trigger:
                self.render_pause(screen, pause_condition)
            if self.shop_trigger:
                self.exp_shop_render(screen, shop_condition)
            #  значение кнопки
            button = None

            #  принятие и обработка событий
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    # Остановка музыки карты
                    music_map.stop()
                    # Остановка работы pygame и программы
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    # Обработчик клавиш
                    if event.key == pg.K_ESCAPE:
                        running = False

                if self.all_levels_already_here:

                    #  координаты названий уровней
                    coords = LEVEL_HUB_BUTTONS_COORDINATES

                    #  координаты кнопки паузы
                    pause_cords = PAUSE_BUTTON_COORDINATES

                    #  координаты кнопок в меню паузы

                    #  продолжить
                    pause_play = PAUSE_PLAY_BUTTON
                    #  сохраниться
                    pause_save = PAUSE_SAVE_BUTTON
                    #  выйти
                    pause_exit = PAUSE_EXIT_BUTTON

                    #  координаты магазина оружия
                    gun_shop = GUN_MAGAZINE

                    #  координаты магазина еды
                    food_shop = FOOD_MAGAZINE

                    #  координаты магазина умений
                    skill_shop = SKILLS_MAGAZINE

                    #  координаты магазина умения
                    skill_wnd = SHOP_WND_POSITION

                    #  координаты кнопок магазина умений
                    acc_btn = ACCURACY_PLACE
                    def_btn = DEFENCE_PLACE
                    spe_btn = SPEED_PLACE

                    #  проверка нажатой паузы
                    if not self.pause_trigger and not self.shop_trigger:
                        #  отлов наведения мышки на кнопки
                        if event.type == pg.MOUSEMOTION:
                            mouse_x, mouse_y = event.pos

                            #  проверка наведения на "пионер"
                            if coords[0][0] < mouse_x < coords[0][2] and \
                                    coords[0][1] < mouse_y < coords[0][3]:
                                self.basic_level_names_list[0][0] = 48
                            else:
                                self.basic_level_names_list[0][0] = 47
                            #  проверка наведения на "крест"
                            if coords[1][0] < mouse_x < coords[1][2] and \
                                    coords[1][1] < mouse_y < coords[1][3]:
                                self.basic_level_names_list[1][0] = 55
                            else:
                                self.basic_level_names_list[1][0] = 54
                            #  проверка наведения на "книжный"
                            if coords[2][0] < mouse_x < coords[2][2] and \
                                    coords[2][1] < mouse_y < coords[2][3]:
                                self.basic_level_names_list[2][0] = 64
                            else:
                                self.basic_level_names_list[2][0] = 63
                            #  проверка наведения на "спорт"
                            if coords[3][0] < mouse_x < coords[3][2] and \
                                    coords[3][1] < mouse_y < coords[3][3]:
                                self.basic_level_names_list[3][0] = 71
                            else:
                                self.basic_level_names_list[3][0] = 70
                            #  проверка наведения на "мойка"
                            if coords[4][0] < mouse_x < coords[4][2] and \
                                    coords[4][1] < mouse_y < coords[4][3]:
                                self.basic_level_names_list[4][0] = 78
                            else:
                                self.basic_level_names_list[4][0] = 77
                            #  проверка наведения на "спас"
                            if coords[5][0] < mouse_x < coords[5][2] and \
                                    coords[5][1] < mouse_y < coords[5][3]:
                                self.basic_level_names_list[5][0] = 84
                            else:
                                self.basic_level_names_list[5][0] = 83
                            #  проверка наведения на "фрунзе"
                            if coords[6][0] < mouse_x < coords[6][2] and \
                                    coords[6][1] < mouse_y < coords[6][3]:
                                self.basic_level_names_list[6][0] = 92
                            else:
                                self.basic_level_names_list[6][0] = 91
                            #  проверка наведения на "врата"
                            if coords[7][0] < mouse_x < coords[7][2] and \
                                    coords[7][1] < mouse_y < coords[7][3]:
                                self.basic_level_names_list[7][0] = 99
                            else:
                                self.basic_level_names_list[7][0] = 98

                            #  отлов наведения на кнопку паузы
                            if pause_cords[0] < mouse_x < pause_cords[2] and \
                                    pause_cords[1] < mouse_y < pause_cords[3]:
                                self.pause_button_frame = 176
                            else:
                                self.pause_button_frame = 175

                            #  отлов наведения на магазин оружия
                            if gun_shop[0] < mouse_x < gun_shop[2] and \
                                    gun_shop[1] < mouse_y < gun_shop[3]:
                                self.visible_guns = True
                            else:
                                self.visible_guns = False

                            #  отлов наведения на магазин еды
                            if food_shop[0] < mouse_x < food_shop[2] and \
                                    food_shop[1] < mouse_y < food_shop[3]:
                                self.visible_food = True
                            else:
                                self.visible_food = False

                            #  отлов наведения на магазин умений
                            if skill_shop[0] < mouse_x < skill_shop[2] and \
                                    skill_shop[1] < mouse_y < skill_shop[3]:
                                self.visible_skills = True
                            else:
                                self.visible_skills = False

                        #  отлов нажатия мышки на кнопки
                        if event.type == pg.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = event.pos

                            #  проверка нажатия на "пионер"
                            if coords[0][0] < mouse_x < coords[0][2] and \
                                    coords[0][1] < mouse_y < coords[0][3]:
                                self.basic_level_names_list[0][0] = 49
                            else:
                                self.basic_level_names_list[0][0] = 47
                            #  проверка нажатия на "крест"
                            if coords[1][0] < mouse_x < coords[1][2] and \
                                    coords[1][1] < mouse_y < coords[1][3]:
                                self.basic_level_names_list[1][0] = 56
                            else:
                                self.basic_level_names_list[1][0] = 54
                            #  проверка нажатия на "книжный"
                            if coords[2][0] < mouse_x < coords[2][2] and \
                                    coords[2][1] < mouse_y < coords[2][3]:
                                self.basic_level_names_list[2][0] = 65
                            else:
                                self.basic_level_names_list[2][0] = 63
                            #  проверка нажатия на "спорт"
                            if coords[3][0] < mouse_x < coords[3][2] and \
                                    coords[3][1] < mouse_y < coords[3][3]:
                                self.basic_level_names_list[3][0] = 72
                            else:
                                self.basic_level_names_list[3][0] = 70
                            #  проверка нажатия на "мойка"
                            if coords[4][0] < mouse_x < coords[4][2] and \
                                    coords[4][1] < mouse_y < coords[4][3]:
                                self.basic_level_names_list[4][0] = 79
                            else:
                                self.basic_level_names_list[4][0] = 77
                            #  проверка нажатия на "спас"
                            if coords[5][0] < mouse_x < coords[5][2] and \
                                    coords[5][1] < mouse_y < coords[5][3]:
                                self.basic_level_names_list[5][0] = 85
                            else:
                                self.basic_level_names_list[5][0] = 83
                            #  проверка нажатия на "фрунзе"
                            if coords[6][0] < mouse_x < coords[6][2] and \
                                    coords[6][1] < mouse_y < coords[6][3]:
                                self.basic_level_names_list[6][0] = 93
                            else:
                                self.basic_level_names_list[6][0] = 91
                            #  проверка нажатия на "врата"
                            if coords[7][0] < mouse_x < coords[7][2] and \
                                    coords[7][1] < mouse_y < coords[7][3]:
                                self.basic_level_names_list[7][0] = 100
                            else:
                                self.basic_level_names_list[7][0] = 98

                            #  отлов нажатия на кнопку паузы
                            if pause_cords[0] < mouse_x < pause_cords[2] and \
                                    pause_cords[1] < mouse_y < pause_cords[3]:
                                self.pause_button_frame = 177
                            else:
                                self.pause_button_frame = 175

                            #  отлов нажатия на магазин оружия
                            if gun_shop[0] < mouse_x < gun_shop[2] and \
                                    gun_shop[1] < mouse_y < gun_shop[3]:
                                self.visible_guns = True
                            else:
                                self.visible_guns = False

                            #  отлов нажатия на магазин еды
                            if food_shop[0] < mouse_x < food_shop[2] and \
                                    food_shop[1] < mouse_y < food_shop[3]:
                                self.visible_food = True
                            else:
                                self.visible_food = False

                            #  отлов нажатия на магазин умений
                            if skill_shop[0] < mouse_x < skill_shop[2] and \
                                    skill_shop[1] < mouse_y < skill_shop[3]:
                                self.visible_skills = True
                            else:
                                self.visible_skills = False

                        #  отлов отжатия мышки
                        if event.type == pg.MOUSEBUTTONUP:
                            mouse_x, mouse_y = event.pos

                            #  проверка отжатия "пионер"
                            if coords[0][0] < mouse_x < coords[0][2] and \
                                    coords[0][1] < mouse_y < coords[0][3]:
                                self.basic_level_names_list[0][0] = 48
                                button = 1
                            else:
                                self.basic_level_names_list[0][0] = 47
                            #  проверка отжатия "крест"
                            if coords[1][0] < mouse_x < coords[1][2] and \
                                    coords[1][1] < mouse_y < coords[1][3]:
                                self.basic_level_names_list[1][0] = 55
                            else:
                                self.basic_level_names_list[1][0] = 54
                            #  проверка отжатия "книжный"
                            if coords[2][0] < mouse_x < coords[2][2] and \
                                    coords[2][1] < mouse_y < coords[2][3]:
                                self.basic_level_names_list[2][0] = 64
                            else:
                                self.basic_level_names_list[2][0] = 63
                            #  проверка отжатия "спорт"
                            if coords[3][0] < mouse_x < coords[3][2] and \
                                    coords[3][1] < mouse_y < coords[3][3]:
                                self.basic_level_names_list[3][0] = 71
                            else:
                                self.basic_level_names_list[3][0] = 70
                            #  проверка отжатия "мойка"
                            if coords[4][0] < mouse_x < coords[4][2] and \
                                    coords[4][1] < mouse_y < coords[4][3]:
                                self.basic_level_names_list[4][0] = 78
                            else:
                                self.basic_level_names_list[4][0] = 77
                            #  проверка отжатия "спас"
                            if coords[5][0] < mouse_x < coords[5][2] and \
                                    coords[5][1] < mouse_y < coords[5][3]:
                                self.basic_level_names_list[5][0] = 84
                            else:
                                self.basic_level_names_list[5][0] = 83
                            #  проверка отжатия "фрунзе"
                            if coords[6][0] < mouse_x < coords[6][2] and \
                                    coords[6][1] < mouse_y < coords[6][3]:
                                self.basic_level_names_list[6][0] = 92
                            else:
                                self.basic_level_names_list[6][0] = 91
                            #  проверка отжатия "врата"
                            if coords[7][0] < mouse_x < coords[7][2] and \
                                    coords[7][1] < mouse_y < coords[7][3]:
                                self.basic_level_names_list[7][0] = 99
                            else:
                                self.basic_level_names_list[7][0] = 98

                            #  отлов отжатия кнопки паузы
                            if pause_cords[0] < mouse_x < pause_cords[2] and \
                                    pause_cords[1] < mouse_y < pause_cords[3]:
                                self.pause_button_frame = 176
                                self.pause_trigger = True
                            else:
                                self.pause_button_frame = 175

                            #  отлов отжатия магазина оружия
                            if gun_shop[0] < mouse_x < gun_shop[2] and \
                                    gun_shop[1] < mouse_y < gun_shop[3]:
                                self.visible_guns = True
                            else:
                                self.visible_guns = False

                            #  отлов отжатия магазина еды
                            if food_shop[0] < mouse_x < food_shop[2] and \
                                    food_shop[1] < mouse_y < food_shop[3]:
                                self.visible_food = True
                            else:
                                self.visible_food = False

                            #  отлов отжатия магазина умений
                            if skill_shop[0] < mouse_x < skill_shop[2] and \
                                    skill_shop[1] < mouse_y < skill_shop[3]:
                                self.visible_skills = True
                                self.shop_trigger = True
                            else:
                                self.visible_skills = False

                    if self.pause_trigger:
                        if event.type == pg.QUIT:
                            self.pause_trigger = False

                        if event.type == pg.MOUSEMOTION:
                            mouse_x, mouse_y = event.pos

                            #  отслеживание наведения продолжить
                            if pause_play[0] < mouse_x < pause_play[2] and \
                                    pause_play[1] < mouse_y < pause_play[3]:
                                pause_condition = 1
                            #  отслеживание наведения сохраниться
                            elif pause_save[0] < mouse_x < pause_save[2] and \
                                    pause_save[1] < mouse_y < pause_save[3]:
                                pause_condition = 3
                            #  отслеживание наведения выход
                            elif pause_exit[0] < mouse_x < pause_exit[2] and \
                                    pause_exit[1] < mouse_y < pause_exit[3]:
                                pause_condition = 5
                            else:
                                pause_condition = 0

                        if event.type == pg.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = event.pos

                            #  отслеживание нажатия продолжить
                            if pause_play[0] < mouse_x < pause_play[2] and \
                                    pause_play[1] < mouse_y < pause_play[3]:
                                pause_condition = 2
                            #  отслеживание нажатия сохраниться
                            elif pause_save[0] < mouse_x < pause_save[2] and \
                                    pause_save[1] < mouse_y < pause_save[3]:
                                pause_condition = 4
                            #  отслеживание нажатия выход
                            elif pause_exit[0] < mouse_x < pause_exit[2] and \
                                    pause_exit[1] < mouse_y < pause_exit[3]:
                                pause_condition = 6
                            else:
                                pause_condition = 0

                        if event.type == pg.MOUSEBUTTONUP:
                            mouse_x, mouse_y = event.pos

                            #  отслеживание отжатия продолжить
                            if pause_play[0] < mouse_x < pause_play[2] and \
                                    pause_play[1] < mouse_y < pause_play[3]:
                                pause_condition = 1
                                self.pause_trigger = False
                            #  отслеживание отжатия сохраниться
                            elif pause_save[0] < mouse_x < pause_save[2] and \
                                    pause_save[1] < mouse_y < pause_save[3]:
                                pause_condition = 3
                            #  отслеживание отжатия выход
                            elif pause_exit[0] < mouse_x < pause_exit[2] and \
                                    pause_exit[1] < mouse_y < pause_exit[3]:
                                pause_condition = 5
                                running = False
                            else:
                                pause_condition = 0

                    if self.shop_trigger:
                        if event.type == pg.QUIT:
                            self.pause_trigger = False

                        if event.type == pg.MOUSEMOTION:
                            mouse_x, mouse_y = event.pos

                            if skill_wnd[0] < mouse_x < skill_wnd[2] and \
                                    skill_wnd[1] < mouse_y < skill_wnd[3]:

                                if acc_btn[0] < mouse_x < acc_btn[2] and \
                                        acc_btn[1] < mouse_y < acc_btn[3]:
                                    shop_condition = 1

                                if def_btn[0] < mouse_x < def_btn[2] and \
                                        def_btn[1] < mouse_y < def_btn[3]:
                                    shop_condition = 3

                                if spe_btn[0] < mouse_x < spe_btn[2] and \
                                        spe_btn[1] < mouse_y < spe_btn[3]:
                                    shop_condition = 5

                        if event.type == pg.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = event.pos

                            if skill_wnd[0] < mouse_x < skill_wnd[2] and \
                                    skill_wnd[1] < mouse_y < skill_wnd[3]:

                                if acc_btn[0] < mouse_x < acc_btn[2] and \
                                        acc_btn[1] < mouse_y < acc_btn[3]:
                                    shop_condition = 2

                                elif def_btn[0] < mouse_x < def_btn[2] and \
                                        def_btn[1] < mouse_y < def_btn[3]:
                                    shop_condition = 4

                                elif spe_btn[0] < mouse_x < spe_btn[2] and \
                                        spe_btn[1] < mouse_y < spe_btn[3]:
                                    shop_condition = 6
                            else:
                                self.shop_trigger = False

                        if event.type == pg.MOUSEBUTTONUP:
                            mouse_x, mouse_y = event.pos

                            if skill_wnd[0] < mouse_x < skill_wnd[2] and \
                                    skill_wnd[1] < mouse_y < skill_wnd[3]:

                                if acc_btn[0] < mouse_x < acc_btn[2] and \
                                        acc_btn[1] < mouse_y < acc_btn[3]:
                                    shop_condition = 1

                                if def_btn[0] < mouse_x < def_btn[2] and \
                                        def_btn[1] < mouse_y < def_btn[3]:
                                    shop_condition = 3

                                if spe_btn[0] < mouse_x < spe_btn[2] and \
                                        spe_btn[1] < mouse_y < spe_btn[3]:
                                    shop_condition = 5
                                else:
                                    shop_condition = 0

            #  задержка
            self.clock.tick(self.fps)
            pg.display.flip()
            self.light_frame += 1
            if button == 1:
                Level(1).run(screen)
            #  проверка нажатия на паузу

    def names_render(self, screen):
        if self.level_names_frame == 47:
            self.basic_level_names_list[0][1] = True
        if self.level_names_frame == 54:
            self.basic_level_names_list[1][1] = True
        if self.level_names_frame == 63:
            self.basic_level_names_list[2][1] = True
        if self.level_names_frame == 70:
            self.basic_level_names_list[3][1] = True
        if self.level_names_frame == 77:
            self.basic_level_names_list[4][1] = True
        if self.level_names_frame == 83:
            self.basic_level_names_list[5][1] = True
        if self.level_names_frame == 91:
            self.basic_level_names_list[6][1] = True
        if self.level_names_frame == 98:
            self.basic_level_names_list[7][1] = True
        for i in self.basic_level_names_list:
            if i[1]:
                screen.blit(func.load_image(PATHS[i[0]])[0],
                            func.load_image(PATHS[i[0]])[1])

    def health_bar_render(self, screen):
        health_level = self.health // 10
        health_frame = 163 + health_level
        if self.health == 0:
            health_frame = 164
        screen.blit(func.load_image(PATHS[health_frame])[0],
                    func.load_image(PATHS[health_frame])[1])
        font = pg.font.SysFont('agencyfb', 40)
        text = font.render(f'{self.health}', True, (250, 250, 250))
        screen.blit(text, (HEALTH_PLACE[0], HEALTH_PLACE[1]))

    def money_and_pauseBtn_render(self, screen):
        screen.blit(func.load_image(PATHS[self.pause_button_frame])[0],
                    func.load_image(PATHS[self.pause_button_frame])[1])
        font = pg.font.SysFont('agencyfb', 40)
        text = font.render(f'{self.money}', True, (200, 200, 200))
        screen.blit(text, (MONEY_PLACE[0], MONEY_PLACE[1]))

    def shops_render(self, screen):
        if self.visible_guns:
            screen.blit(func.load_image(PATHS[179])[0],
                        func.load_image(PATHS[179])[1])
        elif self.visible_food:
            screen.blit(func.load_image(PATHS[180])[0],
                        func.load_image(PATHS[180])[1])
        elif self.visible_skills:
            screen.blit(func.load_image(PATHS[181])[0],
                        func.load_image(PATHS[181])[1])
        else:
            screen.blit(func.load_image(PATHS[182])[0],
                        func.load_image(PATHS[182])[1])

    def exp_shop_render(self, screen, condition):
        if condition == 0:
            screen.blit(func.load_image(PATHS[192])[0],
                        func.load_image(PATHS[192])[1])
        if condition == 1:
            screen.blit(func.load_image(PATHS[193])[0],
                        func.load_image(PATHS[193])[1])
        if condition == 2:
            screen.blit(func.load_image(PATHS[194])[0],
                        func.load_image(PATHS[194])[1])
        if condition == 3:
            screen.blit(func.load_image(PATHS[195])[0],
                        func.load_image(PATHS[195])[1])
        if condition == 4:
            screen.blit(func.load_image(PATHS[196])[0],
                        func.load_image(PATHS[196])[1])
        if condition == 5:
            screen.blit(func.load_image(PATHS[197])[0],
                        func.load_image(PATHS[197])[1])
        if condition == 6:
            screen.blit(func.load_image(PATHS[198])[0],
                        func.load_image(PATHS[198])[1])
        font = pg.font.SysFont('agencyfb', 27)
        text = font.render('меткость', True, (250, 250, 250))
        screen.blit(text, (ACCURACY_NAME[0], ACCURACY_NAME[1]))
        font = pg.font.SysFont('agencyfb', 27)
        text = font.render('защита', True, (250, 250, 250))
        screen.blit(text, (DEFENCE_NAME[0], DEFENCE_NAME[1]))
        font = pg.font.SysFont('agencyfb', 27)
        text = font.render('скорость', True, (250, 250, 250))
        screen.blit(text, (SPEED_NAME[0], SPEED_NAME[1]))
        font = pg.font.SysFont('agencyfb', 30)
        text = font.render(f'{self.accuracy}', True, (250, 250, 250))
        screen.blit(text, (ACCURACY_LVL[0], ACCURACY_LVL[1]))
        font = pg.font.SysFont('agencyfb', 30)
        text = font.render(f'{self.defence}', True, (250, 250, 250))
        screen.blit(text, (DEFENCE_LVL[0], DEFENCE_LVL[1]))
        font = pg.font.SysFont('agencyfb', 30)
        text = font.render(f'{self.speed}', True, (250, 250, 250))
        screen.blit(text, (SPEED_LVL[0], SPEED_LVL[1]))
        font = pg.font.SysFont('agencyfb', 40)
        text = font.render(f'{self.exp_count}', True, (250, 250, 250))
        screen.blit(text, (EXP_BANK[0], EXP_BANK[1]))

    def render_pause(self, screen, pause_condition):
        if pause_condition == 0:
            screen.blit(func.load_image(PATHS[184])[0],
                        func.load_image(PATHS[184])[1])
        if pause_condition == 1:
            screen.blit(func.load_image(PATHS[185])[0],
                        func.load_image(PATHS[185])[1])
        if pause_condition == 2:
            screen.blit(func.load_image(PATHS[186])[0],
                        func.load_image(PATHS[186])[1])
        if pause_condition == 3:
            screen.blit(func.load_image(PATHS[187])[0],
                        func.load_image(PATHS[187])[1])
        if pause_condition == 4:
            screen.blit(func.load_image(PATHS[188])[0],
                        func.load_image(PATHS[188])[1])
        if pause_condition == 5:
            screen.blit(func.load_image(PATHS[189])[0],
                        func.load_image(PATHS[189])[1])
        if pause_condition == 6:
            screen.blit(func.load_image(PATHS[190])[0],
                        func.load_image(PATHS[190])[1])
        screen.blit(func.load_pause_slider_way(PAUSE_SLIDER_WAY_POSITION1)[0],
                    func.load_pause_slider_way(PAUSE_SLIDER_WAY_POSITION1)[1])
        screen.blit(func.load_pause_slider_way(PAUSE_SLIDER_WAY_POSITION2)[0],
                    func.load_pause_slider_way(PAUSE_SLIDER_WAY_POSITION2)[1])
        screen.blit(func.load_pause_slider(PAUSE_SLIDER_POSITION1)[0],
                    func.load_pause_slider(PAUSE_SLIDER_POSITION1)[1])
        screen.blit(func.load_pause_slider(PAUSE_SLIDER_POSITION2)[0],
                    func.load_pause_slider(PAUSE_SLIDER_POSITION2)[1])


