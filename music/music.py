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
        elif name_music == 'level_melody.ogg':
            pygame.mixer.music.load('music/music_data/level_melody.ogg')

    def run(self):
        """Метод, проигрывающий музыку или звук
           Parameter:
           Returns:
        """
        pygame.mixer.music.play(-1)

    def set_volume(self, volume_of_music):
        """Метод, проигрывающий музыку или звук
           Parameter volume_of_music: int
           Returns:
        """
        pygame.mixer.music.set_volume(volume_of_music)

    def stop(self):
        """Метод, останавливающий музыку или звук
           Parameter:
           Returns:
        """
        pygame.mixer.music.stop()
