from GUI import Window
from Graphics import Line, line_constructor


def main() -> None:
    win = Window(WIDTH_PX, HEIGHT_PX)
    L1: Line = line_constructor((WIDTH_PX, HEIGHT_PX), (100, 100), (100, 500))
    L2: Line = line_constructor((WIDTH_PX, HEIGHT_PX), (100, 100), (600, 500))
    win.draw_line(L1, "red")
    win.draw_line(L2, "blue")
    win.wait_for_close()


if __name__ == "__main__":

    WIDTH_PX: int = 800
    HEIGHT_PX: int = 600

    main()
