import csv

#  файл для констант и прочих ништяков которые
#  не хотелось бы задавать в main.py

SIZE = WIDTH, HEIGHT = 1024, 576

with open('graphics_paths.csv', mode='r', encoding='utf-8') as in_file:
    reader = csv.reader(in_file, delimiter=';')
    PATHS = [path for number, path in reader]
    #  распаковка содержащихся в csv файле путей к кадрам графики

MAIN_MENU_PLAY = [256, 208, 764, 276]
MAIN_MENU_SAVE = [256, 296, 764, 364]
MAIN_MENU_SETTINGS = [256, 384, 764, 452]
MAIN_MENU_QUIT = [256, 472, 764, 540]
#  координаты начал и концов кнопок главного меню
MAIN_MENU_BUTTONS_COORDINATES = [MAIN_MENU_PLAY,
                                 MAIN_MENU_SAVE,
                                 MAIN_MENU_SETTINGS,
                                 MAIN_MENU_QUIT]

PIONER_LEVEL_PLAY = [412, 80, 508, 96]
KREST_LEVEL_PLAY = [372, 148, 452, 164]
KNIJNIY_LEVEL_PLAY = [492, 168, 604, 184]
SPORT_LEVEL_PLAY = [360, 224, 440, 240]
MOIKA_LEVEL_PLAY = [416, 288, 496, 304]
SPAS_LEVEL_PLAY = [532, 284, 596, 300]
FRUNZE_LEVEL_PLAY = [512, 368, 608, 384]
VRATA_LEVEL_PLAY = [512, 436, 592, 452]
#  координаты начал и концов кнопок levelhub'а
LEVEL_HUB_BUTTONS_COORDINATES = [PIONER_LEVEL_PLAY,
                                 KREST_LEVEL_PLAY,
                                 KNIJNIY_LEVEL_PLAY,
                                 SPORT_LEVEL_PLAY,
                                 MOIKA_LEVEL_PLAY,
                                 SPAS_LEVEL_PLAY,
                                 FRUNZE_LEVEL_PLAY,
                                 VRATA_LEVEL_PLAY]
#  кадры обычных состояний названий уровней
LEVEL_NAMES_BASIC_FRAMES = [47, 54, 63, 70, 77, 83, 91, 98]
#  кадры активированных путей и названий уровней
ACTION_BUTTONS_FRAMES = [48, 49, 55, 56, 64, 65, 71, 72,
                         78, 79, 84, 85, 93, 92, 98, 100]
ACTION_WAY_FRAMES = [105, 113, 120, 128, 136, 144, 152, 160]
#  координаты значений здоровья и денег
HEALTH_PLACE = [528, 4]
MONEY_PLACE = [840, 8]
#  координаты кнопки паузы
PAUSE_BUTTON_COORDINATES = [992, 4, 1016, 28]
#  координаты объектов магазинов
GUN_MAGAZINE = [92, 392, 188, 572]
FOOD_MAGAZINE = [100, 100, 228, 308]
SKILLS_MAGAZINE = [728, 176, 1020, 508]
#  координаты кнопок в меню паузы
PAUSE_PLAY_BUTTON = [416, 164, 604, 196]
PAUSE_SAVE_BUTTON = [416, 216, 604, 248]
PAUSE_EXIT_BUTTON = [416, 384, 604, 416]
PAUSE_SLIDER_POSITION1 = (704, 328)
PAUSE_SLIDER_POSITION2 = (704, 256)
PAUSE_SLIDER_WAY_POSITION1 = (256, 248)
PAUSE_SLIDER_WAY_POSITION2 = (256, 320)

#  координаты кнопок в меню сохранения
SAVE_PROFILE_1 = (50, 50, 924, 60)
SAVE_PROFILE_2 = (50, 114, 924, 60)
SAVE_PROFILE_3 = (50, 178, 924, 60)
SAVE_PROFILE_4 = (50, 242, 924, 60)
SAVE_PROFILE_5 = (50, 306, 924, 60)
SAVE_PROFILE_6 = (50, 370, 924, 60)
SAVE_PROFILE_7 = (50, 434, 924, 60)

#  координаты надписей в магазине навыков
ACCURACY_NAME = [608, 288]
DEFENCE_NAME = [724, 288]
SPEED_NAME = [848, 288]
EXP_BANK = [900, 212]
ACCURACY_LVL = [608, 252]
DEFENCE_LVL = [724, 252]
SPEED_LVL = [848, 252]
SHOP_WND_POSITION = [576, 192, 956, 444]
ACCURACY_PLACE = [596, 276, 696, 424]
DEFENCE_PLACE = [712, 276, 820, 424]
SPEED_PLACE = [836, 276, 936, 424]