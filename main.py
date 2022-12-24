from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from panda3d.physics import *
import time
import random

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Model Init
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.gltf")
        self.obstacle1 = self.loader.loadModel("models/car.gltf")
        self.obstacle2 = self.loader.loadModel("models/car.gltf")
        self.car.ls()

        # Texture Init
        self.car_texture = self.loader.loadTexture("sprites/game.png")

        # Set Texture
        self.car.set_texture(self.car_texture, 1)

        #Reparent To
        self.scene.reparentTo(self.render)
        self.car.reparentTo(self.render)
        self.obstacle1.reparentTo(self.render)
        self.obstacle2.reparentTo(self.render)

        # Scale
        self.scene.setScale(0.26, 0.26, 5)
        self.car.setScale(0.25, 0.25, 0.25)
        self.obstacle1.setScale(0.25, 0.25, 0.25)
        self.obstacle2.setScale(0.25, 0.25, 0.25)
        # Pos
        self.scene.setPos(0, 6.5, -1)
        self.car.setPos(0, 6.5, -0.74)
        self.obstacle1.setPos(0, 50, -0.74)
        self.obstacle2.setPos(0, 50, -0.74)
        # Rotation
        self.car.setHpr(90, 0, 90)
        self.scene.setHpr(90, 0, 90)

        # Buttons
        self.accept('a', self.input)
        self.accept('d', self.input)
        self.accept('r', self.spawn_obstacle)

        self.is_down = self.mouseWatcherNode.is_button_down

        self.moveArr = 1
        self.arr = [-.78, 0, .78]

        # self.disableMouse()

        self.taskMgr.add(self.update, "update")

        self.obst1y = 50
        self.obst2y = 50
    def spawn_obstacle(self):
        arr = []
        for i in range(2):
            arr.append(random.choice(self.arr))
        self.obstacle1.setPos(arr[0], 50, -0.74)
        self.obstacle2.setPos(arr[1], 50, -0.74)

    def obstacle_movement(self):
        self.obst1y -= 1
        self.obst2y -= 1
        self.obstacle1.setPos(0, self.obst1y, -0.74)
        self.obstacle2.setPos(0, self.obst2y, -0.74)

    def update(self, task):
        self.obstacle_movement()
        # self.spawn_obstacle()
        return task.cont
    def input(self):
        if self.is_down("d"):
            self.movement(1)
        if self.is_down("a"):
            self.movement(-1)

    def movement(self, x):
        if self.moveArr + x in range(len(self.arr)):
            self.moveArr += x
            self.car.setPos(self.arr[self.moveArr], 6.5, -0.74)


if __name__ == '__main__':
    game = Game()
    game.run()