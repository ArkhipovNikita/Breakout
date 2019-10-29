import pygame
import os
from helps import *
from menu.ButtonType import ButtonType
from menu.Button import Button

class Menu:
    """
    Class describes menu of the game: contains buttons start, records, quit

    Attributes:
        screen      dispalay of the app, game
        btns        buttons list of start, record, quit
    """
    def __init__(self, screen):
        self.screen = screen
        self.__init_btns()

    def __init_btns(self):
        """ 
        Initialize the attribute btns
        """
        btns_name_list = [ButtonType.Start, ButtonType.Records, ButtonType.Quit]
        path = 'assets/buttons'
        images = os.listdir(path)
        images.sort()
        start_y = 100
        step_y = button_size[1] + 20
        self.btns = [Button(os.path.join(path, images[i]), btn, start_y + i * step_y) for i, btn in enumerate(btns_name_list)]
    
    def menu_loop(self):
        """ 
        Loop of option choosing by user
        """
        is_choosing = True
        btns_group = pygame.sprite.Group()
        btns_group.add(*self.btns)
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(True)
        while is_choosing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    btn = [btn for btn in self.btns if btn.is_clicked(event.pos)]
                    if len(btn) == 1:
                        is_choosing = False
                        return btn[0].name
            
            self.screen.fill(BLACK)
            btns_group.draw(self.screen)
            pygame.display.update()
            clock.tick(FPS)