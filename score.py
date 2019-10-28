import pygame
from helps import constants as const
from pygame.locals import *

# from player import nickname
nickname = "qwerty"

pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 25)


class Score:
    def __init__(self):
        self.path = "top_plays.txt"
        self.local_score = 0
        self.scores = self.__plays__()[:-1]
        self.text = font_renderer.render("Score: " + str(self.local_score), 1, const.FONT_COLOR)
        self.record = font_renderer.render("Leader: " + str(self.scores[0][1]), 1, const.FONT_COLOR)

    def __plays__(self):
        """
        Read file with leader board and return list of them
        :return: list of scores from leader board
        """
        return [s.split(" ") for s in open(self.path).read().split("\n")]

    def save(self):
        """
        Save the leader board in sorted order
        """
        self.scores.append([nickname, self.local_score])
        self.scores = sorted(self.scores, key=lambda x: 1 / int(x[1]))
        file = open(self.path, 'w')
        for i in self.scores:
            file.write(i[0] + " " + str(i[1]) + "\n")
        self.local_score = 0

    def draw(self, screen):
        screen.blit(self.text, const.SCORE_PLACE)
        screen.blit(self.record, const.RECORD_PLACE)
    
    def increment_score(self):
        """
        Increment player score by points from constants
        """
        self.local_score += const.points
        self.text = font_renderer.render("Score: " + str(self.local_score), 1, const.FONT_COLOR)
