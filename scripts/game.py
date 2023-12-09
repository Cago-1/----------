import pygame
import os

class Game():
    def __init__(self) -> None:
        self.background_image = pygame.image.load(os.path.join('assets','icons','icon.ico'))  

    def render(self,surface: pygame.Surface):
        surface.blit(self.background_image,(0,0))
