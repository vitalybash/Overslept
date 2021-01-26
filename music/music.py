from pygame import mixer


class Music:
    """Класс отвечающий за музыку и звуки в игре"""

    def __init__(self, name_music):
        """Инициализация музыки
           Parameter name_music: str
           Returns:
        """
        if name_music == 'main_menu_melody.ogg':
            mixer.music.load('music/music_data/main_menu_melody.ogg')
        elif name_music == 'map_melody.ogg':
            mixer.music.load('music/music_data/map_melody.ogg')

    def run(self):
        """Метод, проигрывающий музыку или звук
           Parameter:
           Returns:
        """
        mixer.music.play(-1)

    def stop(self):
        """Метод, останавливающий музыку или звук
           Parameter:
           Returns:
        """
        mixer.music.stop()
