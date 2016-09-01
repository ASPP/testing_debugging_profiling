"""
Test suite for a Sudoku solver.

Sudoku grids are represented as 2D lists, with 0 indicating an empty
element of the grid.
"""

from copy import deepcopy

import sudoku
from problems import *

grid_elements = [[(j,i) for i in range(1, sudoku.GRID_SIZE+1)] 
                 for j in range(1, sudoku.GRID_SIZE+1)]


def test_has_all_numbers():
    assert sudoku.has_all_numbers([1,5,9,8,3,6,7,2,4])
    assert not sudoku.has_all_numbers([1,1,9,8,3,6,7,2,4])
    assert not sudoku.has_all_numbers([0,1,9,8,3,6,7,2,4])


def test_is_solution():
    """Verify that solutions to given problems are valid"""
    for k in sudoku_solutions:
        assert sudoku.is_solution(sudoku_solutions[k],
                                  sudoku_problems[k])


def test_is_not_solution():
    """Verify that wrong solutions are invalid"""
    for k in sudoku_solutions:
        # modify solution, check that is_solution fails
        not_solution = deepcopy(sudoku_solutions[k])
        # swap two elements
        not_solution[3][4], not_solution[3][3] = \
            not_solution[3][3], not_solution[3][4]
        assert not sudoku.is_solution(not_solution,
                                      sudoku_problems[k])


def test_is_solution_to_problem():
    """Check that is_solution control that solution is a solution
    to the problem at hand, not come other problem."""
    assert not sudoku.is_solution(sudoku_solutions[TEST_KEYS[0]],
                                  sudoku_problems[TEST_KEYS[1]])


def test_is_allowed():
    k = TEST_KEYS[0]
    prob = sudoku_problems[k]
    sol = deepcopy(sudoku_solutions[k])
    for row in range(sudoku.GRID_SIZE):
        for col in range(sudoku.GRID_SIZE):
            if prob[row][col] == 0:
                assert sudoku.is_allowed(prob, sol, row+1, col+1)
            saved_number = sol[row][col]
            sol[row][col] = 0
            alt_col = (col+1) % sudoku.GRID_SIZE
            assert not sudoku.is_allowed(sol, sol[row][alt_col], row+1, col+1)
            sol[row][col] = saved_number


def test_find_solution():
    for k in TEST_KEYS:
        print('Solving', k)
        assert sudoku.solve_sudoku(sudoku_problems[k]) == sudoku_solutions[k]


def test_get_row():
    assert sudoku.get_row(grid_elements, 3) == \
           [(3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9)]


def test_get_column():
    assert sudoku.get_column(grid_elements, 3) == \
           [(1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3), (8,3), (9,3)]


def test_get_square():
    assert sudoku.get_square(grid_elements, 2) == \
           [(1,4), (1,5), (1,6), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6)]
    
