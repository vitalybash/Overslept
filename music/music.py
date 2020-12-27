import os.path

import pygame
from pygame.mixer import Sound


class Music:
    """Класс отвечающий за музыку и звуки в игре"""

    def run(self, name_music):
        """Метод, проигрывающий музыку"""
        # может быть в инициализации проблема...
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        # внизу должно быть просто через mixer,
        # но через Sound хотя бы нормальные звуки слышны
        filepath = os.path.dirname(__file__)
        music = Sound(os.path.join(filepath, 'main_menu_melody.ogg'))
        music.play(-1)
        if name_music == 0:
            music.stop()
