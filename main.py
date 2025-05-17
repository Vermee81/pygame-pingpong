import pygame
from pygame.locals import QUIT, Rect
import sys


def main():
    pygame.init()
    SCREEN = Rect((0, 0, 400, 600))
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("Let's PingPong")

    clock = pygame.time.Clock()

    """棒とボールの設定"""
    bar = pygame.Surface((50, 10))  # 棒のSurfaceは横50、縦10
    bar.fill((255, 255, 255))  # 棒の色は白
    bar_rect = bar.get_rect()
    bar_rect.center = (
        SCREEN.centerx,
        SCREEN.bottom - 50,
    )  # 棒の初期位置xは画面の中心、初期位置yは画面の下辺から50上
    ball = pygame.Surface((20, 20))  # ボールのSurfaceは 20*20
    pygame.draw.circle(
        ball, (255, 255, 255), (10, 10), 10
    )  # ボールの中心は(10,10)半径は10、色は白
    ball_rect = ball.get_rect()
    ball_rect.centerx = bar_rect.centerx  # ボールのxの初期位置は棒の中心に合わせる
    ball_rect.bottom = bar_rect.top  # ボールのyの初期位置は棒の上辺に合わせる

    while True:

        screen.fill((0, 0, 0))

        screen.blit(bar, bar_rect)
        screen.blit(ball, ball_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)


if __name__ == "__main__":
    main()
