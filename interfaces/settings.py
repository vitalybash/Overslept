import pygame
import sqlite3

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

    def connect_to_db(self):
        """Подключение к базе данных
           Parameter:
           Returns:
        """
        self.con = sqlite3.connect('data/level_of_music.db')
        self.cur = self.con.cursor()

    def get_from_db(self):
        """Получение данных с базы данных
           Parameter:
           Returns volume_of_music: int
        """
        volume_of_melody = self.cur.execute('SELECT value_of_volume '
                                            'FROM music '
                                            'WHERE type = "melody"').fetchone()[
            0]
        return volume_of_melody

    def return_slider_location(self):
        """Получение данных с базы данных
           Parameter:
           Returns x_slider: int
        """
        slider_location = self.get_from_db()
        if slider_location == 0:
            x_slider = 275
        elif slider_location == 0.1:
            x_slider = 315
        elif slider_location == 0.2:
            x_slider = 366
        elif slider_location == 0.3:
            x_slider = 410
        elif slider_location == 0.4:
            x_slider = 460
        elif slider_location == 0.5:
            x_slider = 505
        elif slider_location == 0.6:
            x_slider = 552
        elif slider_location == 0.7:
            x_slider = 600
        elif slider_location == 0.8:
            x_slider = 645
        elif slider_location == 0.9:
            x_slider = 692
        else:
            x_slider = 723
        return x_slider

    def render_settings(self):
        """Установка изображений фона, кнопок и т. п.
           Parameter:
           Returns:
        """
        # установка фона
        self.screen.blit(load_image(PATHS[30])[0],
                         load_image(PATHS[30])[1])
        # установка текста и кнопок, ползунков
        self.font = pygame.font.Font(
            'fonts/comic _sans_ms_pixel_rus_eng.ttf', 40)
        self.font_count = pygame.font.Font(
            'fonts/comic _sans_ms_pixel_rus_eng.ttf', 35)
        self.screen.blit(self.font.render('НАСТРОЙКИ', True,
                                          (250, 250, 250)),
                         (420, 62, 188, 572))
        # установка текста и ползунков, относящихся к музыке
        self.screen.blit(self.font.render('музыка:', True,
                                          (250, 250, 250)),
                         (92, 200, 188, 572))
        music_slider_way = load_setting_image((275, 196), PATHS[28], (512, 64))
        self.screen.blit(music_slider_way[0], music_slider_way[1])
        self.music_slider = load_setting_image(
            (self.return_slider_location(), 204), PATHS[29],
            (64, 64))
        self.screen.blit(self.music_slider[0], self.music_slider[1])
        # установка текста и ползунков, относящихся к звукам
        self.screen.blit(self.font.render('звук:', True,
                                          (250, 250, 250)),
                         (92, 296, 188, 572))
        sound_slider_way = load_setting_image((275, 292), PATHS[28], (512, 64))
        self.screen.blit(sound_slider_way[0], sound_slider_way[1])
        self.sound_slider = load_setting_image((275, 300), PATHS[29],
                                               (64, 64))
        self.screen.blit(self.sound_slider[0], self.sound_slider[1])
        # установка текста и кнопок, относящихся к полноэкранному режиму
        self.screen.blit(self.font.render('полноэкранный режим:', True,
                                          (250, 250, 250)),
                         (92, 392, 188, 572))
        yes_button = load_setting_image((540, 388), PATHS[26], (64, 64))
        self.screen.blit(yes_button[0], yes_button[1])
        self.screen.blit(self.font.render('да', True,
                                          (250, 250, 250)),
                         (620, 392, 188, 572))
        no_button = load_setting_image((700, 388), PATHS[27], (64, 64))
        self.screen.blit(no_button[0], no_button[1])
        self.screen.blit(self.font.render('нет', True,
                                          (250, 250, 250)),
                         (780, 392, 188, 572))

    def text_for_music_slider_way(self):
        """Установка цифр-подсказок снизу дорожки ползунка
           Parameter:
           Returns:
        """
        music_slider_way_y = 250
        music_slider_way_x = 295
        for i in range(2):
            for j in range(10):
                self.screen.blit(self.font_count.render(f'{j}', True,
                                                        (250, 250, 250)),
                                 (
                                     music_slider_way_x, music_slider_way_y,
                                     188,
                                     572))
                j += 1
                music_slider_way_x += 47.1
            self.screen.blit(self.font_count.render('10', True,
                                                    (250, 250, 250)),
                             (
                                 755, music_slider_way_y, 188,
                                 572))
            music_slider_way_y = 347
            music_slider_way_x = 295

    def pinning_the_slider(self):
        """Установка положения ползунка
           Parameter:
           Returns:
        """
        volume_of_music = 0
        which_music = 0
        music_y = 0
        if self.is_changed_music_slider is False:
            if 224 <= self.y <= 231:
                music_y = 204
                which_music = 1
            if 321 <= self.y <= 327:
                music_y = 301
                which_music = 2
            if 295 <= self.x <= 334:
                self.music_slider = load_setting_image((275, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0
            elif 335 <= self.x <= 355:
                self.music_slider = load_setting_image((315, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.1
            elif 356 <= self.x <= 402:
                self.music_slider = load_setting_image((366, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.2
            elif 403 <= self.x <= 447:
                self.music_slider = load_setting_image((410, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.3
            elif 448 <= self.x <= 498:
                self.music_slider = load_setting_image((460, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.4
            elif 499 <= self.x <= 540:
                self.music_slider = load_setting_image((505, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.5
            elif 541 <= self.x <= 585:
                self.music_slider = load_setting_image((552, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.6
            elif 586 <= self.x <= 635:
                self.music_slider = load_setting_image((600, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.7
            elif 631 <= self.x <= 680:
                self.music_slider = load_setting_image((645, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.8
            elif 681 <= self.x <= 735:
                self.music_slider = load_setting_image((692, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 0.9
            else:
                self.music_slider = load_setting_image((723, music_y),
                                                       PATHS[29], (64, 64))
                self.screen.blit(self.music_slider[0],
                                 self.music_slider[1])
                volume_of_music = 1.0
        self.add_to_db(volume_of_music, which_music)

    def add_to_db(self, volume_of_music, which_music):
        """Запись значений в базу данных
           Parameters volume_of_music, which_music: int, int
           Returns:
        """
        self.cur.execute('UPDATE music '
                         f'SET value_of_volume = {volume_of_music} '
                         f'WHERE id = {which_music}')
        self.con.commit()

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
        self.screen = screen
        self.is_changed_music_slider = False
        self.connect_to_db()
        self.render_settings()
        running = True
        while running:
            self.text_for_music_slider_way()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.x, self.y = pygame.mouse.get_pos()
                    if event.button == 1:
                        if 564 <= self.x <= 578 and 411 <= self.y <= 426 or \
                                724 <= self.x <= 739 and 411 <= self.y <= 426:
                            self.button_pressed()
                        elif 295 <= self.x <= 766 and 224 <= self.y <= 231:
                            self.is_changed_music_slider = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.is_changed_music_slider = False
                    if 295 <= self.x <= 766 and 224 <= self.y <= 231:
                        self.pinning_the_slider()
                        music_menu.set_volume(self.get_from_db())
                    elif 295 <= self.x <= 766 and 321 <= self.y <= 327:
                        self.pinning_the_slider()
            pygame.display.flip()
