from panda3d.core import Vec3, Vec2, NodePath
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionSphere, CollisionNode
import random
import calc as calc_
class GameObject:
    def __init__(self, pos: Vec3, render, model):
        # Obstacle's object
        self.actor = Actor(model)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)

class Obstacle(GameObject):
    def __init__(self, pos: Vec3, speed: int, chance_to_spawn: int, collider_name, render, model):
        super().__init__(pos=pos, render=render, model=model)
        self.speed = speed
        if calc_.Calculations.check_chance(chance_to_spawn):
            self.type = "Money"
        else:
            self.type = "Obstacle"

