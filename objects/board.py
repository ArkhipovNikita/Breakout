import pygame
import random
from helps import Common, width, height
from base_classes import *

class Board(pygame.sprite.Sprite, GameObject):
    """ 
    Class describing behavior of board object
    Class inherits GameObject class

    Attributes:
        step        step of moving by key
    """

    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, filename)
        self.rect.x = width / 2 - self.width / 2
        self.rect.y = height - self.height - 15
        self.step = 20

    def update(self):
        """ 
        Update coordinate of a board
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.right + self.step <= width:
            self.rect.x += self.step
        elif keys[pygame.K_LEFT] and self.left - self.step >= 0 :
            self.rect.x -= self.step
