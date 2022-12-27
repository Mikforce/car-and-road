from panda3d.core import Vec3, Vec2, NodePath
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionSphere, CollisionNode
import random
import calc as calc_
import panda3dfunctions as p3f
class GameObject:
    def __init__(self, pos: Vec3, render, model):
        # Obstacle's object
        self.actor = Actor(model, {"walk": "models/car.gltf"})
        self.actor.reparentTo(render)
        self.actor.setPos(pos)

    def setPos(self, x: float, y: float, z: float):
        self.actor.setPos(x, y, z)

class Obstacle(GameObject):
    def __init__(self, pos: Vec3, speed: int, chance_to_spawn: int, render, showbase):
        self.speed = speed
        if calc_.Calculations.check_chance(chance_to_spawn):
            self.type = "Money"
        else:
            self.type = "Obstacle"

        self.pos = pos

        self.showbase = showbase

        match self.type:
            case "Obstacle":
                self.model = p3f.panda3dFunc.load_model("obstacle.dae", showbase=self.showbase)
            case "Money":
                self.model = p3f.panda3dFunc.load_model("money.gltf", showbase=self.showbase)

        self.model.setScale(0.25, 0.25, 0.25)

        GameObject.__init__(self=self, pos=pos, render=render, model=self.model)

    def update(self, task):
        y = self.pos.y - 1
        self.model.setPos(self.pos.x, y, self.pos.z)
        return task.cont

