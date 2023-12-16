import numpy as np


class GameState:
    def __init__(self, grid_size_x, grid_size_y):
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.state = self.initialize_state(grid_size_x, grid_size_y)

    @staticmethod
    def initialize_state(grid_size_x, grid_size_y):
        state = np.random.choice([0, 1], size=(grid_size_x, grid_size_y), p=[0.8, 0.2])
        return state

    def update_cell(self, x, y):
        self.state[x, y] = not self.state[x, y]

    def create_new_generation_from_previous_state(self):
        new_state = np.copy(self.state)

        for y in range(self.grid_size_y):
            for x in range(self.grid_size_x):
                n_neighbors = self.state[(x - 1) % self.grid_size_x, (y - 1) % self.grid_size_y] + \
                              self.state[x % self.grid_size_x, (y - 1) % self.grid_size_y] + \
                              self.state[(x + 1) % self.grid_size_x, (y - 1) % self.grid_size_y] + \
                              self.state[(x - 1) % self.grid_size_x, (y) % self.grid_size_y] + \
                              self.state[(x + 1) % self.grid_size_x, (y) % self.grid_size_y] + \
                              self.state[(x - 1) % self.grid_size_x, (y + 1) % self.grid_size_y] + \
                              self.state[x % self.grid_size_x, (y + 1) % self.grid_size_y] + \
                              self.state[(x + 1) % self.grid_size_x, (y + 1) % self.grid_size_y]

                if self.state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif self.state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1

        self.state = new_state
        return self.state