import pygame
from constants import colors, screen_dimensions, n_cells_x, n_cells_y, cell_width, cell_height


class Draw:
    def grid(self, screen):
        for y in range(0, screen_dimensions["height"], cell_height):
            for x in range(0, screen_dimensions["width"], cell_width):
                cell = pygame.Rect(x, y, cell_width, cell_height)
                pygame.draw.rect(screen, colors["gray"], cell, 1)

    def cells(self, screen, game_state):
        for y in range(n_cells_y):
            for x in range(n_cells_x):
                cell = create_cell(x, y)
                if game_state[x, y] == 1:
                    pygame.draw.rect(screen, colors["black"], cell)


def create_cell(x, y):
    return pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)