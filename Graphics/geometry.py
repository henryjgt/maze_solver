import math as m
import tkinter as tk
from typing import Optional, Tuple

from Graphics import line_constructor


class Point:
    def __init__(self, x: int, y: int, window_size: Optional[Tuple] = None) -> None:
        if window_size and not (0 < x < window_size[0] or 0 < y < window_size[1]):
            raise ValueError("Points must lie within the canvas boundaries")

        self.x: int = x
        self.y: int = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1: Point = p1
        self.p2: Point = p2

    def draw(self, canvas: tk.Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Square:
    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True

        self.__top_left_x: int = top_left.x
        self.__top_left_y: int = top_left.y
        self.__bottom_right_x: int = bottom_right.x
        self.__bottom_right_y: int = bottom_right.y

        __x_centre: int = m.floor(0.5 * (self.__bottom_right_x - self.__top_left_x))
        __y_centre: int = m.floor(0.5 * (self.__bottom_right_y - self.__top_left_y))
        self.__centre = Point(__x_centre, __y_centre)

    @property
    def centre(self) -> Point:
        return self.__centre

    @property
    def left_wall(self) -> Line:
        _p1 = Point(self.__top_left_x, self.__top_left_y)
        _p2 = Point(self.__top_left_x, self.__bottom_right_y)
        return line_constructor(_p1, _p2)

    @property
    def right_wall(self) -> Line:
        _p1 = Point(self.__bottom_right_x, self.__top_left_y)
        _p2 = Point(self.__bottom_right_x, self.__bottom_right_y)
        return line_constructor(_p1, _p2)

    @property
    def top_wall(self) -> Line:
        _p1 = Point(self.__top_left_x, self.__top_left_y)
        _p2 = Point(self.__bottom_right_x, self.__top_left_y)
        return line_constructor(_p1, _p2)

    @property
    def bottom_wall(self) -> Line:
        _p1 = Point(self.__top_left_x, self.__bottom_right_y)
        _p2 = Point(self.__bottom_right_x, self.__bottom_right_y)
        return line_constructor(_p1, _p2)
