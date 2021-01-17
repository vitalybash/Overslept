import sys

import pygame

from basic_functions import load_image
from developers_settings import *


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
        screen.blit(font.render('музыка:', True,
                                (250, 250, 250)), (92, 200, 188, 572))
        pygame.image.load('graphics/main_menu/settings/slider_way.png')
        screen.blit(font.render('звук:', True,
                                (250, 250, 250)), (92, 296, 188, 572))
        screen.blit(font.render('полноэкранный режим:', True,
                                (250, 250, 250)), (92, 392, 188, 572))

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
                    running = False
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
