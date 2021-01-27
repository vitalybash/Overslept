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
        font = pygame.font.Font(
            'fonts/comic _sans_ms_pixel_rus_eng.ttf', 40)
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

    def return_music_volume(self, x, y, music):
        """Установка ползунка на дорожке
           Parameters x, y: int, int
           Returns:
        """
        if 220 < y < 230:
            if 305 <= x <= 349.8:
                music.set_volume(0.1)
            elif 349.9 <= x <= 394.7:
                music.set_volume(0.2)
            elif 394.8 <= x <= 439.6:
                music.set_volume(0.3)
            elif 439.7 <= x <= 484.5:
                music.set_volume(0.4)
            elif 484.6 <= x <= 529.4:
                music.set_volume(0.5)
            elif 529.5 <= x <= 574.3:
                music.set_volume(0.6)
            elif 574.4 <= x <= 619.2:
                music.set_volume(0.7)
            elif 619.3 <= x <= 664.1:
                music.set_volume(0.8)
            elif 664.2 <= x <= 709:
                music.set_volume(0.9)
            else:
                music.set_volume(1)

    def global_values(self):
        """Возвращает глобальные вспомогательные переменные
           Parameters:
           Returns volume: int
        """
        volume = self
        return volume

    def button_pressed(self):
        """Если кнопка нажата, то меняет картинку
           Parameter:
           Returns:
        """
        yes_button = load_setting_image((540, 388), PATHS[27], (64, 64))
        self.screen.blit(yes_button[0], yes_button[1])
        no_button = load_setting_image((700, 388), PATHS[26], (64, 64))
        self.screen.blit(no_button[0], no_button[1])

    def run(self, screen, music_menu):
        """Открытие настроек
           Parameter screen: surface
           Returns:
        """
        music_menu.run()
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
                            self.return_music_volume(x, y, music_menu)
                            music_menu.stop()
                            music_menu.run()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.held = False
                    x, y = pygame.mouse.get_pos()
                    if not (564 <= x <= 578 and 411 <= y <= 426 or
                            724 <= x <= 739 and 411 <= y <= 426):
                        self.render_settings(1)
                        self.pinning_the_slider(x, y)
            pygame.display.flip()
