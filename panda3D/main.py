from direct.showbase.ShowBase import ShowBase
import panda3d
from math import *
from direct.task import Task


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.scene.getPos()
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(0, 0, 0)

        # Define a procedure to move the camera.
        def spinCameraTask(self, task):
            angleDegrees = task.time * 6.0
            angleRadians = angleDegrees * (pi / 180.0)
            self.camera.setPos(5, 0, 5)
            self.camera.setHpr(angleDegrees, 0, 0)
            return Task.cont

if __name__ == '__main__':
    game = Game()
    game.run()