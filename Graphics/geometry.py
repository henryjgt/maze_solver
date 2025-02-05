import math as m
import tkinter as tk
from typing import Optional


class Point:
    def __init__(self, x: int, y: int, window_size: Optional[tuple] = None) -> None:
        if window_size and not (0 < x < window_size[0] or 0 < y < window_size[1]):
            raise ValueError("Points must lie within the canvas boundaries")

        self.x: int = x
        self.y: int = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1: Point = p1
        self.p2: Point = p2

    def draw(self, canvas: tk.Canvas, fill_color: str) -> None:
        self._id: int = canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2,
        )

    def delete(self, canvas) -> None:
        canvas.delete(self._id)


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

        self._centre: Optional[Point] = None
        self._left_wall: Optional[Line] = None
        self._right_wall: Optional[Line] = None
        self._top_wall: Optional[Line] = None
        self._bottom_wall: Optional[Line] = None

    @property
    def centre(self) -> Point:
        if self._centre:
            return self._centre

        _x_centre: int = m.floor(0.5 * (self.__bottom_right_x - self.__top_left_x))
        _y_centre: int = m.floor(0.5 * (self.__bottom_right_y - self.__top_left_y))
        self._centre = Point(_x_centre, _y_centre)
        return self._centre

    @property
    def left_wall(self) -> Line:
        if self._left_wall:
            return self._left_wall
        _p1 = Point(self.__top_left_x, self.__top_left_y)
        _p2 = Point(self.__top_left_x, self.__bottom_right_y)
        self._left_wall: Line = line_constructor(_p1, _p2)
        return self._left_wall

    @property
    def right_wall(self) -> Line:
        if self._right_wall:
            return self._right_wall
        _p1 = Point(self.__bottom_right_x, self.__top_left_y)
        _p2 = Point(self.__bottom_right_x, self.__bottom_right_y)
        self._right_wall: Line = line_constructor(_p1, _p2)
        return self._right_wall

    @property
    def top_wall(self) -> Line:
        if self._top_wall:
            return self._top_wall
        _p1 = Point(self.__top_left_x, self.__top_left_y)
        _p2 = Point(self.__bottom_right_x, self.__top_left_y)
        self._top_wall: Line = line_constructor(_p1, _p2)
        return self._top_wall

    @property
    def bottom_wall(self) -> Line:
        if self._bottom_wall:
            return self._bottom_wall
        _p1 = Point(self.__top_left_x, self.__bottom_right_y)
        _p2 = Point(self.__bottom_right_x, self.__bottom_right_y)
        self._bottom_wall: Line = line_constructor(_p1, _p2)
        return self._bottom_wall


def line_constructor(
    _from: Point | tuple[int, int],
    _to: Point | tuple[int, int],
    window: Optional["Window"] = None,
) -> Line:

    window_size: Optional[tuple[int, int]] = None
    if window:
        window_size = (window.width, window.height)
    if not isinstance(_from, Point):
        _from = Point(_from[0], _from[1], window_size=window_size)
    if not isinstance(_to, Point):
        _to = Point(_to[0], _to[1], window_size=window_size)

    return Line(_from, _to)
