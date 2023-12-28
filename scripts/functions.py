import pygame
import os

def load_image(*path):
    path = os.path.join(*path)
    image = pygame.image.load(path).convert()
    image.set_colorkey((0,0,0))

    return image