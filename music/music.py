from os.path import dirname, join

import pygame, time
from pygame.mixer import Sound


class Music:
    """Класс отвечающий за музыку и звуки в игре"""

    def __init__(self):
        filepath = dirname(__file__)
        self.play_music = Sound(join(filepath, 'main_menu_melody.ogg'))

    def run(self, name_music):
        """Метод, проигрывающий музыку"""
        pygame.mixer.init()
        Sound.play(self.play_music)
        time.sleep(183)

    def stop(self):
        Sound.stop(self.play_music)
