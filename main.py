import math as m

from GUI import Maze, Window


WIDTH_PX: int = 800  # x
HEIGHT_PX: int = 600  # y


def main() -> None:
    num_rows = 10
    num_cols = 10
    margin = 50
    cell_size_x: int = m.floor((WIDTH_PX - 2 * margin) / num_cols)
    cell_size_y: int = m.floor((HEIGHT_PX - 2 * margin) / num_rows)

    win = Window(WIDTH_PX, HEIGHT_PX)
    maze = Maze(
        margin,
        margin,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=0,
    )
    # maze.solve()

    win.wait_for_close()


def cli(): ...


if __name__ == "__main__":
    main()
