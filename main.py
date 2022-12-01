# Import moduls
import pygame

# Classes
class Game: # Game's class
    def __init__(self): # Game's initialization
        super().__init__()
        pygame.init() # Pygame's initialization
        self.window_size = (1200, 800) # Window size
        self.screen = pygame.display.set_mode(self.window_size) # Screen

    def update(self): # Update the game
        self.screen.fill((0, 0, 0))
        self.event_handler()
        pygame.display.flip()
    def event_handler(self): # Check Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def run(self):
        while True:
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run() # Game's run