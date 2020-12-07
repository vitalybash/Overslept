import pygame

from developers_settings import *
from interfaces.main_menu import MainMenu


def load_image(img_path):
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.scale(image, (1024, 576))
    image_rect = image.get_rect(topleft=(0, 0))
    return [image, image_rect]


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('OverSlept')
    screen = pygame.display.set_mode(SIZE)
    screen.fill((0, 0, 0))

    # Экземпляр
    MAIN_WND = MainMenu()
    running = True
    while running:
        running = MAIN_WND.render(screen)
    pygame.quit()

