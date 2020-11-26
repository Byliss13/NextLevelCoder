import pygame
from utils.constants import (
    SCREEM_HEIGHT,
    SCREEM_WHIDTH,
    TITLE
)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        pygame.display.set_mode((SCREEM_WHIDTH,SCREEM_HEIGHT))

    def run(self):
        self.create_components()
        #game loop:
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()



    def create_components(self):
        pass


    def update(self):
        pass


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing =False




    def draw(self):
        pass
