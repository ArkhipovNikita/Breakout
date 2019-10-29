import pygame
import random
from helps import Common, width, height
from base_classes import *

class Board(pygame.sprite.Sprite, GameObject, Reflectable):
    """ 
    Class describing behavior of board object
    Class inherits GameObject and Reflectable classes

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
    
    def reflect(self, obj: Movable):
        """ 
        If obj intersects with a side of a board, obj changes velocity 
        depending on how many sides obj intersects

        :param obj: Movable object which will be reflected
        :type obj: Movable
        """
        if self.rect.colliderect(obj.rect):
            edges = Common.find_side_collision(self, obj)
            if len(edges) > 1:
                obj.velocity.y = -obj.velocity.y
                obj.velocity.x = -obj.velocity.x
            elif len(edges) == 1:
                if edges[0] in ('top', 'bottom'):
                    obj.velocity.y = -obj.velocity.y
                    obj.velocity.x = random.randint(-obj.speed, obj.speed)
                else:
                    obj.velocity.x = random.randint(-obj.speed, obj.speed)
