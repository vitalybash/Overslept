import pygame


class Music:
    """Класс отвечающий за музыку и звуки в игре"""

    def run(self, name_music):
        """Метод, проигрывающий музыку"""
        pygame.mixer.init()
        pygame.mixer.music.load(name_music)
        pygame.mixer.music.play(-1)
        if name_music == 0:
            pygame.mixer.music.stop()
