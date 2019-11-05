import pygame
import random
import os
from helps import Common, line_limit, brick_size
from objects.brick import Brick
from base_classes import GameObject

pygame.mixer.init()


class Bricks:
    """
    Class containing bricks

    Attributes:
          bricks       list of bricks
          path         path to dir with images
          images       list of images from path
          start point  start point of generation
    """

    def __init__(self, path, score):
        self.count = 0
        self.bricks = pygame.sprite.Group()
        self.start_point = 25
        self.path = path
        self.images = os.listdir(self.path)
        self.destroy_sound = pygame.mixer.Sound('assets/sound/destroy_brick.wav')
        self.score = score

    def find_bricks_colls(self, obj: GameObject):
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
        for i in range(len(res)):
            self.destroy_sound.play()
            self.score.increment_score()
            self.count += 1
        self.generate(self.count // 8)
        self.count %= 8
        return [key for key, val in res.items()]

    def draw(self, screen):
        for e in self.bricks:
            e.draw(screen)

    def __append__(self):
        """
        Push bricks bottom to clear first line for new bricks
        """
        for i in self.bricks:
            i.rect[1] += brick_size[1]

    def generate(self, number):
        """
        generate(self, number):
        Generator random lines of bricks

        :param number: number of brick lines to generate
        """
        y = self.start_point
        for i in range(number):
            self.__append__()
            x = 0
            for j in range(line_limit):
                if random.randint(0, 4) != 2:
                    self.bricks.add(Brick(os.path.join(self.path, str(random.choice(self.images))), x, y))
                x += brick_size[0]
