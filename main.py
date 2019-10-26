import pygame  
from objects import board, ball
import constants as const  

pygame.init()
screen = pygame.display.set_mode(const.size)
clock = pygame.time.Clock()
board = board.Board('assets/board.png')
ball = ball.Ball('assets/ball.png', board)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                const.is_ball_go = True
    screen.fill(const.BLACK)
    screen.blit(board.image, board.rect)
    screen.blit(ball.image, ball.rect)
    board.update()
    ball.update()
    pygame.display.update()
    clock.tick(const.FPS)