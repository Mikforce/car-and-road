from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.physics import *

base = ShowBase()

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Model Init
        self.scene = self.loader.loadModel("models/roads2.obj")
        self.car = self.loader.loadModel("models/car.gltf")
        self.car.ls()

        # Texture Init
        self.car_texture = self.loader.loadTexture("sprites/game.png")

        # Set Texture
        self.car.set_texture(self.car_texture, 1)

        # ReparentTo
        self.scene.reparentTo(self.render)
        self.car.reparentTo(self.render)

        # Scale
        self.scene.setScale(0.26, 0.26, 5)
        self.car.setScale(0.25, 0.25, 0.25)
        # Pos
        self.scene.setPos(0, 6.5, -1)
        self.car.setPos(0, 6.5, -0.74)
        # Rotation
        self.car.setHpr(90, 0, 90)
        self.scene.setHpr(90, 0, 90)

        # Buttons
        self.d_button = map.get_mapped_button("d")
        self.a_button = map.get_mapped_button("a")
    @staticmethod
    def update(self):
        while True:
            self.input()
    def input(self):
        if base.mouseWatcherNode.is_button_down(self.d_button):
            self.movement(1)
        if base.mouseWatcherNode.is_button_down(self.a_button):
            self.movement(-1)

    def movement(self, x):
        print(x)

if __name__ == '__main__':
    game = Game()
    game.run()

