import pygame
from developers_settings import *


def load_image(img_path):
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.scale(image, (1024, 576))
    image_rect = image.get_rect(topleft=(0, 0))
    return [image, image_rect]


def cut_sheet(sheet, frames, col):
    rect = pygame.Rect(0, 0, 256, 144)
    for i in range(col):
        frame_location = (rect.w * i, 0)
        frames.append(sheet.subsurface(pygame.Rect(
            frame_location, rect.size)))


def load_pause_slider(pos):
    image = pygame.image.load(PATHS[29]).convert_alpha()
    image = pygame.transform.scale(image, (64, 64))
    image_rect = image.get_rect(topleft=pos)
    return [image, image_rect]


def load_pause_slider_way(pos):
    image = pygame.image.load(PATHS[28]).convert_alpha()
    image = pygame.transform.scale(image, (512, 64))
    image_rect = image.get_rect(topleft=pos)
    return [image, image_rect]


def load_hero(img_path, pos):
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.scale(image, (128, 128))
    image_rect = image.get_rect(bottomright=(pos[0], pos[1]))
    return [image, image_rect]


def load_main_hero(img_path, pos):
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.scale(image, (192, 192))
    image_rect = image.get_rect(bottomleft=(pos[0], pos[1]))
    return [image, image_rect]


def load_health_bar(img_path, pos):
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.scale(image, (512, 64))
    image_rect = image.get_rect(topleft=(pos[0], pos[1]))
    return [image, image_rect]


def load_pause_for_levels(img_path, pos):
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.scale(image, (36, 36))
    image_rect = image.get_rect(topleft=(pos[0], pos[1]))
    return [image, image_rect]
