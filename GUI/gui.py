import tkinter as tk

from Graphics import Line


class Window:

    def __init__(self, width: int, height: int) -> None:
        self.__running: bool = False

        self.__root = tk.Tk()
        self.__root.title("DEMO GUI")

        self.__canvas = tk.Canvas(width=width, height=height)
        self.__canvas.pack()

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running: bool = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running: bool = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)
