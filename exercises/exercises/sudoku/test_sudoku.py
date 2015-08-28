"""
Test suite for a Sudoku solver.

Sudoku grids are represented as 2D lists, with 0 indicating an empty
element of the grid.
"""

import unittest
from copy import deepcopy

# this is the module you have to write
import sudoku

# the problems module contains two dictionaries,
# sudoku_solutions and sudoku_problems. Their keys are
# problems names, and the values are Sudoku boards
from problems import sudoku_problems, sudoku_solutions, TEST_KEYS


class TestIsSolution(unittest.TestCase):
    """TestCase for a Sudoku solution validator:
    sudoku.is_solution(solution_grid, problem_grid)
    Both arguments are 2D lists.
    """

    def test_is_solution(self):
        """Verify that solutions to given problems are valid"""
        for k in sudoku_solutions:
            self.assertTrue(sudoku.is_solution(sudoku_solutions[k],
                                               sudoku_problems[k]))

    def test_is_not_solution(self):
        """Verify that wrong solutions are invalid"""
        for k in sudoku_solutions:
            # modify solution, check that is_solution fails
            not_solution = deepcopy(sudoku_solutions[k])
            # swap two elements
            not_solution[3][4], not_solution[3][3] = \
                not_solution[3][3], not_solution[3][4]
            self.assertFalse(sudoku.is_solution(not_solution,
                                                sudoku_problems[k]))

    def test_is_solution_to_problem(self):
        """Check that is_solution control that solution is a solution
        to the problem at hand, not come other problem."""
        self.assertFalse(sudoku.is_solution(sudoku_solutions[TEST_KEYS[0]],
                                            sudoku_problems[TEST_KEYS[1]]))


class TestSolveSudoku(unittest.TestCase):
    """TestCase for a Sudoku solver:
    solution_grid = sudoku.solve_sudoku(problem_grid)
    This function takes a 2D list as input arguemtn and returns a 2D list.
    """

    def test_find_solution(self):
        print '\n'
        for k in TEST_KEYS:
            print 'Solving', k
            self.assertEqual(sudoku.solve_sudoku(sudoku_problems[k]),
                             sudoku_solutions[k])


if __name__ == '__main__':
    unittest.main()
