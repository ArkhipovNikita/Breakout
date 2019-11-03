import pygame
import random
from helps import constants as const
from helps import Common, Vector2D
from base_classes import * 
from objects.board import Board
from objects.bricks import Bricks


class Ball(pygame.sprite.Sprite, GameObject):
    """ 
    Class describing behavior of ball object
    Class inherits GameObject class

    Attributes:
        radius      radius of ball
        speed       speed/step of moving
        velocity    direction of moving (vector)
        board        link to a board
        bricks      link to a bricks
    """
    def __init__(self, filename, board: Board, bricks: Bricks):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, filename)
        self.radius = self.width / 2
        self.speed = 15
        self.velocity = Vector2D(random.randint(-self.speed, self.speed), -self.speed)
        self.board = board
        self.bricks = bricks
    

    def update(self, is_ball_go):
        """ 
        Update coordinate of a ball
            Until key space isn't pressed, the ball will follow for board
            After pressing key scpace, the ball will jump intersecting from other objects

        :param board: a bord that is followed by ball
        :type board: Board
        """
        if not is_ball_go:
            self.rect.x = self.board.rect.x + self.board.width / 2 - self.radius
            self.rect.y = self.board.rect.y - self.radius * 2
        if is_ball_go:
            self.__bump_into_walls()
            self.__bump_into_board()
            self.__bump_into_bricks()
            self.rect.y += self.velocity.y
            self.rect.x += self.velocity.x

    def __bump_into_board(self):
        """ 
        If obj intersects with a side of a board, velocity of ball is changed
        depending on how many sides obj intersects
        """
        # is there intersection
        if self.rect.colliderect(self.board.rect):
            edges = Common.find_side_collision(self.board, self)
            if 'top' in edges:
                self.velocity.y = -self.velocity.y
                # angle
                if 'right' in edges or 'left' in edges:
                    self.velocity.x = -self.velocity.x
                else:
                     self.velocity.x = random.randint(-self.speed, self.speed)
            elif 'right' in edges or 'left' in edges:
                self.velocity.x = -self.velocity.x

    # иногда мяч застревает в боковой стене
    def __bump_into_walls(self):
        """ 
        If a ball intersects with walls apart from bottom wall, velocity of the ball will change 
        """
        if self.left <= 0 or self.right >= const.width:
            self.velocity.x = -self.velocity.x
        if self.top <= 0:
           self.velocity.y = -self.velocity.y

    def __bump_into_bricks(self):
        """
        Change velocity of a obj if it intersects bricks
        Type of chanhing velocity depends on how many bricks and their edges obj intersects
        """
        colls = self.bricks.find_bricks_colls(self)
        # one brick
        if len(colls) == 1:
            edges = Common.find_side_collision(colls[0], self)
            # two edges means intersection with angle of a brick
            if len(edges) > 1:
                self.velocity.y = -self.velocity.y
                self.velocity.x = -self.velocity.x
            # one edge means intersection with one side
            elif len(edges) == 1:
                if edges[0] in ('top', 'bottom'):
                    self.velocity.y = -self.velocity.y
                else:
                    self.velocity.x = -self.velocity.x
        # more than one brick (must be two)
        elif len(colls) > 1:
            edge1 = Common.find_side_collision(colls[0], self)[0]
            edge2 = Common.find_side_collision(colls[1], self)[0]
            comb1 = ('top', 'bottom')
            comb2 = ('right', 'left')
            # intersection with bricks that are situated on one y-position
            if edge1 in comb1 and edge2 in comb1:
            # if edge1 in comb1 and edge2 in comb1:
                self.velocity.y = -self.velocity.y
            # intersection with bricks that are situated on one x-position
            elif edge1 in comb2 and edge2 in comb2:
                self.velocity.x = -self.velocity.x
            # intersection with bricks which are situated on different y-position and x-position
            else:
                self.velocity.y = -self.velocity.y
                self.velocity.x = -self.velocity.x