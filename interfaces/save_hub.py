import data.userCore as uC
import pygame
import sys

from basic_functions import load_image
from developers_settings import *


class SaveHub:
    def __init__(self):
        self.cell = -1
        self.saves = uC.listSaves

    def render_saves(self):
        for save in self.saves:
            pass

    def run(self, screen):
        running = True
        while running:
            screen.blit(load_image(PATHS[14])[0], load_image(PATHS[14])[1])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    # Обработчик клавиш
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 50 <= mouse_x <= 974 and 50 <= mouse_y <= 110:
                        self.cell = 1
                    elif 50 <= mouse_x <= 974 and 113 <= mouse_y <= 173:
                        self.cell = 2
                    elif 50 <= mouse_x <= 974 and 176 <= mouse_y <= 236:
                        self.cell = 3
                    elif 50 <= mouse_x <= 974 and 239 <= mouse_y <= 299:
                        self.cell = 4
                    elif 50 <= mouse_x <= 974 and 302 <= mouse_y <= 362:
                        self.cell = 5
                    elif 50 <= mouse_x <= 974 and 365 <= mouse_y <= 425:
                        self.cell = 6
                    elif 50 <= mouse_x <= 974 and 428 <= mouse_y <= 488:
                        self.cell = 7
                    else:
                        self.cell = -1

            # Наведение мышью на одну из ячеек сохранения
            if self.cell == -1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 50 <= mouse_x <= 974 and 50 <= mouse_y <= 110:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     SAVE_PROFILE_1, 3)
                elif 50 <= mouse_x <= 974 and 113 <= mouse_y <= 173:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     SAVE_PROFILE_2, 3)
                elif 50 <= mouse_x <= 974 and 176 <= mouse_y <= 236:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     SAVE_PROFILE_3, 3)
                elif 50 <= mouse_x <= 974 and 239 <= mouse_y <= 299:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     SAVE_PROFILE_4, 3)
                elif 50 <= mouse_x <= 974 and 302 <= mouse_y <= 362:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     SAVE_PROFILE_5, 3)
                elif 50 <= mouse_x <= 974 and 365 <= mouse_y <= 425:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     SAVE_PROFILE_6, 3)
                elif 50 <= mouse_x <= 974 and 428 <= mouse_y <= 488:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     SAVE_PROFILE_7, 3)
            # выделение выбранной ячейки
            elif self.cell == 1:
                pygame.draw.rect(screen, pygame.Color('white'),
                                 SAVE_PROFILE_1, 3)
            elif self.cell == 2:
                pygame.draw.rect(screen, pygame.Color('white'),
                                 SAVE_PROFILE_2, 3)
            elif self.cell == 3:
                pygame.draw.rect(screen, pygame.Color('white'),
                                 SAVE_PROFILE_3, 3)
            elif self.cell == 4:
                pygame.draw.rect(screen, pygame.Color('white'),
                                 SAVE_PROFILE_4, 3)
            elif self.cell == 5:
                pygame.draw.rect(screen, pygame.Color('white'),
                                 SAVE_PROFILE_5, 3)
            elif self.cell == 6:
                pygame.draw.rect(screen, pygame.Color('white'),
                                 SAVE_PROFILE_6, 3)
            elif self.cell == 7:
                pygame.draw.rect(screen, pygame.Color('white'),
                                 SAVE_PROFILE_7, 3)

            pygame.display.flip()
