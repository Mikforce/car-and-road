from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from panda3d.physics import *
import random
from calc import *

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.calc = Calculations
        self.base = ShowBase
        self.base.enableParticles(self)
        self.gravityForce = LinearVectorForce(0, 0, -9.81/10)  # gravity acceleration
        self.base.physicsMgr.addLinearForce(self.gravityForce)

        # Nodes
        self.node = NodePath("PhysicsNode")

        # Actor Node
        self.carActor = ActorNode("car")

        # Model Init
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.gltf")
        self.obstacle1 = self.loader.loadModel("models/car.gltf")
        self.obstacle2 = self.loader.loadModel("models/car.gltf")
        self.obstacle3 = self.loader.loadModel("models/car.gltf")
        self.obstacle4 = self.loader.loadModel("models/car.gltf")
        self.obstacle5 = self.loader.loadModel("models/car.gltf")
        self.obstacle6 = self.loader.loadModel("models/car.gltf")
        self.car.ls()

        # Attach Node
        self.carActorN = self.node.attachNewNode(self.carActor)

        # Texture Init
        self.car_texture = self.loader.loadTexture("sprites/game.png")

        # Set Texture
        self.car.set_texture(self.car_texture, 1)

        # Self
        self.base.physicsMgr.attachPhysicalNode(self.carActor)

        #Reparent To
        self.node.reparentTo(self.render)
        self.scene.reparentTo(self.render)
        self.car.reparentTo(self.carActorN)
        self.obstacle1.reparentTo(self.render)
        self.obstacle2.reparentTo(self.render)
        self.obstacle3.reparentTo(self.render)
        self.obstacle4.reparentTo(self.render)
        self.obstacle5.reparentTo(self.render)
        self.obstacle6.reparentTo(self.render)

        # Scale
        self.scene.setScale(0.26, 0.26, 10)
        self.car.setScale(0.25, 0.25, 0.25)
        self.obstacle1.setScale(0.25, 0.25, 0.25)
        self.obstacle2.setScale(0.25, 0.25, 0.25)
        self.obstacle3.setScale(0.25, 0.25, 0.25)
        self.obstacle4.setScale(0.25, 0.25, 0.25)
        self.obstacle5.setScale(0.25, 0.25, 0.25)
        self.obstacle6.setScale(0.25, 0.25, 0.25)

        # Pos
        self.scene.setPos(0, 6.5, -1)
        self.car.setPos(0, 6.5, -0.74)

        # Rotation
        self.car.setHpr(90, 0, 90)
        self.scene.setHpr(90, 0, 90)

        # Buttons
        self.accept('a', self.input)
        self.accept('d', self.input)
        self.accept('r', self.spawn_obstacle)

        # Collision
        self.carCol = self.car.attachNewNode(CollisionNode('colNode'))
        self.carCol.node().addSolid(CollisionBox(0, 0, 0, 1))
        self.ColMan = CollisionHandlerPusher()
        self.ColMan.addCollider(self.carCol, self.car)

        self.is_down = self.mouseWatcherNode.is_button_down

        self.moveArr = 1
        self.arr = [-.78, 0, .78]

        # self.disableMouse()

        self.taskMgr.add(self.update, "update")

        self.obst1y = self.obstacle1.getPos().y
        self.obst2y = self.obstacle2.getPos().y

        self.spawn_obstacle()

        # Physics
        self.carActor.getPhysicsObject().setMass(136.077)
    def spawn_obstacle(self):
        arr = self.calc.random_choice(self, self.arr, 6)
        self.obstacle1.setPos(arr[0], 50, -0.74)
        self.obstacle2.setPos(arr[1], 50, -0.74)
        self.obstacle3.setPos(arr[2], 70, -0.74)
        self.obstacle4.setPos(arr[3], 70, -0.74)
        self.obstacle5.setPos(arr[4], 90, -0.74)
        self.obstacle6.setPos(arr[5], 90, -0.74)

    def obstacle_movement(self):
        self.obstacle1.setPos(self.obstacle1.getPos().x, self.obstacle1.getPos().y - 1, -0.74)
        self.obstacle2.setPos(self.obstacle2.getPos().x, self.obstacle2.getPos().y - 1, -0.74)
        self.obstacle3.setPos(self.obstacle3.getPos().x, self.obstacle3.getPos().y - 1, -0.74)
        self.obstacle4.setPos(self.obstacle4.getPos().x, self.obstacle4.getPos().y - 1, -0.74)
        self.obstacle5.setPos(self.obstacle5.getPos().x, self.obstacle5.getPos().y - 1, -0.74)
        self.obstacle6.setPos(self.obstacle6.getPos().x, self.obstacle6.getPos().y - 1, -0.74)

    def update(self, task):
        if self.obstacle6.getPos().y > 0:
            self.obstacle_movement()
            return task.cont
        else:
            self.spawn_obstacle()
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