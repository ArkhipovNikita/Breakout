import pygame
from base_classes.game_object import GameObject


class Brick(pygame.sprite.Sprite, GameObject):
    """
    Brick class - one unit to destroy
    Class inherits GameObject class
    """
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, filename)
        self.rect = pygame.Rect(x, y, self.width, self.height)