from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode
from direct.gui.DirectGui import *
base = ShowBase()


class Car:
    def __init__(self):
        self.font = loader.loadFont('fonts/PixeloidMono-1G8ae.ttf')
        self.title = OnscreenText(
            text="C-A-R",
            fg=(255, 0, 0, 1), scale=.15, font=self.font, parent=base.a2dpTopCenter, align=TextNode.A_center, pos=(0, -0.15))
        base.setBackgroundColor(0, 0, 0)
        base.disableMouse()
        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0)
        self.size_scale = 0.6
        self.orbitscale = 10

        self.load_models()

    def load_models(self):
        self.sun = loader.loadModel("models/planet")
        self.sun.reparentTo(render)
        self.sun_tex = loader.loadTexture("models/sun_tex.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.setScale(2 * self.size_scale)


c = Car()
# As usual - run() must be called before anything can be shown on screen
base.run()
