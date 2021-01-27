import pygame
from interfaces.settings import Settings


class Music:
    """Класс отвечающий за музыку и звуки в игре"""

    def __init__(self, name_music):
        """Инициализация музыки
           Parameter name_music: str
           Returns:
        """
        if name_music == 'main_menu_melody.ogg':
            pygame.mixer.music.load('music/music_data/main_menu_melody.ogg')
        elif name_music == 'map_melody.ogg':
            pygame.mixer.music.load('music/music_data/map_melody.ogg')
        self.count = 0
        self.volume_pin = 0

    def run(self):
        """Метод, проигрывающий музыку или звук
           Parameter:
           Returns:
        """
        pygame.mixer.music.play(-1)

    def set_volume(self, value):
        pygame.mixer.music.set_volume(value)

    def get_volume(self):
        pygame.mixer.music.get_volume()

    def stop(self):
        """Метод, останавливающий музыку или звук
           Parameter:
           Returns:
        """
        pygame.mixer.music.stop()
