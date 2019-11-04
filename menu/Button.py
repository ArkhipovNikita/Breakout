import pygame
from helps import width
from menu.ButtonType import ButtonType

class Button(pygame.sprite.Sprite):
    """ 
    Class describes a button

    Attributes:
        name            type of a button
    """
    def __init__(self, image_path, type_btn: ButtonType, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = type_btn
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center = (width / 2, y))

    def is_clicked(self, mouse_pos):
        """ 
        Mouse intersects a button or not

        :param mouse_pos: position of mouse

        :return: True if mouse intersects
        :return: False if mouse doesn't intersect 
        """
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)