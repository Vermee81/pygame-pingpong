import pygame
from pygame.locals import QUIT, Rect
from model.bar import Bar
import sys


def main():
    pygame.init()
    SCREEN = Rect((0, 0, 400, 600))
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("Let's PingPong")

    clock = pygame.time.Clock()

    """棒とボールの設定"""
    bar = Bar(SCREEN)
    ball = pygame.Surface((20, 20))  # ボールのSurfaceは 20*20
    pygame.draw.circle(
        ball, (255, 255, 255), (10, 10), 10
    )  # ボールの中心は(10,10)半径は10、色は白
    ball_rect = ball.get_rect()
    ball_rect.centerx = bar.rect.centerx  # ボールのxの初期位置は棒の中心に合わせる
    ball_rect.bottom = bar.rect.top  # ボールのyの初期位置は棒の上辺に合わせる
    dx, dy = 3, -4  # ボールのx軸、y軸のスピード

    while True:

        screen.fill((0, 0, 0))

        bar.update(SCREEN)

        ball_rect.move_ip(dx, dy)
        if ball_rect.left < SCREEN.left or ball_rect.bottom > SCREEN.bottom:
            dx = -dx
        if ball_rect.top < SCREEN.top or ball_rect.bottom > SCREEN.bottom:
            dy = -dy
        ball_rect.clamp_ip(SCREEN)

        bar.draw(screen)
        screen.blit(ball, ball_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)


if __name__ == "__main__":
    main()
