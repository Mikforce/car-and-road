from panda3d.core import Vec3, Vec2
from direct.actor.Actor import Actor
from panda3d.core import CollisionSphere, CollisionNode

class GameObject():
    def __init__(self, pos, speed, chance_to_spawn):
        self.actor = Actor("")

class Obstacle(GameObject):
    pass