import unittest
from sudoku_solution import find_empty
from sudoku_solution import check_row
from sudoku_solution import check_column
from sudoku_solution import check_sudoka
from sudoku_solution import check_square

class TestSudoka_solution(unittest.TestCase):
    def setUp(self):
        self.s1 = [[2, 0, 4, 0, 0, 8, 0, 0, 9],
              [0, 0, 9, 0, 0, 0, 2, 0, 8],
              [0, 6, 0, 0, 0, 2, 0, 3, 0],
              [0, 2, 5, 0, 0, 6, 0, 0, 4],
              [0, 4, 6, 0, 0, 0, 7, 8, 0],
              [7, 0, 0, 2, 0, 0, 5, 6, 0],
              [0, 9, 0, 6, 0, 0, 0, 2, 0],
              [4, 0, 7, 0, 0, 0, 8, 0, 0],
              [6, 0, 0, 4, 0, 0, 9, 0, 3]]

        self.s_invalid = [[2, 0, 4, 0, 0, 8, 0, 0, 9],
                   [0, 0, 9, 0, 0, 0, 2, 0, 8],
                   [0, 6, 0, 0, 0, 2, 0, 3, 0],
                   [0, 2, 5, 0, 8, 6, 0, 0, 4],
                   [0, 4, 6, 0, 0, 0, 7, 8, 0],
                   [7, 0, 0, 2, 0, 0, 5, 6, 0],
                   [0, 9, 0, 6, 0, 0, 0, 2, 0],
                   [4, 2, 7, 0, 0, 5, 8, 0, 0],
                   [6, 0, 0, 4, 0, 0, 9, 0, 3]]

        self.s1s = [[2, 7, 4, 3, 1, 8, 6, 5, 9],
               [3, 1, 9, 7, 6, 5, 2, 4, 8],
               [5, 6, 8, 9, 4, 2, 1, 3, 7],
               [1, 2, 5, 8, 7, 6, 3, 9, 4],
               [9, 4, 6, 1, 5, 3, 7, 8, 2],
               [7, 8, 3, 2, 9, 4, 5, 6, 1],
               [8, 9, 1, 6, 3, 7, 4, 2, 5],
               [4, 3, 7, 5, 2, 9, 8, 1, 6],
               [6, 5, 2, 4, 8, 1, 9, 7, 3]]
    def test_check_row(self):
        self.assertEqual(True, check_row(self.s1, find_empty(self.s1), 7))
        self.assertEqual(False, check_row(self.s1, find_empty(self.s1), 4))
    def test_check_column(self):
        self.assertEqual(True,check_column(self.s1,find_empty(self.s1),7))
        self.assertEqual(False, check_column(self.s1, find_empty(self.s1), 2))
    def test_check_square(self):
        self.assertEqual(True, check_square(self.s1, find_empty(self.s1), 7))
        self.assertEqual(False, check_square(self.s1, find_empty(self.s1), 2))
    def test_check_sudoka(self):
        self.assertEqual(True,check_sudoka(self.s1s))
        self.assertEqual(True,check_sudoka(self.s1))
        self.assertEqual(False, check_sudoka(self.s_invalid))

if __name__ == "__main__":
    unittest.main()