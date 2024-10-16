import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        win = Window(800, 600)
        m1.add_window(win)
        m1._break_entrance_and_exit()
        m1._break_walls(0, 0)
        m1._reset_cells_visited()
        bad_cell = False
        for i in range(m1.num_cols):
            for j in range(m1.num_rows):
                bad_cell = bad_cell or m1._cells[i][j].visited
        self.assertEqual(bad_cell, False)

        self.assertEqual(m1.solve(), True)

if __name__ == '__main__':
    unittest.main()
