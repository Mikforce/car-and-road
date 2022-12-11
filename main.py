from direct.showbase.ShowBase import ShowBase
import panda3d
import fbx


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.fbx")
        self.scene.reparentTo(self.render)
        self.car.reparentTo(self.render)
        self.car.ls()
        self.car.list_joints()
        self.scene.setScale(0.25, 0.25, 5)
        self.scene.setPos(0, 6.5, -1)
        self.scene.setHpr(90, 0, 90)
        self.car.setScale(0.25, 0.25, 0.25)
        self.car.setPos(0, 6.5, -1)

if __name__ == '__main__':
    game = Game()
    game.run()

