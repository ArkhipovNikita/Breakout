import pygame
from base_classes import GameObject
from helps.sides import Sides

class Common:
    # Скорее всего будет класс Game, в который перенесу общие для игры методы и свойства
    """
    Class containing common methods and properties
    """

    @staticmethod
    def find_side_collision(obj1: GameObject, obj2: GameObject):
        """
        Find all sides of obj2 which obj1 intersects

        :param obj1: game object for which method find intersected sides by obj2
        :type obj1: GameObject
        :param obj2: game object whose sides intersections the method is looking for
        :type obj2: GameObject

        :return: list of intersecting sides
        """
        edges = {Sides.Left : pygame.Rect(obj1.left, obj1.top, 1, obj1.height),
                Sides.Right : pygame.Rect(obj1.right, obj1.top, 1, obj1.height),
                Sides.Top : pygame.Rect(obj1.left, obj1.top, obj1.width, 1),
                Sides.Bottom : pygame.Rect(obj1.left, obj1.bottom, obj1.width, 1)}
        collisions = [edge for edge, rect in edges.items() if obj2.rect.colliderect(rect)]
        if len(collisions) > 1:
            if obj1.left <= obj2.center[0] and obj2.center[0] <= obj1.right:
                return [e for e in collisions if e in (Sides.Top, Sides.Bottom)]
            if obj1.top <= obj2.center[1] and obj2.center[1] <= obj1.bottom:
                return [e for e in collisions if e in (Sides.Left, Sides.Right)]
        return collisions