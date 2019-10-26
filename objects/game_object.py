import pygame

class GameObject:
    def __init__(self, file_path):
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect()

    @property
    def width(self):
        return self.image.get_width()

    @property
    def height(self):
        return self.image.get_height()

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom
    
    @property
    def right(self):
        return self.rect.right
    
    @property
    def left(self):
        return self.rect.left
    