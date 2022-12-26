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
        self.actor = Actor(model)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)

class Obstacle(GameObject):
    def __init__(self, pos: Vec3, speed: int, chance_to_spawn: int, render):
        self.speed = speed
        if calc_.Calculations.check_chance(chance_to_spawn):
            self.type = "Money"
        else:
            self.type = "Obstacle"

        match self.type:
            case "Obstacle":
                self.model = p3f.panda3dFunc.load_model("car.gltf")
            case "Money":
                self.model =

        super().__init__(pos=pos, render=render, model=self.model)

