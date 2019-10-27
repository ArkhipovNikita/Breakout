import pygame 
from objects import board, ball
import constants as const

class Game:
    def __init__(self, board_path, ball_path):
        self.board = board.Board(board_path)
        self.ball = ball.Ball(ball_path)
        self.__is_ball_go = False
    
    @property
    def is_ball_go(self):
        return self.__is_ball_go
