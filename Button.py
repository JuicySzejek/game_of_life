import pygame
from constants import colors


class Button:
    def __init__(self, x, y, width, height, color, text, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.text = text
        self.font_size = font_size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, True, colors["black"])
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text, text_rect)

    def is_clicked(self, event):
        is_x_axis_overlapping = self.x <= event.pos[0] <= self.x + self.width
        is_y_axis_overlapping = self.y <= event.pos[1] <= self.y + self.height
        return is_x_axis_overlapping and is_y_axis_overlapping