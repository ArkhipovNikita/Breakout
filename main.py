import pygame
from objects import board, ball
import constants as const
from bricks import Bricks
from score import Score

pygame.init()
screen = pygame.display.set_mode(const.size)
clock = pygame.time.Clock()
board = board.Board('assets/board.png')
ball = ball.Ball('assets/ball.png', board)
bricks = Bricks()
bricks.generate(5)
score = Score()


# не могу перенести
def bricks_draw():
    for i in bricks.bricks:
        screen.blit(i.image, i.rect)


def score_draw():
    screen.blit(score.text, const.SCORE_PLACE)
    screen.blit(score.record, const.RECORD_PLACE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                const.is_ball_go = True
    screen.fill(const.BLACK)

    score_draw()
    bricks_draw()
    bricks.find_brick(10, 125)
    screen.blit(board.image, board.rect)
    screen.blit(ball.image, ball.rect)
    board.update()
    ball.update()
    pygame.display.update()
    clock.tick(const.FPS)
