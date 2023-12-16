import pygame

from time import sleep
from Draw import Draw
from Button import Button
from GameState import GameState
from constants import colors, screen_dimensions, n_cells_x, n_cells_y, cell_width, cell_height

button_width, button_height = 200, 50
button_x, button_y = (screen_dimensions["width"] - button_width) // 2, screen_dimensions[
    "height"] - button_height - 10


def button_factory(color, text):
    return Button(button_x, button_y, button_width, button_height, color, text, 36)


def game_state_factory():
    return GameState(n_cells_x, n_cells_y)


tick = 1
#True - next generation on click, False - next generation on tick
use_button = False

def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_dimensions["width"], screen_dimensions["height"]))
    game_state = game_state_factory()
    draw = Draw()

    running = True
    while running:
        screen.fill(colors["white"])
        draw.grid(screen)
        draw.cells(screen, game_state.state)
        button = button_factory(colors["green"], "Next Generation")
        if use_button:
            button.draw(screen=screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event):
                    if use_button:
                        game_state.create_new_generation_from_previous_state()
                else:
                    x, y = event.pos[0] // cell_width, event.pos[1] // cell_height
                    game_state.update_cell(x, y)

        if not use_button:
            sleep(tick)
            game_state.create_new_generation_from_previous_state()

    pygame.quit()


if __name__ == "__main__":
    main()