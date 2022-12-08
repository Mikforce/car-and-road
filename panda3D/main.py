from direct.showbase.ShowBase import ShowBase
import panda3d


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.load_texture("sprites/game.png")


if __name__ == '__main__':
    game = Game()
    game.run()