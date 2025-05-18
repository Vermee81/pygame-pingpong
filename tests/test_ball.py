import pytest
import pygame
from pygame.locals import Rect
from model.ball import Ball
from model.bar import Bar


@pytest.fixture
def screen():
    pygame.init()
    screen = Rect((0, 0, 400, 600))
    yield screen
    pygame.quit()


@pytest.fixture
def bar(screen):
    return Bar(screen)


@pytest.fixture
def ball(bar):
    return Ball(bar)


def test_initial_state(ball, bar):
    assert ball.status == "INIT"
    assert ball.dx == 3
    assert ball.dy == -4
    assert ball.rect.centerx == bar.rect.centerx
    assert ball.rect.bottom == bar.rect.top


def test_start(ball):
    ball.start()
    assert ball.status == "RUNNING"


def test_wall_collision_left(ball, screen):
    ball.start()
    ball.rect.left = -1
    ball._handle_wall_collision(screen)
    assert ball.dx == -3  # dx は負の値になっているはず


def test_wall_collision_right(ball, screen):
    ball.start()
    ball.rect.right = screen.right + 1
    ball._handle_wall_collision(screen)
    assert ball.dx == -3  # dx は負の値になっているはず


def test_wall_collision_top(ball, screen):
    ball.start()
    ball.rect.top = -1
    ball._handle_wall_collision(screen)
    assert ball.dy == 4  # dy は正の値になっているはず


def test_wall_collision_bottom(ball, screen):
    ball.start()
    ball.rect.bottom = screen.bottom + 1
    ball._handle_wall_collision(screen)
    assert ball.status == "INIT"  # ボールが下の壁に当たったら INIT 状態に戻るはず
