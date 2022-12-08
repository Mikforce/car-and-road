from direct.showbase.ShowBase import ShowBase
import panda3d


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("")
        self.scene.reparentTo(self.render)


if __name__ == '__main__':
    game = Game()
    game.run()