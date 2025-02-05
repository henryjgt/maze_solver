import random
import time
import tkinter as tk
from typing import Optional

from Graphics import Square, Line, Point


class Window:
    def __init__(self, width: int, height: int) -> None:
        self._width: int = width
        self._height: int = height
        self.__running: bool = False
        self.__root = tk.Tk()
        self.__root.title("Python Maze Solver")
        self.__canvas = tk.Canvas(width=width, height=height)
        self.__canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running: bool = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running: bool = False

    def draw_line(self, line: Line, fill_color: str = "black") -> None:
        line.draw(self.__canvas, fill_color)

    def delete_line(self, line: Line) -> None:
        line.delete(self.__canvas)


class Cell(Square):
    def __init__(
        self,
        top_left: Point,
        bottom_right: Point,
        window: Optional[Window] = None,
    ) -> None:

        super().__init__(top_left, bottom_right)
        self._window: Optional[Window] = window
        self._visited = False

    def draw(self) -> None:
        if not isinstance(self._window, Window):
            return
        if self.has_left_wall:
            self._window.draw_line(self.left_wall)
        if self.has_right_wall:
            self._window.draw_line(self.right_wall)
        if self.has_bottom_wall:
            self._window.draw_line(self.bottom_wall)
        if self.has_top_wall:
            self._window.draw_line(self.top_wall)

    def delete_side(self, side: str) -> None:
        if not isinstance(self._window, Window):
            return

        match side:
            case "top":
                if self.has_top_wall:
                    self._window.delete_line(self.top_wall)
                    self.has_top_wall = False
            case "left":
                if self.has_left_wall:
                    self._window.delete_line(self.left_wall)
                    self.has_left_wall = False
            case "right":
                if self.has_right_wall:
                    self._window.delete_line(self.right_wall)
                    self.has_right_wall = False
            case "bottom":
                if self.has_bottom_wall:
                    self._window.delete_line(self.bottom_wall)
                    self.has_bottom_wall = False

    def draw_move(self, to_cell: "Cell", undo=False) -> None:
        if not isinstance(self._window, Window):
            return
        color: str = "gray" if undo else "red"
        self._window.draw_line(Line(self.centre, to_cell.centre), fill_color=color)

    @property
    def walls(self) -> dict:
        return {
            "left": self.has_left_wall,
            "right": self.has_right_wall,
            "top": self.has_top_wall,
            "bottom": self.has_bottom_wall,
        }

    def has_wall(self, side: str) -> bool:
        return self.walls[side]


class Maze:

    _map_to_target: dict[str, str] = {
        "left": "right",
        "right": "left",
        "top": "bottom",
        "bottom": "top",
    }

    def __init__(
        self,
        x0: int,
        y0: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Optional[Window] = None,
        seed: Optional[int] = None,
    ) -> None:

        self.x0: int = x0
        self.y0: int = y0
        self.num_rows: int = num_rows
        self.num_cols: int = num_cols
        self.cell_size_x: int = cell_size_x
        self.cell_size_y: int = cell_size_y
        self._window: Optional[Window] = window
        self._window_size: Optional[tuple] = None
        if isinstance(self._window, Window):
            self._window_size: Optional[tuple] = (
                self._window.width,
                self._window.height,
            )
        if seed is not None:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        if isinstance(self._window, Window):
            self._animate()

    def _create_cells(self) -> None:
        self._cells: list[list[Cell]] = []
        for col in range(self.num_cols):
            col_cells: list[Cell] = []
            for row in range(self.num_rows):
                cell_top_left_x: int = self.x0 + col * self.cell_size_x
                cell_top_left_y: int = self.y0 + row * self.cell_size_y
                tl_point = Point(cell_top_left_x, cell_top_left_y, self._window_size)
                cell_bottom_right_x: int = cell_top_left_x + self.cell_size_x
                cell_bottom_right_y: int = cell_top_left_y + self.cell_size_y
                br_point = Point(cell_bottom_right_x, cell_bottom_right_y, self._window_size)  # fmt: skip
                col_cells.append(Cell(tl_point, br_point, window=self._window))
            self._cells.append(col_cells)

        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row) -> None:
        cell: Cell = self._cells[col][row]
        cell.draw()
        self._animate(_sleep=None)

    def _animate(self, _sleep: Optional[float] = 0.03) -> None:
        if not isinstance(self._window, Window):
            return
        self._window.redraw()
        if _sleep:
            time.sleep(_sleep)

    def _break_entrance_and_exit(self) -> None:
        if not isinstance(self._window, Window):
            return
        start_cell: Cell = self._cells[0][0]
        start_cell.delete_side("top")
        finish_cell: Cell = self._cells[-1][-1]
        finish_cell.delete_side("bottom")
        self._animate()

    def get_adjacent(self, col, row) -> dict[str, tuple[int, int]]:
        return {
            "left": (col - 1, row),
            "right": (col + 1, row),
            "top": (col, row - 1),
            "bottom": (col, row + 1),
        }

    def _break_walls_r(self, col, row) -> None:
        cell: Cell = self._cells[col][row]
        cell._visited = True
        adjacent_cells: dict[str, tuple[int, int]] = self.get_adjacent(col, row)
        while True:
            unvisited_neighbours: dict[str, Cell] = {}
            for direction, indices in adjacent_cells.items():
                if not (
                    (0 <= indices[0] < self.num_cols)
                    and (0 <= indices[1] < self.num_rows)
                ):
                    continue
                neighbour: Cell = self._cells[indices[0]][indices[1]]
                if not neighbour._visited:
                    unvisited_neighbours.update({direction: neighbour})

            if len(unvisited_neighbours.keys()) <= 0:
                return

            direction: str = random.choice(list(unvisited_neighbours.keys()))
            cell.delete_side(direction)
            next_cell: Cell = unvisited_neighbours[direction]
            next_cell.delete_side(self._map_to_target[direction])
            self._break_walls_r(*adjacent_cells[direction])

    def _reset_cells_visited(self) -> None:
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._cells[col][row]._visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, col, row) -> bool:
        self._animate()
        cell: Cell = self._cells[col][row]
        cell._visited = True
        adjacent_cells: dict[str, tuple[int, int]] = self.get_adjacent(col, row)

        if cell == self._cells[-1][-1]:
            return True

        for direction, indices in adjacent_cells.items():
            if cell.has_wall(direction):
                continue
            if not (
                (0 <= indices[0] < self.num_cols) and (0 <= indices[1] < self.num_rows)
            ):
                continue
            next_cell: Cell = self._cells[indices[0]][indices[1]]
            if not next_cell._visited:
                cell.draw_move(next_cell)
                progress: bool = self._solve_r(indices[0], indices[1])
                if progress:
                    return True
                else:
                    cell.draw_move(next_cell, undo=True)
        else:
            return False
