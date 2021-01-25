import pygame

from basic_functions import load_image
from developers_settings import *


def load_setting_image(pos, link, size):
    """Функция, отвечающая за передачу картинок
       Parameters pos, link, size: tuple, str, tuple
       Returns [image, image_rect]: list
    """
    image = pygame.image.load(link).convert_alpha()
    image = pygame.transform.scale(image, size)
    image_rect = image.get_rect(topleft=pos)
    return [image, image_rect]


class Settings:
    """Класс, отвечающий за настройки(громкость музыки, звуков;
    разрешение окна"""

    def render_settings(self, flag):
        """Установка изображений фона, кнопок и т. п.
           Parameter flag: int
           Returns:
        """
        # установка фона
        self.screen.blit(load_image(PATHS[30])[0],
                         load_image(PATHS[30])[1])
        # установка текста и кнопок, ползунков
        font = pygame.font.SysFont('impact', 40)
        self.screen.blit(font.render('НАСТРОЙКИ', True,
                                     (250, 250, 250)), (420, 62, 188, 572))
        # установка текста и ползунков, относящихся к музыке
        self.screen.blit(font.render('музыка:', True,
                                     (250, 250, 250)), (92, 200, 188, 572))
        music_slider_way = load_setting_image((275, 196), PATHS[28], (512, 64))
        self.screen.blit(music_slider_way[0], music_slider_way[1])
        # если flag = 0, то начальное расположение позунка,
        # если flag = 1, то конечное
        if not flag:
            self.music_slider = load_setting_image((275, 204), PATHS[29],
                                                   (64, 64))
            self.screen.blit(self.music_slider[0], self.music_slider[1])
        # установка текста и ползунков, относящихся к звукам
        self.screen.blit(font.render('звук:', True,
                                     (250, 250, 250)), (92, 296, 188, 572))
        sound_slider_way = load_setting_image((275, 292), PATHS[28], (512, 64))
        self.screen.blit(sound_slider_way[0], sound_slider_way[1])
        sound_slider = load_setting_image((275, 300), PATHS[29], (64, 64))
        self.screen.blit(sound_slider[0], sound_slider[1])
        # установка текста и кнопок, относящихся к полноэкранному режиму
        self.screen.blit(font.render('полноэкранный режим:', True,
                                     (250, 250, 250)), (92, 392, 188, 572))
        yes_button = load_setting_image((540, 388), PATHS[26], (64, 64))
        self.screen.blit(yes_button[0], yes_button[1])
        self.screen.blit(font.render('да', True,
                                     (250, 250, 250)), (620, 392, 188, 572))
        no_button = load_setting_image((700, 388), PATHS[27], (64, 64))
        self.screen.blit(no_button[0], no_button[1])
        self.screen.blit(font.render('нет', True,
                                     (250, 250, 250)), (780, 392, 188, 572))

    def holding(self):
        """Перетаскивание ползунка
           Parameter:
           Returns:
        """
        if self.held:
            x, y = pygame.mouse.get_pos()
            if 305 <= x <= 753 and 220 < y < 230:
                self.music_slider = load_setting_image((x - 30, y - 20),
                                                       PATHS[29],
                                                       (64, 64))
                self.screen.blit(self.music_slider[0], self.music_slider[1])
            else:
                self.music_slider = load_setting_image((275, 204), PATHS[29],
                                                       (64, 64))
                self.screen.blit(self.music_slider[0], self.music_slider[1])
                self.render_settings(1)

    def pinning_the_slider(self, x, y):
        """Установка ползунка на дорожке
           Parameters x, y: int, int
           Returns:
        """
        if self.held is False:
            if 305 <= x <= 753 and 220 < y < 230:
                self.music_slider = load_setting_image((x - 30, y - 20),
                                                       PATHS[29],
                                                       (64, 64))
                self.screen.blit(self.music_slider[0], self.music_slider[1])

    def return_music_volume(self, x, y):
        """Установка ползунка на дорожке
           Parameters x, y: int, int
           Returns music_volume: int
        """
        if 220 < y < 230:
            pass

    def button_pressed(self):
        """Если кнопка нажата, то меняет картинку
           Parameter:
           Returns:
        """
        yes_button = load_setting_image((540, 388), PATHS[27], (64, 64))
        self.screen.blit(yes_button[0], yes_button[1])
        no_button = load_setting_image((700, 388), PATHS[26], (64, 64))
        self.screen.blit(no_button[0], no_button[1])

    def run(self, screen):
        """Открытие настроек
           Parameter screen: surface
           Returns:
        """
        self.screen = screen
        self.held = False
        self.render_settings(0)
        running = True
        while running:
            if self.held:
                self.holding()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    if event.button == 1:
                        if 564 <= x <= 578 and 411 <= y <= 426 or \
                                724 <= x <= 739 and 411 <= y <= 426:
                            self.button_pressed()
                        else:
                            self.held = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.held = False
                    x, y = pygame.mouse.get_pos()
                    if 565 <= x <= 577 and 413 <= y <= 421:
                        self.button_pressed()
                    else:
                        self.render_settings(1)
                        self.pinning_the_slider(x, y)
            pygame.display.flip()
