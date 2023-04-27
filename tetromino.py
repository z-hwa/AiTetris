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

    def set_rect_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE #設定rect位置到pos的位置 左上角為描點

    def update(self):
        self.set_rect_pos() #不斷更新方塊位置


class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOS.keys())) #隨機選取鍵值(俄羅斯方塊種類)
        self.blocks = [Block(self, pos) for pos in TETROMINOS[self.shape]] #根據shape中定義的pos 生成一個俄羅斯方塊

    #方塊移動函數
    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction] #從移動方向中 選擇一個移動方向
        #為每一個生成的方塊添加移動量
        for block in self.blocks:
            block.pos += move_direction

    def update(self):
        self.move(direction = 'down') #向下移動
        pg.time.wait(200) #每200單位時間 向下移動一次
        
