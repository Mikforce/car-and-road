from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Game(Ursina):
    def __init__(self):
        super().__init__()
        self.window_size = (1600, 720)
        self.fullscreen = False
        self.Light = AmbientLight(color=(255, 255, 255, 1))
        self.new_game()

    def create_map(self):
        self.road = Entity(model=load_model("models/roads2.obj"), texture=load_texture("sprites/game.png"),
                           position=(0, -1, 150), scale=(1, 1, 15), rotation=(0, 0, 90), collider='mesh', collision=True)
        self.car = Entity(model='cube', position=(0, 0, 0), collider='mesh', collision=True)

    def new_game(self):
        self.create_map()

    def update(self):
        pass

    def input(self, key):
        super().input(key)

if __name__ == '__main__':
    game = Game()
    update = game.update
    FirstPersonController()
    Sky()
    game.run()