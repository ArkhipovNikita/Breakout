import pygame
from objects.game_object import GameObject


class Brick(pygame.sprite.Sprite, GameObject):
    """
    Break class - one unit to destroy
    rect[x, y]    coordinates
    """
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, filename)
        self.rect = [x, y]