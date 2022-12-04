import pygame
import sys
from button import Button
from typing import Union, Tuple


class GUI:
    def __init__(self):
        pygame.init()
        self.window_size = (1200, 800)
        self.screen = pygame.display.set_mode(self.window_size)
        self.screen_rect = self.screen.get_rect()
        self.buttons = []
        self.background_img = pygame.image.load('images/C-A-R_Background.png')
        self.bg_rect = self.background_img.get_rect()
        self.running = True

    @staticmethod
    def draw_text(text: str, font: pygame.font.Font, color: Union[str, Tuple[int, int, int]], surface: pygame.Surface, x: float, y: float):
        text_obg = font.render(text, True, color)
        text_rect = text_obg.get_rect()
        text_rect.center = x
        text_rect.top = y + 20
        surface.blit(text_obg, text_rect)

    def update(self):
        self.screen.blit(self.background_img, self.bg_rect)
        [button.draw_button() for button in self.buttons]
        pygame.display.update()
        pygame.display.flip()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                self.check_mouse_events(x, y)
            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.running = False

    def check_mouse_events(self, x: float, y: float):
        button_clicked = {}
        for button in self.buttons:
            button_clicked.update({button: button.rect.collidepoint(x, y)})
            self.checking_clicks(button_clicked)

    def checking_clicks(self, button_clicked):
        pass

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.event_handler()


class MainMenu(GUI):
    def __init__(self):
        super().__init__()
        self.title_font = pygame.font.Font('fonts/PixeloidMono-1G8ae.ttf', 100)
        self.title_font.bold = True
        self.options = Options()
        self.buttons = {
            'start_button': {'rect': pygame.Rect(self.screen_rect.centerx - 100,
                                                 self.screen_rect.centery - 150, 200, 50),
                             'text': 'Начать игру'},
            'options_button': {'rect': pygame.Rect(self.screen_rect.centerx - 100,
                                                   self.screen_rect.centery - 50, 200, 50),
                               'text': 'Настройки'},
            'quit_button': {'rect': pygame.Rect(self.screen_rect.centerx - 100, self.screen_rect.centery + 50, 200, 50),
                            'text': 'Выйти из игры'}
        }
        self.buttons = [Button(self.screen, self.buttons[button]['rect'], 'purple', self.buttons[button]['text'], 'yellow')
                        for button in self.buttons]

    def update(self):
        self.screen.blit(self.background_img, self.bg_rect)
        self.draw_text('C-A-R', self.title_font, 'purple', self.screen, self.screen_rect.center, self.screen_rect.top)
        [button.draw_button() for button in self.buttons]
        pygame.display.update()
        pygame.display.flip()

    def checking_clicks(self, button_clicked):
        for button in button_clicked:
            if button_clicked[button] and button.text_str == 'Выйти из игры':
                sys.exit()
            elif button_clicked[button] and button.text_str == 'Настройки':
                self.options.run()


class Options(GUI):
    def __init__(self):
        super().__init__()
        self.buttons = [Button(self.screen, pygame.Rect(50, 50, 300, 50), 'purple', 'Вернуться назад', 'yellow')]

    def checking_clicks(self, button_clicked):
        for button in button_clicked:
            if button_clicked[button] and button.text_str == 'Вернуться назад':
                self.running = False
                MainMenu().run()
