import random

from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE]) #用於顯示圖片的物件
        self.image.fill('orange') #填充橘色

        self.rect = self.image.get_rect() #獲取Surface中的rect
        self.rect.topleft = self.pos * TILE_SIZE #設定rect屬性 左上角


class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOS.keys())) #隨機選取鍵值(俄羅斯方塊種類)
        self.blocks = [Block(self, pos) for pos in TETROMINOS[self.shape]] #根據shape中定義的pos 生成一個俄羅斯方塊

    def update(self):
        pass