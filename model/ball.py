import pygame
from pygame.locals import Rect


class Ball:
    def __init__(self, bar):
        self.image = pygame.Surface((20, 20))  # ボールのSurfaceは 20*20
        pygame.draw.circle(
            self.image, (255, 255, 255), (10, 10), 10
        )  # ボールの中心は(10,10)半径は10、色は白
        self.bar = bar
        self.rect = self.image.get_rect()
        self.rect.centerx = bar.rect.centerx  # ボールのxの初期位置は棒の中心に合わせる
        self.rect.bottom = bar.rect.top  # ボールのyの初期位置は棒の上辺に合わせる
        self.dx, self.dy = 3, -4  # ボールのx軸、y軸のスピード
        self.status = "INIT"

    def start(self):
        self.status = "RUNNING"

    def update(self, SCREEN: pygame.locals.Rect):
        if self.status == "INIT":
            self.rect.centerx = (
                self.bar.rect.centerx
            )  # ボールのxの初期位置は棒の中心に合わせる
            self.rect.bottom = (
                self.bar.rect.top
            )  # ボールのyの初期位置は棒の上辺に合わせる
            return

        old_rect = self.rect.copy()
        self.rect.move_ip(self.dx, self.dy)
        if self.rect.colliderect(self.bar.rect):
            if self.bar.rect.left >= old_rect.right:
                self.rect.right = self.bar.rect.left
                self.dx = -self.dx
            elif self.bar.rect.right < old_rect.left:
                self.rect.left = self.bar.rect.right
                self.dx = -self.dx
            elif self.bar.rect.top >= old_rect.bottom:
                self.rect.bottom = self.bar.rect.top
                self.dy = -self.dy
            else:
                self.rect.top = self.bar.rect.bottom
                self.dy = -self.dy
        if self.rect.left < SCREEN.left or self.rect.right > SCREEN.right:
            self.dx = -self.dx
        if self.rect.top < SCREEN.top:
            self.dy = -self.dy
        if self.rect.bottom > SCREEN.bottom:
            self.status = "INIT"
        self.rect.clamp_ip(SCREEN)

    def draw(self, screen_surface: pygame.Surface):
        screen_surface.blit(self.image, self.rect)
