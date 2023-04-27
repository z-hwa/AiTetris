import pygame as pg

vec = pg.math.Vector2 #二維class

FPS = 60 #遊戲幀率
FIELD_COLOR = (48, 39, 32) #背景顏色

TILE_SIZE = 40 #單個方塊的大小
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20 #整個遊戲區塊的單位大小
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE #計算實際的遊戲區塊面積 單位遊戲區塊*單個方塊大小

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)  #預設的pos 根據寬度隨機生成
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)} #移動方向

#各種形狀的俄羅斯方塊
TETROMINOS = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)],
}
