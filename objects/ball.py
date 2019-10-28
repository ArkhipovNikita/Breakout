import pygame
import random
from helps import constants as const
from base_classes import * 
from objects.board import Board


class Ball(pygame.sprite.Sprite, GameObject, Movable):
    """ 
    Class describing behavior of ball object
    Class inherits GameObject and Movable classes

    Attributes:
        radius      radius of ball
        speed       speed/step of moving
        velocity    direction of moving (vector)
    """
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, filename)
        Movable.__init__(self, 15)
        self.radius = self.width / 2
        self.velocity = Vector2D(random.randint(-self.speed, self.speed), -self.speed)
    

    def update(self, board: Board):
        """ 
        Update coordinate of a ball
            Until key space isn't pressed, the ball will follow for board
            After pressing key scpace, the ball will jump

        :param board: a bord that is followed by ball
        :type board: Board
        """
        if not const.is_ball_go:
            self.rect.x = board.rect.x + board.width / 2 - self.radius
            self.rect.y = board.rect.y - self.radius * 2
        if const.is_ball_go:
            self.rect.y += self.velocity.y
            self.rect.x += self.velocity.x
