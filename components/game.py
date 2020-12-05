import pygame
from components.ball import Ball
from components.powerup import Fruit
from components.player import Player
from utils.test_utils import draw_text
from os import path
from utils.constants import (
    SCREEM_HEIGHT,
    SCREEM_WHIDTH,
    TITLE,
    BLACK,
    IMG_DIR,
    FPS
)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((SCREEM_WHIDTH,SCREEM_HEIGHT))
        self.clock = pygame.time.Clock()
        self.backgroup_img = pygame.image.load(path.join(IMG_DIR, "spacefield.png"))
        self.backgroup_img = pygame.transform.scale(self.backgroup_img, (SCREEM_WHIDTH,SCREEM_HEIGHT))
        self.playing = False
        self.running = True
        self.condic = False
        pygame.mixer.init()
        pygame.mixer.music.load(path.join(IMG_DIR, "town4.mp3"))
        pygame.mixer.music.play(-1)
        self.contador = 0

    def run(self):
        self.create_components()
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



    def create_components(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.balls = pygame.sprite.Group()
        ball = Ball(1)
        self.all_sprites.add(ball)
        self.balls.add(ball)
        self.fruits = pygame.sprite.Group()
        fruit = Fruit()
        self.fruits.add(fruit)
        self.all_sprites.add(fruit)


    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player ,self.balls , False)
        if hits:
            self.playing = False
        hits = pygame.sprite.groupcollide(self.balls, self.player.bullets, True, True)
        if hits:
            self.contador+= 1
        for hit in hits :
            if hit.size < 4:
                for i in range(0, 2):
                    ball = Ball(hit.size + 1)
                    self.all_sprites.add(ball)
                    self.balls.add(ball)

        hit = pygame.sprite.spritecollide(self.player, self.fruits, True)
        if hit:
            self.condic = True


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing =False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self.condic)
            elif self.contador == 15:
                self.playing = False





    def draw(self):
        backgroup_rect = self.backgroup_img.get_rect()
        self.screen.blit(self.backgroup_img, backgroup_rect)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen (self):
        self.screen.blit(self.backgroup_img, self.backgroup_img.get_rect())
        draw_text(self.screen, "BIENVENIDO A MI JUEGAZO!!!!!", 40, SCREEM_WHIDTH/2, SCREEM_HEIGHT/4)
        draw_text(self.screen, "Presiona las teclas direcionales para moverse y SPACE para disparar", 18, SCREEM_WHIDTH/2, SCREEM_HEIGHT/2)
        draw_text(self.screen, "Presiona ENTER para jugar!!!!!!!", 20, SCREEM_WHIDTH/2, SCREEM_HEIGHT*3/5)
        pygame.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        waiting = False








