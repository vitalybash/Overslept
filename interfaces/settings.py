import sys

import pygame

from basic_functions import load_image
from developers_settings import *


def load_setting_image(pos, link, size):
    """Установка фона
       Parameter pos, link, size: tuple, str, tuple
       Returns [image, image_rect]: list
    """
    image = pygame.image.load(link).convert_alpha()
    image = pygame.transform.scale(image, size)
    image_rect = image.get_rect(topleft=pos)
    return [image, image_rect]


class Settings:
    """Класс отвечающий за настройки(громкость музыки, звуков;
    разрешение окна"""

    def render_settings(self, screen):
        """Установка фона
           Parameter screen: surface
           Returns:
        """
        # установка фона
        screen.blit(load_image(PATHS[30])[0],
                    load_image(PATHS[30])[1])
        # установка текста и кнопок, ползунков
        font = pygame.font.SysFont('impact', 40)
        screen.blit(font.render('НАСТРОЙКИ', True,
                                (250, 250, 250)), (420, 62, 188, 572))
        # установка текста и ползунков, относящихся к музыке
        screen.blit(font.render('музыка:', True,
                                (250, 250, 250)), (92, 200, 188, 572))
        music_slider_way = load_setting_image((275, 196), PATHS[28], (512, 64))
        screen.blit(music_slider_way[0], music_slider_way[1])
        music_slider = load_setting_image((275, 204), PATHS[29], (64, 64))
        screen.blit(music_slider[0], music_slider[1])
        # установка текста и ползунков, относящихся к звукам
        screen.blit(font.render('звук:', True,
                                (250, 250, 250)), (92, 296, 188, 572))
        sound_slider_way = load_setting_image((275, 292), PATHS[28], (512, 64))
        screen.blit(sound_slider_way[0], sound_slider_way[1])
        sound_slider = load_setting_image((275, 300), PATHS[29], (64, 64))
        screen.blit(sound_slider[0], sound_slider[1])
        # установка текста и кнопок, относящихся к полноэкранному режиму
        screen.blit(font.render('полноэкранный режим:', True,
                                (250, 250, 250)), (92, 392, 188, 572))
        yes_button = load_setting_image((540, 388), PATHS[26], (64, 64))
        screen.blit(yes_button[0], yes_button[1])
        screen.blit(font.render('да', True,
                                (250, 250, 250)), (620, 392, 188, 572))
        yes_button = load_setting_image((700, 388), PATHS[26], (64, 64))
        screen.blit(yes_button[0], yes_button[1])
        screen.blit(font.render('нет', True,
                                (250, 250, 250)), (780, 392, 188, 572))

    def run(self, screen):
        """Открытие настроек
           Parameter screen: surface
           Returns:
        """
        running = True
        while running:
            self.render_settings(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.flip()
