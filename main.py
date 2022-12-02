# Import moduls
import sys
import pygame


# Classes
class Game:  # Game's class
    def __init__(self):  # Game's initialization
        pygame.init()  # Pygame's initialization
        self.window_size = (1200, 800)  # Window size
        self.screen = pygame.display.set_mode(self.window_size)  # Screen
        pygame.display.set_caption("car and road")

    def update(self):  # Update the game
        self.screen.fill('white')
        pygame.display.update()
        pygame.display.flip()

    @staticmethod
    def event_handler():  # Check Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while True:
            self.update()
            self.event_handler()


if __name__ == '__main__':
    game = Game()
    game.run()  # Game's run
