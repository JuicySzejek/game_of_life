colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "gray": (128, 128, 128),
    "green": (0, 255, 0),
}

screen_dimensions = {
    "width": 800,
    "height": 600,
}
# Grid dimensions
n_cells_x, n_cells_y = 40, 30
cell_width = screen_dimensions["width"] // n_cells_x
cell_height = screen_dimensions["height"] // n_cells_y