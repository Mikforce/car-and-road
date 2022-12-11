from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import gltf


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        node = NodePath("PhysicsNode")
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.gltf")
        self.car_texture = self.loader.loadTexture("sprites/game.png")
        self.car.set_texture(self.car_texture, 1)
        node.reparentTo(self.render)
        self.scene.reparentTo(self.render)
        self.car.reparentTo(self.render)
        self.car.ls()
        self.scene.setScale(0.25, 0.25, 5)
        self.scene.setPos(0, 6.5, -1)
        self.scene.setHpr(90, 0, 90)
        self.car.setScale(0.25, 0.25, 0.25)
        node.physicsMgr.attachPhysicalNode(self.car)
        self.car.setPos(0, 6.5, -0.5)

if __name__ == '__main__':
    game = Game()
    game.run()

