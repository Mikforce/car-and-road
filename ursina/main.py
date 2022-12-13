from ursina import *

class Game(Ursina):
    def __init__(self):
        super().__init__()
        self.window_size = (1600, 720)
        self.fullscreen = False

    def create_map(self):
        pass

    def new_game(self):
        self.create_map()

    def update(self):
        pass

    def input(self, key):
        pass

if __name__ == '__main__':
    game = Game()
    update = game.update
    game.run()