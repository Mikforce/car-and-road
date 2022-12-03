import pygame
from typing import Union, Tuple


class Button:
    def __init__(self, screen: pygame.Surface, rect: pygame.Rect,
                 bg_color: Union[str, Tuple[int, int, int]], text: str = None, text_color: Union[str, Tuple[int, int, int]] = None):
        pygame.init()
        self.screen = screen
        self.rect = rect
        self.bg_color = bg_color
        if text is not None:
            self.text_str = text
            self.font = pygame.font.Font('fonts/PixeloidSansBold-RpeJo.ttf', 20)
            self.font.italic = False
            self.font.bold = True
            self.text = self.font.render(text, True, text_color, bg_color)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = self.rect.center

    def centering_button(self):
        self.rect.center = self.screen.get_rect().center

    def draw_button(self):
        self.screen.fill(self.bg_color, self.rect)
        if self.text is not None:
            self.screen.blit(self.text, self.text_rect)
