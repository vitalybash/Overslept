import pygame

from developers_settings import *
from interfaces.main_menu import MainMenu


def load_image(img_path):
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.scale(image, (1024, 576))
    image_rect = image.get_rect(topleft=(0, 0))
    return [image, image_rect]


if __name__ == '__main__':
    pygame.mixer.init()
    pygame.init()
    FPS = 60
    clock = pygame.time.Clock()
    pygame.display.set_caption('OverSlept')
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_icon(load_image(PATHS[12])[0])
    screen.fill((0, 0, 0))
    clock.tick(FPS)

    MainMenu().run(screen)
