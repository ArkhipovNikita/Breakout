import pygame
import random
import math
from helps import constants as const
from helps import Common, Vector2D, Sides
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
        self.filename = filename
        self.radius = self.width / 2
        self.speed = 8
        x = random.random()
        y = math.sqrt(1 - x * x)
        self.velocity = Vector2D(x, y)
        self.board = board
        self.bricks = bricks
        self.coll_sound = pygame.mixer.Sound('assets/sound/coll_with_board.wav')

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
            ahead_ball = self.__give_ahead_ball()
            self.__bump_into_walls(ahead_ball)
            self.__bump_into_board(ahead_ball)
            self.__bump_into_bricks(ahead_ball)
            self.rect.y += self.velocity.y * self.speed
            self.rect.x += self.velocity.x * self.speed

    def __bump_into_board(self, ahead_ball):
        """ 
        If obj intersects with a side of a board, velocity of ball is changed
        depending on how many sides obj intersects
        """
        # is there intersection
        if ahead_ball.rect.colliderect(self.board.rect):
            edges = Common.find_side_collision(self.board, self)
            if Sides.Top in edges:
                self.velocity.y = -self.velocity.y
                # angle
                if edges in (Sides.Right, Sides.Left):
                    self.velocity.x = -self.velocity.x
                else:
                     self.velocity.x = random.random()
            elif edges in (Sides.Right, Sides.Left):
                self.velocity.x = -self.velocity.x
            self.coll_sound.play()

    # иногда мяч застревает в боковой стене
    def __bump_into_walls(self, ahead_ball):
        """ 
        If a ball intersects with walls apart from bottom wall, velocity of the ball will change 
        """
        if ahead_ball.left <= 0 or ahead_ball.right >= const.width:
            self.velocity.x = -self.velocity.x
            self.coll_sound.play()
        if self.top <= 0:
           self.velocity.y = -self.velocity.y
           self.coll_sound.play()

    def __give_ahead_ball(self):
        """
        Give a ball is ahead by one step
        """
        ball_ahead = Ball(self.filename, self.board, self.bricks)
        ball_ahead.rect.x, ball_ahead.rect.y = self.rect.x, self.rect.y
        ball_ahead.rect.x += self.velocity.x
        ball_ahead.rect.y += self.velocity.y
        return ball_ahead

    def __bump_into_bricks(self, ahead_ball):
        """
        Change velocity of a obj if it intersects bricks
        Type of chanhing velocity depends on how many bricks and their edges obj intersects
        """
        colls = self.bricks.find_bricks_colls(ahead_ball, self)
        length = len(colls)
        # one brick
        if length == 1:
            edges = Common.find_side_collision(colls[0], ahead_ball)
            # two edges means intersection with angle of a brick
            if len(edges) > 1:
                self.velocity.y = -self.velocity.y
                self.velocity.x = -self.velocity.x
            # one edge means intersection with one side
            elif len(edges) == 1:
                if edges[0] in (Sides.Top, Sides.Bottom):
                    self.velocity.y = -self.velocity.y
                else:
                    self.velocity.x = -self.velocity.x
        # more than one brick (must be two)
        elif length > 1:
            edge1 = Common.find_side_collision(colls[0], ahead_ball)[0]
            edge2 = Common.find_side_collision(colls[1], ahead_ball)[0]
            comb1 = (Sides.Top, Sides.Bottom)
            comb2 = (Sides.Right, Sides.Left)
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