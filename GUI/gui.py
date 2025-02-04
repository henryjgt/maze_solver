import math as m
import tkinter as tk

from Graphics import Box, Line, Point
from Graphics import line_constructor


class Window:

    def __init__(self, width: int, height: int) -> None:
        self._width: int = width
        self._height: int = height
        self.__running: bool = False

        self.__root = tk.Tk()
        self.__root.title("DEMO GUI")
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


class Cell(Box):
    def __init__(self, top_left: Point, top_right: Point, window: Window) -> None:
        super().__init__(top_left, top_right)
        self._window: Window = window

    def draw(self) -> None:

        if self.has_left_wall:
            _p1 = Point(self._top_left_x, self._top_left_y)
            _p2 = Point(self._top_left_x, self._bottom_right_y)
            self._window.draw_line(line_constructor(_p1, _p2))

        if self.has_right_wall:
            _p1 = Point(self._bottom_right_x, self._top_left_y)
            _p2 = Point(self._bottom_right_x, self._bottom_right_y)
            self._window.draw_line(line_constructor(_p1, _p2))

        if self.has_bottom_wall:
            _p1 = Point(self._top_left_x, self._bottom_right_y)
            _p2 = Point(self._bottom_right_x, self._bottom_right_y)
            self._window.draw_line(line_constructor(_p1, _p2))

        if self.has_top_wall:
            _p1 = Point(self._top_left_x, self._top_left_y)
            _p2 = Point(self._bottom_right_x, self._top_left_y)
            self._window.draw_line(line_constructor(_p1, _p2))

    def draw_move(self, to_cell: "Cell", undo=False) -> None:
        color: str = "red" if not undo else "gray"

        # fmt: off
        x_centre: int = m.floor(0.5 * (self._bottom_right_x - self._top_left_x))
        y_centre: int = m.floor(0.5 * (self._bottom_right_y - self._top_left_y))
        self._centre = Point(x_centre, y_centre)

        target_x_centre: int = m.floor(0.5 * (to_cell._bottom_right_x - to_cell._top_left_x))
        target_y_centre: int = m.floor(0.5 * (to_cell._bottom_right_y - to_cell._top_left_y))
        _target_centre = Point(target_x_centre, target_y_centre)
        # fmt: on

        self._window.draw_line(line_constructor(self._centre, _target_centre, color))


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Window,
    ) -> None:
        self.x1: int = x1
        self.y1: int = y1
        self.num_rows: int = num_rows
        self.num_cols: int = num_cols
        self.cell_size_x: int = cell_size_x
        self.cell_size_y: int = cell_size_y
        self._window: Window = window

    def _create_cells(self): ...

    def _draw_cell(self): ...

    def _animate(self): ...


if __name__ == "__main__":
    win = Window(800, 600)

    c1 = Cell(Point(100, 100), Point(400, 400), win)
    c1.draw()

    c2 = Cell(Point(200, 200), Point(500, 500), win)
    c2.draw()

    win.wait_for_close()
