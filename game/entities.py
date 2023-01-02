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
        self.actor = Actor("car.egg", {"walk": "models/car.egg"})
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
                self.model = "models/car.egg"
            case "Money":
                self.model = "models/car.egg"

        GameObject.__init__(self=self, pos=pos, render=render, model=self.model)

        self.actor.setScale(0.25, 0.25, 0.25)


    def update(self, task):
        y = self.pos.y - 1
        self.actor.setPos(self.pos.x, y, self.pos.z)
        return task.cont

