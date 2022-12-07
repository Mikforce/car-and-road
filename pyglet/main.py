import pyglet

window = pyglet.window.Window()

class Game():
    def __init__(self):
        self.image = pyglet.resource.image("\Asset\Images\images.jpeg")

    @window.event
    def on_draw(self):
        window.clear()
        self.image.blit(0, 0)

    def run(self):
        pyglet.app.run()


if __name__ == "__main__":
    game = Game()
    game.run()