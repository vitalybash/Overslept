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
LEVEL_NAMES_BASIC_FRAMES = [47, 54, 63, 70, 77, 83, 91, 98]
ACTION_BUTTONS_FRAMES = [48, 49, 55, 56, 64, 65, 71, 72,
                         78, 79, 84, 85, 93, 92, 98, 100]
ACTION_WAY_FRAMES = [105, 113, 120, 128, 136, 144, 152, 160]
