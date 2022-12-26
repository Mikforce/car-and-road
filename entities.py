from panda3d.core import Vec3, Vec2
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionSphere, CollisionNode
import random

class GameObject():
    def __init__(self, pos: Vec3, speed: float, chance_to_spawn_type: int, collider_name, render, model):
        # Obstacle's object
        self.actor = Actor(model)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)
        self.type = None
        # Speed
        self.speed = speed

    def movement(self, speed):
        self.actor.setPos(self.actor.getPos().x - speed, self.actor.getPos().y, self.actor.getPos().z)

    def update(self):
        self.movement(self.speed)

    def spawn_type(self):
        pass

class Obstacle(GameObject, ShowBase):
    def __init__(self, pos, speed, chance_to_spawn, collider_name, render):
        self.model = self.loader.loadModel("")
        GameObject.__init__(self, pos, speed, chance_to_spawn, collider_name, render, self.model)
