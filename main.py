import pygame
from objects import *
from menu import *
import helps.constants as const 
from score import Score
from game import Game

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('assets/sound/back.wav')
pygame.mixer.music.play(loops=-1)
screen = pygame.display.set_mode(const.size)
score = Score()

while True:
    menu = Menu(screen)
    btn = menu.menu_loop()
    if btn == ButtonType.Start:
        game = Game(screen, score)
        game.game_loop()
    elif btn == ButtonType.Records:
        score.records_loop(screen)
    else:
        pygame.mixer.quit()
        exit()