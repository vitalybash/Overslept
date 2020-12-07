import pygame

from developers_settings import *
from interfaces.main_menu import MainMenu
from interfaces.hub_menu import HubMenu


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

    # Экземпляры канвасов
    # Главное меню
    MAIN_WND = MainMenu()
    main_triggered = True

    # Level Hub
    HUB_WND = HubMenu()
    hub_triggered = False

    running = True
    while running:
        if main_triggered:
            running, main_triggered, button = MAIN_WND.render(screen)
            print(main_triggered, button)
            if button == 0 and not main_triggered:
                hub_triggered = True
        elif hub_triggered:
            running, hub_triggered = HUB_WND.render(screen)


