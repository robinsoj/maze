from tkinter import Tk, BOTH, Canvas
from graphic_primatives import Point, Line
from cell import Cell

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True;
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.__root.destroy()

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)

    def get_canvas(self):
        return self.__canvas

def main():
    win = Window(800, 600)
    cell = Cell(50, 50, 100, 100, True, False, True, True, False)
    cell2 = Cell(100, 50, 150, 100, False, True, True, True, False)
    cell.draw(win.get_canvas(), 'black')
    cell2.draw(win.get_canvas(), 'black')
    cell.draw_move(cell2, win.get_canvas())
    line1 = Line(10, 10, 790, 10)
    line2 = Line(790, 10, 790, 590)
    line3 = Line(10, 590, 790, 590)
    line4 = Line(10, 590, 10, 10)
    win.draw_line(line1, 'black')
    win.draw_line(line2, 'black')
    win.draw_line(line3, 'black')
    win.draw_line(line4, 'black')
    win.wait_for_close()

if __name__ == '__main__':
    main()
