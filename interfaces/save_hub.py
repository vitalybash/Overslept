import pygame
import sys

from data.userCore import listSaves
from developers_settings import PATHS
from basic_functions import load_image


class SaveHub:
    def __init__(self):
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

                if event.type == pygame.MOUSEMOTION:
                    pass

            pygame.display.flip()
