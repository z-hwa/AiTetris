from settings import *
from tetromino import Tetromino
import math

class Tetris:
    def __init__(self, app):
        self.app = app #將self 的 app 設為傳入的app
        self.sprite_group = pg.sprite.Group() #將self 的 物件群組設為ps的物件群組
        self.tetromino = Tetromino(self) #將self的tetromino設定為腳本tetromino

    #可以操控方塊的左右移動
    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')

    def draw_grid(self):
        #畫出背景格線
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black',(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        #動畫觸發是true 才繼續update
        if self.app.anim_trigger:
            self.tetromino.update() #呼叫tetromino的腳本 並執行其中的update
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
