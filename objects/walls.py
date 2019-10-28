import pygame
from helps import width
from base_classes import Reflectable, Movable

class Walls(Reflectable):
    """ 
    Class describes 'virtual' wall object from which a movable object can be reflected
    Class inherits Reflectable class
    """
    def reflect(self, obj: Movable):
        """ 
        If obj intersects with walls apart from bottom wall, velocity of obj will change 

        :param obj; movable object
        :type obj: Movable
        """
        if obj.left <= 0 or obj.right >= width:
            obj.velocity.x = -obj.velocity.x
        if obj.top <= 0:
           obj.velocity.y = -obj.velocity.y