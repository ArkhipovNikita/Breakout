import pygame
import constants as const
from objects.game_object import GameObject

margin = 10


class Board(pygame.sprite.Sprite, GameObject):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, filename)
        self.rect.x = const.width / 2 - self.width / 2
        self.rect.y = const.height - self.height - 15
        self.step = 12

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < const.width - margin - self.width:
            self.rect.x += self.step
        elif keys[pygame.K_LEFT] and self.rect.x > margin:
            self.rect.x -= self.step
