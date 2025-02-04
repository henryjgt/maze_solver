from GUI import Window, DisplayedCell

# from Graphics import Line, line_constructor


def main() -> None:
    win = Window(WIDTH_PX, HEIGHT_PX)
    # L1: Line = line_constructor(
    #     (100, 100),
    #     (100, 500),
    #     window_size=(WIDTH_PX, HEIGHT_PX),
    # )
    # L2: Line = line_constructor(
    #     (100, 100),
    #     (600, 500),
    #     window_size=(WIDTH_PX, HEIGHT_PX),
    # )
    # win.draw_line(L1, "red")
    # win.draw_line(L2, "blue")

    win.wait_for_close()


if __name__ == "__main__":

    WIDTH_PX: int = 800
    HEIGHT_PX: int = 600

    main()
