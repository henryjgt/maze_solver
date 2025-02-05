import math as m

from GUI import Maze, Window


WIDTH_PX: int = 700  # x, x=0 @ top left
HEIGHT_PX: int = 700  # y, y=0 @ top left
MARGIN: int = 50
GRID_SIZE: int = 15  # no. cols & rows


def main() -> None:
    win = Window(WIDTH_PX, HEIGHT_PX)
    cell_size_x: int = m.floor((WIDTH_PX - 2 * MARGIN) / GRID_SIZE)  # no. cols
    cell_size_y: int = m.floor((HEIGHT_PX - 2 * MARGIN) / GRID_SIZE)  # no. rows
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


def cli(): ...


if __name__ == "__main__":
    main()
