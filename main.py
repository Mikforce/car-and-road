import pygame


class Game:
    def __init__(self):
        super().__init__()
        pygame.init()
        self.window_size = (1200, 800)
        self.screen = pygame.display.set_mode(self.window_size)

    def update(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == '__main__':
    game = Game()
    while True:
        game.update()