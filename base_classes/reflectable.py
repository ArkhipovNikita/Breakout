import pygame
from base_classes.movable import Movable
from abc import ABCMeta, abstractmethod, abstractproperty

class Reflectable:
    """
    Abstract class describing objects which must reflect movable objects
    """
    __metaclass__=ABCMeta

    @abstractmethod
    def reflect(obj: Movable):
        """ 
        Change the velocity of movable object 

        :param obj: movable game object

        :return: not return
        """