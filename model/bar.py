import pygame
from pygame.locals import Rect


class Bar:
    def __init__(self, SCREEN: pygame.locals.Rect):
        self.image = pygame.Surface((50, 10))  # 棒のSurfaceは横50、縦10
        self.image.fill((255, 255, 255))  # 棒の色は白
        self.rect = self.image.get_rect()
        self.rect.center = (
            SCREEN.centerx,
            SCREEN.bottom - 50,
        )  # 棒の初期位置xは画面の中心、初期位置yは画面の下辺から50上

    def update(self, SCREEN: pygame.locals.Rect):
        self.rect.centerx = pygame.mouse.get_pos()[
            0
        ]  # get_posでx座標とy座標のtupleが返ってくるので、tupleの最初の要素をとる
        self.rect.clamp_ip(SCREEN)

    def draw(self, screen_surface: pygame.Surface):
        screen_surface.blit(self.image, self.rect)
