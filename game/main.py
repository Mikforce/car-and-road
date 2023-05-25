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

        # Flag for creating 1 obstacle
        self.obstacle_spawned = False

        self.calc = Calculations()
        # Nodes
        self.node = NodePath("PhysicsNode")

        # Actor Node
        self.carActor = ActorNode("car")
        self.obstacleActor = ActorNode("obstacle")

        # Model Init
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.gltf")
        self.obstacle = self.loader.loadModel("models/car.gltf")
        self.car.ls()
        self.obstacle.ls()

        # Attach Node
        self.carActorN = self.node.attachNewNode(self.carActor)
        self.obstacleActorN = self.node.attachNewNode(self.obstacleActor)

        # Texture Init
        self.car_texture = self.loader.loadTexture("sprites/game.png")
        self.obstacle_texture = self.loader.loadTexture("sprites/obstacle.png")

        # Set Texture
        self.car.set_texture(self.car_texture, 1)
        self.obstacle.set_texture(self.obstacle_texture, 1)

        # Reparent To
        self.node.reparentTo(self.render)
        self.scene.reparentTo(self.render)
        self.car.reparentTo(self.carActorN)
        self.obstacle.reparentTo(self.obstacleActorN)

        # Scale
        self.scene.setScale(0.26, 0.26, 10)
        self.car.setScale(0.25, 0.25, 0.25)
        self.obstacle.setScale(0.25, 0.25, 0.25)
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
        self.arr = [-0.78, 0, 0.78]

    # Spawn new obstacles
    def spawn(self):
        self.obstacle_new = self.loader.loadModel("models/car.gltf")
        self.obstacle_new.ls()
        self.obstacle_new.set_texture(self.obstacle_texture, 1)
        self.obstacle_new.reparentTo(self.obstacleActorN)
        self.obstacle_new.setScale(0.25, 0.25, 0.25)

    # Spawn obstacles in front of the car (random road)
    def spawn_obstacle(self):
        x_car, y_car, z_car = self.car.getPos()
        self.spawn()
        # Spawn the appearance of obstacles in front of the car (random road)
        spawn = (random.choice(self.arr), y_car + 25, z_car)
        self.obstacle_new.setPos(spawn)

    def del_obstacle(self):
        # Function unfinished
        ...

    # Input buttons
    def input(self):
        if self.is_down("a"):
            self.movement(-0.74)
        elif self.is_down("d"):
            self.movement(0.74)

    # Movement after pressing the button
    def movement(self, movement_x: float):
        x, y, z = self.car.getPos()
        match movement_x + round(x, 2):
            case -0.74 | 0 | 0.74:
                self.car.setPos(movement_x + x, y + 0.5, -0.74)

    # Car movement and created obstacle
    def run_car(self, task):
        x, y, z = self.car.getPos()
        # Car movement
        self.car.setPos(x, y + 0.05, z)

        # An obstacle is created every 10 coordinates y
        if int(y) % 10 == 0 and not self.obstacle_spawned:
            self.obstacle_spawned = True
            self.spawn_obstacle()
        if int(y) % 10 != 0:
            self.obstacle_spawned = False
        return Task.cont


if __name__ == '__main__':
    game = Game()
    # Adding tasks to the car_run queue
    game.taskMgr.add(game.run_car, "run_car")
    # Start game
    game.run()