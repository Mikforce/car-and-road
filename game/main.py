# Other functions
import random

from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from panda3d.physics import *

import datetime
# My functions

from panda3dfunctions import *
from entities import *


# Game Class
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.real_time = datetime.datetime.now()
        # Flag for creating 1 obstacle
        self.obstacle_spawned = False

        # Nodes
        self.node = NodePath("PhysicsNode")

        # Actor Node
        self.carActor = ActorNode("car")
        self.obstacleActor = ActorNode("obstacle")

        # Model Init
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.gltf")
        self.car.ls()
        # Attach Node
        self.carActorN = self.node.attachNewNode(self.carActor)
        self.obstacleActorN = self.node.attachNewNode(self.obstacleActor)

        # Texture Init
        self.car_texture = self.loader.loadTexture("sprites/game.png")
        self.obstacle_texture = self.loader.loadTexture("sprites/obstacle.png")

        # Set Texture
        self.car.set_texture(self.car_texture, 1)

        # Reparent To
        self.node.reparentTo(self.render)
        self.scene.reparentTo(self.render)
        self.car.reparentTo(self.carActorN)

        # Scale
        self.scene.setScale(0.26, 0.26, 10)
        self.car.setScale(0.25, 0.25, 0.25)
        # Pos
        self.scene.setPos(0, 6.5, -1)
        self.car.setPos(0, -110, -0.74)
        # Rotation
        self.car.setHpr(90, 0, 90)
        self.scene.setHpr(90, 0, 90)

        # Buttons
        self.accept("d", self.input)
        self.accept("a", self.input)

        self.obstacle_arr = []

        self.is_down = self.mouseWatcherNode.is_button_down

        # The speed of the obstacle
        self.speed = 0.55
        # Coordinates of the road by x
        self.arr = [-0.78, 0, 0.78]

    # Spawn new obstacles
    def spawn(self):
        x_car, y_car, z_car = self.car.getPos()
        self.obstacle = self.loader.loadModel("models/car.gltf")
        self.obstacle.set_texture(self.obstacle_texture, 1)
        self.obstacle.reparentTo(self.obstacleActorN)
        self.obstacle.setScale(0.25, 0.25, 0.25)
        self.obstacle_arr.append(self.obstacle)
        # Spawn the appearance of obstacles in front of the car (random road)
        self.obstacle.setPos(random.choice(self.arr), y_car + 200, z_car)

    # Spawn obstacles in front of the car (random road)

    def del_obstacle(self, obstacle):
        obstacle.removeNode()
        self.obstacle_arr.remove(obstacle)

    # Input buttons
    def input(self):
        if self.is_down("a"):
            self.movement(self.arr[0])
        elif self.is_down("d"):
            self.movement(self.arr[2])

    # Movement after pressing the button
    def movement(self, movement_x: float):
        x, y, z = self.car.getPos()
        # The car cannot go off the road
        match movement_x + round(x, 2):
            # Magic numbers from self.arr
            case -0.78 | 0 | 0.78:
                self.car.setPos(movement_x + x, y, self.arr[0])

    # Movement of all obstacles
    def move_obstacles(self):
        x_car, y_car, z_car = self.car.getPos()
        if len(self.obstacle_arr) != 0:
            for obstacle in self.obstacle_arr:
                x_obstacle, y_obstacle, z_obstacle = obstacle.getPos()
                # Movement of each obstacle
                obstacle.setPos(x_obstacle, y_obstacle - self.speed, z_obstacle)

                # If an obstacle is out of sight,
                # then it is removed from the array of obstacles on the road
                if y_car - 10 >= y_obstacle:
                    self.del_obstacle(obstacle)

    # Camera movement behind the typewriter
    def move_camera(self):
        x_car, y_car, z_car = self.car.getPos()
        self.camera.setPos(x_car, y_car - 10, z_car + 2)
        self.camera.setHpr(0, 0, 0)

    # Creating new obstacles on the road
    def spawn_obstacles(self):
        # Create new obstacles every 0.5 seconds
        if (datetime.datetime.now() - self.real_time).total_seconds() >= 0.5:
            # Updating the obstacle spawn timer
            self.real_time = datetime.datetime.now()
            # Self.obstacle_spawned - check for the correct spawn
            if not self.obstacle_spawned:
                self.obstacle_spawned = True
                # Creating two new obstacles
                self.spawn()
                self.spawn()
            else:
                self.obstacle_spawned = False

        # Controlling the movement of the car, camera and obstacles on the road
    def start_game(self, task):
        # Move all the obstacles on the road
        self.move_obstacles()
        # Camera movement behind the typewriter
        self.move_camera()
        # Creating new obstacles on the road
        self.spawn_obstacles()
        return Task.cont


if __name__ == '__main__':
    game = Game()
    # Adding tasks to the car_run queue
    game.taskMgr.add(game.start_game, "start_game")
    # Start game
    game.run()