# Other functions

from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from panda3d.physics import *

import datetime
# My functions
from calc import *
from panda3dfunctions import *
from entities import *


# Game Class
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.real_time = datetime.datetime.now()
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

        self.moveArr = 1
        self.list_obstacles = []

        # Coordinates of the road by x
        self.arr = [-0.78, 0, 0.78]

    # Spawn new obstacles
    def spawn(self):
        self.obstacle_new = self.loader.loadModel("models/car.gltf")
        self.obstacle_new.ls()
        self.obstacle_new.set_texture(self.obstacle_texture, 1)
        self.obstacle_new.reparentTo(self.obstacleActorN)
        self.obstacle_new.setScale(0.25, 0.25, 0.25)
        self.list_obstacles.append(self.obstacle_new)

    # Spawn obstacles in front of the car (random road)
    def spawn_obstacle(self):
        x_car, y_car, z_car = self.car.getPos()
        self.spawn()

        # Spawn the appearance of obstacles in front of the car (random road)
        random_road = (random.choice(self.arr), y_car + 200, z_car)
        self.obstacle_new.setPos(random_road)

    def del_obstacle(self, obstacle):
        obstacle.removeNode()
        self.list_obstacles.remove(obstacle)

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

    # Moving obstacles, not a car
    def run_car(self, task):
        x_car, y_car, z_car = self.car.getPos()

        # The length comparison is needed for the first run
        if len(self.list_obstacles) != 0:
            for obstacle in self.list_obstacles:
                x, y, z = obstacle.getPos()
                # Speed obstacle
                obstacle.setPos(x, y - 0.5, z)

                # Removes an obstacle when it disappears from view
                if y_car - 10 >= y:
                    self.del_obstacle(obstacle)

        # Camera movement
        self.camera.setPos(x_car, y_car - 10, z_car + 2)
        # Blocking camera rotation
        self.camera.setHpr(0, 0, 0)

        # An obstacle is created every 0.5 second
        if (datetime.datetime.now() - self.real_time).total_seconds() >= 0.5:
            # Updating the spawn timer
            self.real_time = datetime.datetime.now()
            # Self.obstacle_spawned - check for the correct spawn
            if not self.obstacle_spawned:
                self.obstacle_spawned = True
                # Spawn 2 obstacle
                self.spawn_obstacle()
                self.spawn_obstacle()
            else:
                self.obstacle_spawned = False
        return Task.cont


if __name__ == '__main__':
    game = Game()
    # Adding tasks to the car_run queue
    game.taskMgr.add(game.run_car, "run_car")
    # Start game
    game.run()