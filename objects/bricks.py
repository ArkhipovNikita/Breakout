import pygame
import random
import os
from helps import Common, line_limit, brick_size
from objects.brick import Brick
from base_classes import Movable, Reflectable, GameObject

pygame.mixer.init()


class Bricks(Reflectable):
    """
    Class containing bricks
    Class inherits Reflectable class

    Attributes:
          bricks       list of bricks
          path         path to dir with images
          images       list of images from path
          start point  start point of generation
    """
    
    def __init__(self, path):
        self.bricks = pygame.sprite.Group()
        self.start_point = 25
        self.path = path
        self.images = os.listdir(self.path)
        self.destroy_sound = pygame.mixer.Sound('assets/sound/destroy_brick.wav')

    def __find_bricks(self, obj: GameObject):
        """
        Find all bricks that are intersected by obj
        Play sound effect if obj intersects a brick

        :param obj: the game object which may intersect the bricks
        :type obj: GameObject

        :return: list of intersected bricks
        """
        ball = pygame.sprite.Group()
        ball.add(obj)
        res = pygame.sprite.groupcollide(self.bricks, ball, True, False)
        for i in range(len(res)):   self.destroy_sound.play()
        return [key for key, val in res.items()]
    
    # может где-то есть ошибка, поэтому появлются баги типа удаления кирпича без отражения
    # или проход сквозь кирпич через угол
    def reflect(self, obj: Movable):
        """
        Change velocity of a obj if it intersects bricks
        Type of chanhing velocity depends on how many bricks and their edges obj intersects

        :param obj: Movable object
        :type obj: Movable
        """
        colls = self.__find_bricks(obj)
        # one brick
        if len(colls) == 1:
            edges = Common.find_side_collision(colls[0], obj)
            # two edges means intersection with angle of a brick
            if len(edges) > 1:
                obj.velocity.y = -obj.velocity.y
                obj.velocity.x = -obj.velocity.x
            # one edge means intersection with one side
            elif len(edges) == 1:
                if edges[0] in ('top', 'bottom'):
                    obj.velocity.y = -obj.velocity.y
                else:
                    obj.velocity.x = -obj.velocity.x
        # more than one brick (must be two)
        elif len(colls) > 1:
            try:
                edge1 = Common.find_side_collision(colls[0], obj)[0]
                edge2 = Common.find_side_collision(colls[1], obj)[0]
                comb1 = ('top', 'bottom')
                comb2 = ('right', 'left')
                # intersection with bricks that are situated on one y-position
                if edge1 in comb1 and edge2 in comb2:
                    obj.velocity.y = -obj.velocity.y
                # intersection with bricks which are situated on different y-position
                else:
                    obj.velocity.y = -obj.velocity.y
                    obj.velocity.x = -obj.velocity.x
            except: 
                print('По какой-то причине нет ребра столкновения')

    def draw(self, screen):
        for e in self.bricks:
            e.draw(screen)
    
    def generate(self, number):
        """
        generate(self, number):
        Generator random lines of bricks

        :param number: number of brick lines to generate
        """
        y = self.start_point
        for i in range(number):
            x = 0
            for j in range(line_limit):
                if random.randint(0, 4) != 2:
                    self.bricks.add(Brick(self.path + str(random.choice(self.images)), x, y))
                x += brick_size[0]
            y += brick_size[1]
