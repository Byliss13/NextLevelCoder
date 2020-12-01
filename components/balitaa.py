import pygame
from utils.constants import (
    YELLOW,
    SCREEM_HEIGHT,
    SCREEM_WHIDTH
)
from components.player import (
    Player
)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        player = 50
        self.rect.x = player
        self.rect.y = SCREEM_HEIGHT - 10
    def update(self):
        key = pygame.key.()
        if key[pygame.K_SPACE]:
            self.rect.y -= 5

        #if self.rect.top <= 0:
            #self.rect.top = 0