import pygame
from objects import *
from helps import *
from menu import Menu, ButtonType

class Lifes:
    """
    Class describes lifes 

    Attribute:
        lifes   number of lifes 
    """
    def __init__(self, lifes: int):
        self.lifes = lifes
        self.text = font_renderer.render("Lifes: " + str(self.lifes), 1, FONT_COLOR)

    def decrement_lifes(self):
        """
        Decrement lifes by 1 point
        """
        self.lifes -= 1
        self.text = font_renderer.render("Lifes: " + str(self.lifes), 1, FONT_COLOR)
    
    def draw(self, screen):
        screen.blit(self.text, (width - self.text.get_width(), 2))
 
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
    def __init__(self, screen, score):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.score = score
        self.board = Board('assets/board.png')
        self.bricks = Bricks('assets/bricks/', self.score)
        self.ball = Ball('assets/ball.png', self.board, self.bricks)
        self.lifes = Lifes(3)
    
    @property
    def is_gameover(self):
        """
        Game is over on not

        :return: True if game is over
        :return: False if game is not over
        """
        return self.lifes.lifes < 0

    @property
    def is_dead(self):
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
            self.lifes.draw(self.screen)

            if self.is_dead:
                self.lifes.decrement_lifes()
                self.ball = Ball('assets/ball.png', self.board, self.bricks)
                is_ball_go = False

            # добавить в update ball, board и удаленные bricks, чтобы только эти части экрана обновлялись
            pygame.display.update()
            self.clock.tick(FPS)
        self.score.save()
