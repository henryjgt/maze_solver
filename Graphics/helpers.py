from typing import Optional, Tuple

from Graphics import Line, Point


def line_constructor(
    _from: Point | Tuple[int, int],
    _to: Point | Tuple[int, int],
    window: Optional["Window"] = None,
) -> Line:

    window_size: Optional[Tuple[int, int]] = None
    if window:
        window_size = (window.width, window.height)

    if not isinstance(_from, Point):
        _from = Point(_from[0], _from[1], window_size=window_size)

    if not isinstance(_to, Point):
        _to = Point(_to[0], _to[1], window_size=window_size)

    return Line(_from, _to)
