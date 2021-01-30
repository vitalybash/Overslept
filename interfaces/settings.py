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

    def render_settings(self, flag, flag_sound):
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
        if not flag_sound:
            self.sound_slider = load_setting_image((275, 300), PATHS[29],
                                                   (64, 64))
            self.screen.blit(self.sound_slider[0], self.sound_slider[1])
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

    def pinning_the_slider(self):
        """Установка положения ползунка
           Parameter:
           Returns:
        """
        music_y = 0
        if self.is_changed_music_slider is False:
            if 224 <= self.y <= 231:
                music_y = 204
            if 321 <= self.y <= 327:
                music_y = 301
            if 295 <= self.x <= 342.1:
                self.music_slider = load_setting_image((322.1, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            elif 342.2 <= self.x <= 389.3:
                self.music_slider = load_setting_image((369.3, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            elif 389.4 <= self.x <= 436.5:
                self.music_slider = load_setting_image((416.5, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            elif 436.6 <= self.x <= 483.7:
                self.music_slider = load_setting_image((463.7, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            elif 483.8 <= self.x <= 530.9:
                self.music_slider = load_setting_image((510.9, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            elif 531 <= self.x <= 578.1:
                self.music_slider = load_setting_image((558.1, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            elif 578.2 <= self.x <= 625.3:
                self.music_slider = load_setting_image((605.3, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            elif 625.4 <= self.x <= 672.5:
                self.music_slider = load_setting_image((652.5, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            elif 672.6 <= self.x <= 719.7:
                self.music_slider = load_setting_image((699.7, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
            else:
                self.music_slider = load_setting_image((723, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])

    def button_pressed(self):
        """Если кнопка нажата, то меняет картинку
           Parameter:
           Returns:
        """
        if 564 <= self.x <= 578 and 411 <= self.y <= 426:
            yes_button = load_setting_image((540, 388), PATHS[27], (64, 64))
            self.screen.blit(yes_button[0], yes_button[1])
            no_button = load_setting_image((700, 388), PATHS[26], (64, 64))
            self.screen.blit(no_button[0], no_button[1])
        else:
            yes_button = load_setting_image((540, 388), PATHS[26], (64, 64))
            self.screen.blit(yes_button[0], yes_button[1])
            no_button = load_setting_image((700, 388), PATHS[27], (64, 64))
            self.screen.blit(no_button[0], no_button[1])

    def run(self, screen, music_menu):
        """Открытие настроек
           Parameter screen, music_menu: surface, Music
           Returns:
        """
        self.music_menu = music_menu
        self.music_menu.run()
        self.screen = screen
        self.is_changed_music_slider = False
        self.render_settings(0, 0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.x, self.y = pygame.mouse.get_pos()
                    print(self.x, self.y)
                    if event.button == 1:
                        if 564 <= self.x <= 578 and 411 <= self.y <= 426 or \
                                724 <= self.x <= 739 and 411 <= self.y <= 426:
                            self.button_pressed()
                        elif 295 <= self.x <= 766 and 224 <= self.y <= 231:
                            self.is_changed_music_slider = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.is_changed_music_slider = False
                    if 295 <= self.x <= 766 and 224 <= self.y <= 231:
                        self.render_settings(1, 0)
                        self.pinning_the_slider()
                    elif 295 <= self.x <= 766 and 321 <= self.y <= 327:
                        self.render_settings(0, 1)
                        self.pinning_the_slider()
            pygame.display.flip()
