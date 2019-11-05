import pygame 

size = width, height = 900, 700
brick_size = (90, 25)
button_size = (373, 106)
line_limit = width // brick_size[0]
BLACK = (0, 0, 0)
FONT_COLOR = (255, 255, 255)
SCORE_PLACE = (0, 2)
RECORD_PLACE = (450, 2)
FPS = 480
points = 5

pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 25)
