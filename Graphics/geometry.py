import tkinter as tk
from typing import Optional, Tuple


class Point:

    __errmsg: str = "Points must lie within the size limit of the window"

    def __init__(self, x: int, y: int, window_size: Optional[Tuple] = None) -> None:
        self._x: int = x
        self._y: int = y

        if window_size and not (0 < x < window_size[0] or 0 < y < window_size[1]):
            raise ValueError(self.__errmsg)

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y


class Line:

    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1: Point = p1
        self.p2: Point = p2

    def draw(self, canvas: tk.Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Box:

    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        self._top_left_x: int = top_left.x
        self._top_left_y: int = top_left.y
        self._bottom_right_x: int = bottom_right.x
        self._bottom_right_y: int = bottom_right.y

        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
