from pygame.mixer import Sound


class Music:
    """Класс отвечающий за музыку и звуки в игре"""

    def __init__(self):
        self.play_music = Sound('music/music_data/main_menu_melody.ogg')

    def run(self, name_music):
        """Метод, проигрывающий музыку"""
        self.play_music.play()

    def stop(self):
        self.play_music.stop()
