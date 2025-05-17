import pygame


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

    def update(self, SCREEN: pygame.locals.Rect):
        self.rect.move_ip(self.dx, self.dy)
        if self.rect.left < SCREEN.left or self.rect.bottom > SCREEN.bottom:
            self.dx = -self.dx
        if self.rect.top < SCREEN.top or self.rect.bottom > SCREEN.bottom:
            self.dy = -self.dy
        self.rect.clamp_ip(SCREEN)

    def draw(self, screen_surface: pygame.Surface):
        screen_surface.blit(self.image, self.rect)
