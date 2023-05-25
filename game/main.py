# Other functions
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from panda3d.physics import *
import time
import random

# My functions
from calc import *
from panda3dfunctions import *
from entities import *

# Game Class
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.calc = Calculations()
        # Nodes
        self.node = NodePath("PhysicsNode")

        # Actor Node
        self.carActor = ActorNode("car")

        # Model Init
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.gltf")
        self.car.ls()

        # Attach Node
        self.carActorN = self.node.attachNewNode(self.carActor)

        # Texture Init
        self.car_texture = self.loader.loadTexture("sprites/game.png")

        # Set Texture
        self.car.set_texture(self.car_texture, 1)

        #Reparent To
        self.node.reparentTo(self.render)
        self.scene.reparentTo(self.render)
        self.car.reparentTo(self.carActorN)

        # Scale
        self.scene.setScale(0.26, 0.26, 10)
        self.car.setScale(0.25, 0.25, 0.25)

        # Pos
        self.scene.setPos(0, 6.5, -1)
        self.car.setPos(0, 6.5, -0.74)

        # Rotation
        self.car.setHpr(90, 0, 90)
        self.scene.setHpr(90, 0, 90)

        # Buttons
        self.accept("d", self.input)
        self.accept("a", self.input)

        self.obstacle_arr = []

        self.is_down = self.mouseWatcherNode.is_button_down

        self.moveArr = 1
        self.arr = [-.78, 0, .78]

        # self.disableMouse()

        self.taskMgr.add(self.update, "update")
        self.taskMgr.add(self.del_obstacle, "del_obstacle")

        # self.obst1y = self.obstacle1.getPos().y
        # self.obst2y = self.obstacle2.getPos().y

    def spawn_obstacle(self):
        self.obs = Obstacle(Vec3(self.arr[0], 50, -0.74), 0, 100, self.render, self)
        self.taskMgr.add(self.obs.update, "update_obs")

    def obstacle_movement(self):
        pass

    def update(self, task):
        self.arr = self.calc.random_choice(self.arr, 1)
        self.spawn_obstacle()
        return task.cont

    def del_obstacle(self, task):
        if len(self.obstacle_arr) > 6:
            self.obstacle_arr.remove(self.obstacle_arr[len(self.obstacle_arr) - 1])
        print(len(self.obstacle_arr))
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