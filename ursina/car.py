from ursina import *

class Car(Ursina):
    def __init__(self):
        super().__init__()
        self.car = Entity(model='cube', position=(0, 1, 0), collider='mesh', collision=True)
