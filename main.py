import math

from graphics import Maze, Window


WIDTH_PX: int = 700   # x=0 @ top left
HEIGHT_PX: int = 700  # y=0 @ top left
MARGIN: int = 50
GRID_SIZE: int = 15   # no. cols & rows


def main() -> None:
    win = Window(WIDTH_PX, HEIGHT_PX)
    cell_size_x: int = math.floor((WIDTH_PX - 2 * MARGIN) / GRID_SIZE)   # no. cols
    cell_size_y: int = math.floor((HEIGHT_PX - 2 * MARGIN) / GRID_SIZE)  # no. rows
    maze = Maze(
        MARGIN,
        MARGIN,
        GRID_SIZE,
        GRID_SIZE,
        cell_size_x,
        cell_size_y,
        window=win,
        # seed=0,
    )
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
