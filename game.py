import pygame
from objects import *
from helps import *
from menu import Menu, ButtonType
from score import Score

class Game:
    """
    Class describes game process

    Attributes:
        screen      dispalay of the app, game
        clock       var for handle speed of game cycle
        score       
        board
        bricks
        ball
    """
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.score = Score()
        self.board = Board('assets/board.png')
        self.bricks = Bricks('assets/bricks/', self.score)
        self.ball = Ball('assets/ball.png', self.board, self.bricks)
    
    @property
    def is_gameover(self):
        """
        Game is over on not

        :return: True if game is over
        :return: False if game is not over
        """
        return self.ball.top >= height
    
    def game_loop(self):
        """ 
        Loop of game process
        """
        self.bricks.generate(5)
        is_ball_go = False
        while not self.is_gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        is_ball_go = True
            self.screen.fill(const.BLACK)

            self.board.update()
            self.ball.update(is_ball_go)

            self.board.draw(self.screen)
            self.ball.draw(self.screen)
            self.bricks.draw(self.screen)
            self.score.draw(self.screen)

            # добавить в update ball, board и удаленные bricks, чтобы только эти части экрана обновлялись
            pygame.display.update()
            self.clock.tick(FPS)
        self.score.save()
