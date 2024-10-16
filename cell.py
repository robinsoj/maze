from tkinter import Tk, BOTH, Canvas
from graphic_primatives import Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, hlw, hrw, htw, hbw, win):
        self.has_left_wall = hlw
        self.has_right_wall = hrw
        self.has_top_wall = htw
        self.has_bottom_wall = hbw
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.left_wall = Line(x1, y1, x1, y2)
        self.right_wall = Line(x2, y1, x2, y2)
        self.top_wall = Line(x1, y1, x2, y1)
        self.bottom_wall = Line(x1, y2, x2, y2)
        self.visited = False

    def draw(self, canvas, color):
        bg_color = canvas.cget('bg')
        if self.has_left_wall:
            self.left_wall.draw(canvas, color)
        else:
            self.left_wall.draw(canvas, bg_color)
        if self.has_right_wall:
            self.right_wall.draw(canvas, color)
        else:
            self.right_wall.draw(canvas, bg_color)
        if self.has_top_wall:
            self.top_wall.draw(canvas, color)
        else:
            self.top_wall.draw(canvas, bg_color)
        if self.has_bottom_wall:
            self.bottom_wall.draw(canvas, color)
        else:
            self.bottom_wall.draw(canvas, bg_color)

    def center(self):
        return Point(int((self.__x1 + self.__x2)/2), int((self.__y1 + self.__y2)/2))

    def draw_move(self, c2, canvas, undo=False):
        
        if not undo:
            color = "red"
        else:
            color = canvas.cget('bg')
        center1 = self.center()
        center2 = c2.center()
        line = Line(center1.x, center1.y, center2.x, center2.y)
        line.draw(canvas, color)

    def get_win(self):
        return self.__win

    def get_corners(self):
        return Point(self.__x1, self.__y1), Point(self.__x2, self.__y2)

    def __repr__(self):
        return f"({self.__x1}, {self.__y1}) - ({self.__x2}, {self.__y2}): {self.has_left_wall}, {self.has_top_wall}, {self.has_right_wall}, {self.has_bottom_wall}"
