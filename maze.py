from tkinter import Tk, BOTH, Canvas
from graphic_primatives import Point, Line
from window import Window
from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, seed = None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__window = None
        if seed is not None:
            random.seed(seed)
        self.create_cells()

    def add_window(self, win):
        self.__window = win

    def create_cells(self):
        for column in range(self.num_cols):
            col_list = []
            for row in range(self.num_rows):
                if row == self.num_rows-1 and column == self.num_cols-1:
                    win = True
                else:
                    win = False
                col_list.append(Cell(self.x1 + row * self.cell_size_x, self.y1 + column * self.cell_size_y,
                                     self.x1 + (row + 1) * self.cell_size_x, self.y1 + (column + 1) * self.cell_size_y,
                                     True, True, True, True, win))
            self._cells.append(col_list)

    def draw_cell(self, i, j):
        canvas = self.__window.get_canvas()
        pt = self._cells[i][j].center()
        self._cells[i][j].draw(canvas, 'black')
        self._animate()

    def _animate(self):
        self.__window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            if i < self.num_cols-1:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))
            if j < self.num_rows-1:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._cells[i][j].draw(self.__window.get_canvas(), 'black')
                return
            x, y = to_visit[random.randrange(0, len(to_visit))]
            if i == x - 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[x][y].has_top_wall = False
            if j == y - 1:
                self._cells[i][j].has_right_wall = False
                self._cells[x][y].has_left_wall = False
            if i == x + 1:
                self._cells[i][j].has_top_wall = False
                self._cells[x][y].has_bottom_wall = False
            if j == y + 1:
                self._cells[i][j].has_left_wall = False
                self._cells[x][y].has_right_wall = False
            self._break_walls(x, y)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        canvas = self.__window.get_canvas()
        if self._cells[i][j].get_win():
            return True
        if not self._cells[i][j].has_left_wall and j > 0:
            if not self._cells[i][j - 1].visited:
                self._cells[i][j].draw_move(self._cells[i][j - 1], canvas)
                if self._solve_r(i, j - 1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j - 1], canvas, True)
        if not self._cells[i][j].has_top_wall and i > 0:
            if not self._cells[i - 1][j].visited:
                self._cells[i][j].draw_move(self._cells[i - 1][j], canvas)
                if self._solve_r(i - 1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i - 1][j], canvas, True)
        if not self._cells[i][j].has_bottom_wall and i < self.num_cols - 1:
            if not self._cells[i + 1][j].visited:
                self._cells[i][j].draw_move(self._cells[i + 1][j], canvas)
                if self._solve_r(i + 1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i + 1][j], canvas, True)
        if not self._cells[i][j].has_right_wall and j < self.num_rows - 1:
            if not self._cells[i][j + 1].visited:
                self._cells[i][j].draw_move(self._cells[i][j + 1], canvas)
                if self._solve_r(i, j + 1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j + 1], canvas, True)
        return False

    
def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 10, 10, 78, 58, 0)
    maze.add_window(win)
    for i in range(maze.num_cols):
        for j in range(maze.num_rows):
            maze.draw_cell(i, j)
    maze._break_entrance_and_exit()
    maze._break_walls(0, 0)
    maze._reset_cells_visited()
    x = maze.solve()
    win.wait_for_close()

if __name__ == '__main__':
    main()
