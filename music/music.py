import pygame


class Music:
    def run(self, name_music):
        if name_music == 1:
            pygame.mixer.music.load('main_menu_melody.wav')
            pygame.mixer.music.play(-1)
