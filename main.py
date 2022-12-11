from direct.showbase.ShowBase import ShowBase
import panda3d


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.obj")
        self.scene.getPos()
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 5)
        self.scene.setPos(0, 6.5, -1)
        self.scene.setHpr(0, 90, 0)

if __name__ == '__main__':
    game = Game()
    game.run()

