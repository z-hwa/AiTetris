from settings import *
from tetris import Tetris
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris') #set windows name 'Tetris'
        self.screen = pg.display.set_mode(FIELD_RES) #show the screen with FIELD_RES
        self.clock = pg.time.Clock() #create clock to help us to determine the runing FPS
        self.tetris = Tetris(self) #instance tetris class

    def update(self):
        self.tetris.update() #更新tetris class
        self.clock.tick(FPS) #每幀調用一次，能確保遊戲運行一秒不超過FPS幀

    def draw(self):
        self.screen.fill(color=FIELD_COLOR) #填充螢幕顏色
        self.tetris.draw() #畫出tetris
        pg.display.flip() #更新螢幕

    def check_event(self):
        #監聽事件
        for event in pg.event.get():
            #如果接收到按鍵被按下 且是  K_ESCAPE '^['  escape 退出
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()