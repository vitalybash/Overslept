import pygame


class Music:
    """Класс отвечающий за музыку и звуки в игре"""

    def __init__(self, music_name=None):
        """Инициализация музыки
           Parameter name_music: str
           Returns:
        """
        if music_name == 'main_menu_melody.ogg':
            pygame.mixer.music.load('music/music_data/main_menu_melody.ogg')
        elif music_name == 'map_melody.ogg':
            pygame.mixer.music.load('music/music_data/map_melody.ogg')

    def run(self):
        """Метод, проигрывающий музыку
           Parameter:
           Returns:
        """
        pygame.mixer.music.play(-1)

    def play(self, sound_name):
        """Метод, проигрывающий звук
           Parameter sound_name: str
           Returns:
        """
        sound = pygame.mixer.Sound(f'music/music_data/{sound_name}')
        pygame.mixer.Sound.play(sound)

    def stop(self):
        """Метод, останавливающий музыку или звук
           Parameter:
           Returns:
        """
        pygame.mixer.music.stop()
