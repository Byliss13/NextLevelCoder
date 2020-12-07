import pygame
from os import path
from utils.constants import (
    GREEN,
    BLACK,
    SCREEM_WHIDTH,
    SCREEM_HEIGHT,
    IMG_DIR
 )

from components.bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, game, image):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEM_WHIDTH/2
        self.rect.bottom = SCREEM_HEIGHT - 10
        self.bullets = pygame.sprite.Group()

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

    def shoot(self, condic):
        sound_rifle = pygame.mixer.Sound(path.join(IMG_DIR, "rifle.ogg"))
        pygame.mixer.Sound.play(sound_rifle)
        condicional = condic
        if condicional == False:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.bullets.add(bullet)
        elif condicional == True:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet2 = Bullet(self.rect.centerx-10, self.rect.top)
            bullet3 = Bullet(self.rect.centerx-20, self.rect.top)
            bullet4 = Bullet(self.rect.centerx+10, self.rect.top)
            bullet5 = Bullet(self.rect.centerx+20, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.game.all_sprites.add(bullet2)
            self.game.all_sprites.add(bullet3)
            self.game.all_sprites.add(bullet4)
            self.game.all_sprites.add(bullet5)
            self.bullets.add(bullet)
            self.bullets.add(bullet2)
            self.bullets.add(bullet3)
            self.bullets.add(bullet4)
            self.bullets.add(bullet5)





