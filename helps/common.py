import pygame
from base_classes import GameObject

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
        edges = dict(left=pygame.Rect(obj1.left, obj1.top, 1, obj1.height),
                    right=pygame.Rect(obj1.right, obj1.top, 1, obj1.height),
                    top=pygame.Rect(obj1.left, obj1.top, obj1.width, 1),
                    bottom=pygame.Rect(obj1.left, obj1.bottom, obj1.width, 1))
        collisions = [edge for edge, rect in edges.items() if obj2.rect.colliderect(rect)]
        return collisions