import pygame

from utils.constants import (
    GREEN,
    SCREEM_WHIDTH,
    SCREEM_HEIGHT
 )

from components.bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEM_WHIDTH/2
        self.rect.bottom = SCREEM_HEIGHT - 10

    def update(self):
        self.movement_on_x = 10
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.right >= SCREEM_WHIDTH:
            self.rect.right = SCREEM_WHIDTH



        if key[pygame.K_LEFT]:
            self.rect.x -= 5

        if self.rect.left <= 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets = pygame.sprite.Group()
        self.bullets.add(bullet)





