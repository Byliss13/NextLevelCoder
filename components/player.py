import pygame

from utils.constants import (
    GREEN,
    SCREEM_WHIDTH,
    SCREEM_HEIGHT
 )


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEM_WHIDTH/2
        self.rect.centery = SCREEM_HEIGHT/2

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.right >= SCREEM_WHIDTH:
            self.rect.right = SCREEM_WHIDTH



