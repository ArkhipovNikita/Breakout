import pygame
from abc import ABCMeta, abstractmethod, abstractproperty


class GameObject:
    """
    Abstract class determining base properties and methods of objects in the game    

    Attributes:
        image       path to image file
        rect        rectangle containing bounds and position of an object
    """
    __metaclass__=ABCMeta
    
    @abstractmethod
    def __init__(self, file_path):
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect()

    @abstractproperty
    def width(self):
        """ width of object """
        return self.image.get_width()

    @abstractproperty
    def height(self):
        """ height of object """
        return self.image.get_height()

    @abstractproperty
    def top(self):
        """ top bound of object """
        return self.rect.top

    @abstractproperty
    def bottom(self):
        """ bottom bound of object """
        return self.rect.bottom

    @abstractproperty
    def right(self):
        """ right bound of object """
        return self.rect.right

    @abstractproperty
    def left(self):
        """ left bound of object """
        return self.rect.left
        
    @abstractmethod
    def draw(self, screen):
        """ 
        Draw object on the screen 

        :param screen: the main screen of the game
        :type screen: Surface

        :return: not return
        """
        screen.blit(self.image, self.rect)
