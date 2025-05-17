import pygame
from pygame.locals import QUIT, Rect, MOUSEBUTTONDOWN
from model.bar import Bar
from model.ball import Ball
import sys


def main():
    pygame.init()
    SCREEN = Rect((0, 0, 400, 600))
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("Let's PingPong")

    clock = pygame.time.Clock()

    """棒とボールの設定"""
    bar = Bar(SCREEN)
    ball = Ball(bar)

    while True:

        screen.fill((0, 0, 0))

        bar.update(SCREEN)
        ball.update(SCREEN)

        bar.draw(screen)
        ball.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                ball.start()

        clock.tick(60)


if __name__ == "__main__":
    main()
