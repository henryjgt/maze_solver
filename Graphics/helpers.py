from typing import Tuple

from Graphics import Line, Point


def line_constructor(
    window_size: Tuple[int, int],
    _from: Tuple[int, int],
    _to: Tuple[int, int],
) -> Line:

    errmsg = "Points must lie within the size limit of the window"
    if not (_from[0] < window_size[0] and _from[1] < window_size[1]):
        raise ValueError(errmsg)

    if not (_to[0] < window_size[0] and _to[1] < window_size[1]):
        raise ValueError(errmsg)

    from_point = Point(_from[0], _from[1])
    to_point = Point(_to[0], _to[1])
    return Line(from_point, to_point)
