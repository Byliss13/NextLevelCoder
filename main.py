from components.game import Game
import pygame
if __name__ == "__main__":
    game = Game()
    while game.running:
        if not game.playing:
            game.show_start_screen()
            if not game.playing:
                game.show_start_screen_part2()
                game.run()

    pygame.quit()
