import random
import pygame
from constants import brick_size as bs
from constants import line_limit as limit
from objects.brick import Brick
import os

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

    def __init__(self):
        self.bricks = []
        self.start_point = 25
        self.path = "assets/bricks/"
        self.images = os.listdir(self.path)
        self.destroy_sound = pygame.mixer.Sound('assets/sound/destroy_brick.wav')

    def find_brick(self, x, y):
        """
         Find brick at x, y coordinates
         return True if found and destroy
         return False if not found
        :param x: x coordinate
        :param y: y coordinate
        :return: False if brick not found
        :return: True if brick found and destroy it
        """
        for i in range(len(self.bricks)):
            if self.bricks[i].rect[0] <= x <= (self.bricks[i].rect[0] + bs[0]):
                if self.bricks[i].rect[1] <= y <= (self.bricks[i].rect[1] + bs[1]):
                    self.destroy_sound.play()
                    self.bricks.pop(i)
                    return True
        return False

    def __append__(self):
        """
        Push bricks bottom to clear first line for new bricks
        """
        for i in self.bricks:
            i.rect[1] += bs[1]

    def generate(self, number):
        """
        generate(self, number):
        Generator random lines of bricks
        :param number: number of brick lines to generate
        """
        for i in range(number):
            self.__append__()
            x = 0
            for j in range(limit):
                if random.randint(0, 4) != 2:
                    self.bricks.append(Brick(self.path + str(random.choice(self.images)), x, self.start_point))
                x += bs[0]
