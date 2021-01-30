from pygame import mixer


class Music:
    """Класс отвечающий за музыку и звуки в игре"""

    def __init__(self, name_music=None):
        """Инициализация музыки
           Parameter name_music: str
           Returns:
        """
        self.melody_or_not = False
        if name_music == 'main_menu_melody.ogg':
            mixer.music.load('music/music_data/main_menu_melody.ogg')
            self.melody_or_not = True
        elif name_music == 'map_melody.ogg':
            mixer.music.load('music/music_data/map_melody.ogg')
            self.melody_or_not = True

    def run(self, name_music=None):
        """Метод, проигрывающий музыку или звук
           Parameter:
           Returns:
        """
        if self.melody_or_not:
            mixer.music.play(-1)
        else:
            self.sound = mixer.Sound(f'music/music_data/{name_music}')
            mixer.Sound.play(self.sound)

    def stop(self):
        """Метод, останавливающий музыку или звук
           Parameter:
           Returns:
        """
        mixer.music.stop()
