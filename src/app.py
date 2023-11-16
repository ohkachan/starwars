import pygame
from pygame.locals import *
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Test")

    while (1):
        screen.fill((0,0,0))        # 画面を黒色に塗りつぶし
        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()
