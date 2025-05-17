import pygame
from pygame.locals import QUIT, Rect
import sys


def main():
    pygame.init()
    SCREEN = Rect((0, 0, 400, 600))
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("Let's PingPong")

    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)


if __name__ == "__main__":
    main()
