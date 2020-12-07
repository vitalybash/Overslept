import pygame
from developers_settings import *
from basic_functions import load_image


class HubMenu:
    def __init__(self, lvl_id=0):
        self.running, self.is_triggered = True, True
        self.available_lvl = lvl_id

    def render(self, screen):
        screen.blit(load_image(PATHS[12])[0], load_image(PATHS[12])[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pygame.display.flip()
        return self.running, self.is_triggered
