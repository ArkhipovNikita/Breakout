import pygame
from helps.vector2d import Vector2D
from abc import ABCMeta, abstractmethod, abstractproperty

class Movable:
    """
    Abstract Class describing movable objects

    Attributes:
        speed       speed/step of moving
        velocity    direction of moving (vector)
    """
    __metaclass__=ABCMeta

    @abstractmethod
    def __init__(self, speed):
        self.speed = speed
        self.velocity = Vector2D(0, 0)