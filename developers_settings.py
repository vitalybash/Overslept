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
