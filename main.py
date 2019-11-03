import pygame
from objects import *
from menu import *
import helps.constants as const 
from score import Score
from game import Game

pygame.init()
screen = pygame.display.set_mode(const.size)

while True:
    menu = Menu(screen)
    btn = menu.menu_loop()
    if btn == ButtonType.Start:
        game = Game(screen)
        game.game_loop()
    elif btn == ButtonType.Records:
        # дописать
        pass
    else:
        exit()