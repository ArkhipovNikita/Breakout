import pygame
import constants as const
from objects.game_object import GameObject
from vector2d import Vector2D
import random


class Ball(pygame.sprite.Sprite, GameObject):
    def __init__(self, filename, board):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, filename)
        self.radius = self.width / 2
        self.speed = 10
        self.velocity = Vector2D(random.randint(-self.speed, self.speed), -self.speed)
        self.board = board

    def update(self):
        if not const.is_ball_go:
            self.rect.x = self.board.rect.x + self.board.width / 2 - self.radius
            self.rect.y = self.board.rect.y - self.radius * 2
        if const.is_ball_go:
            self.__bump_into_wall()
            self.__bump_into_board()
            self.rect.y += self.velocity.y
            self.rect.x += self.velocity.x

    def __bump_into_wall(self):
        if self.left <= 0 or self.right >= const.width:
            self.velocity.x = -self.velocity.x
        if self.top <= 0:
            self.velocity.y = -self.velocity.y

    def __bump_into_board(self):
        if self.rect.colliderect(self.board.rect):
            self.velocity.y = -self.velocity.y
            self.velocity.x = random.randint(-self.speed, self.speed)
