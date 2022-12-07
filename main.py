import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera

# Classes
class Game:  # Game's class
    def __init__(self, win_size=(1600, 900)):  # Game's initialization
        pg.init()
        self.win_size = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode(self.win_size, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        self.clock = pg.time.Clock()
        self.time = 0
        self.camera = Camera(self)
        self.scene = Cube(self)

    @staticmethod
    def check_event():
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def render(self):
        self.ctx.clear()
        self.scene.render()
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def update(self):
        while True:
            self.get_time()
            self.check_event()
            self.render()
            self.clock.tick(60)

    def run(self):
        self.update()

if __name__ == "__main__":
    game = Game()
    game.run()
