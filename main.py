import pygame
from objects import *
import helps.constants as const 
from score import Score

pygame.init()
screen = pygame.display.set_mode(const.size)
clock = pygame.time.Clock()

board = Board('assets/board.png')
bricks = Bricks('assets/bricks/')
ball = Ball('assets/ball.png', board, bricks)
score = Score()

bricks.generate(5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                const.is_ball_go = True
    screen.fill(const.BLACK)

    board.update()
    ball.update()

    board.draw(screen)
    ball.draw(screen)
    bricks.draw(screen)
    score.draw(screen)

    pygame.display.update()
    clock.tick(const.FPS)
