"""Simple, brute-force Sudoku solver."""

from copy import deepcopy

GRID_SIZE = 9
SQUARE_SIZE = 3

def get_row(grid, i):
    """Return i-th row of a Sudoku grid.
    Rows are numbered from 1 to 9."""
    return grid[i-1]

def get_column(grid, i):
    """Return i-th column of a Sudoku grid.
    Columns are numbered from 1 to 9."""
    return [grid[j][i-1] for j in range(GRID_SIZE)]

# start coordinates of sudoku squares
_square_coords = [(_i*SQUARE_SIZE, _j*SQUARE_SIZE)
                  for _i in range(SQUARE_SIZE) for _j in range(SQUARE_SIZE)]

def get_square(grid, i):
    """Return i-th square of a Sudoku grid.
    Squares are numbered from to 9."""
    k0, l0 = _square_coords[i-1]
    return [grid[k0+k][l0+l]
            for k in range(SQUARE_SIZE) for l in range(SQUARE_SIZE)]

def has_all_numbers(grid_part):
    return set(grid_part) == set(range(1, GRID_SIZE+1))

def is_solution(solution, problem=None):
    """Verify if a grid is a solution to a given Sudoku problem.
    If problem is None, the function only verifies that the grid
    is consistent (in the sense of having all numbers 1-9 on all rows,
    columns, and squares)
    """
    
    # first, verify that all the numbers in 'problem' are also in 'solution'
    if problem is not None:
        if not all(solution[i][j]==problem[i][j] or problem[i][j]==0
                   for i in range(GRID_SIZE) for j in range(GRID_SIZE)):
            return False
               
    # verify that on every row, column, and square there are all the numbers once
    for i in range(GRID_SIZE):
        if not (has_all_numbers(get_row(solution, i))
                and has_all_numbers(get_column(solution, i))
                and has_all_numbers(get_square(solution, i))):
            return False
    return True

# ############## Sudoku solver

# initialize coordinates-to-square dictionary
_k = 1
_coords2square = {}
for _i in range(SQUARE_SIZE):
    for _j in range(SQUARE_SIZE):
        _coords2square[(_i,_j)] = _k
        _k += 1

def coords_to_square(row, col):
    """Convert grid coordinates to square number."""
    return _coords2square[((row-1)//3, (col-1)//3)]

def is_allowed(grid, n, row, col):
    """Check that putting 'n' at (row, col) does not violate Sudoku rules.
    row and col must be in the range 1-9"""
    return not (n in get_row(grid, row)
                or n in get_column(grid, col)
                or n in get_square(grid, coords_to_square(row, col)))

def solve_sudoku(problem):
    """Simple, brute-force Sudoku solver."""
    solution = deepcopy(problem)
    # coordinates of blank grid elements
    coords = [(i,j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if problem[i][j]==0]
    
    # index in the coordinates array
    pos = 0
    while pos < len(coords):
        row, col = coords[pos]
        # increment current proposal in the solution
        proposal = solution[row][col] + 1
        solution[row][col] = 0
        
        found = False
        while proposal<=GRID_SIZE:
            found = is_allowed(solution, proposal, row+1, col+1)
            if found: break
            proposal += 1
            
        if found:
            solution[row][col] = proposal
            pos += 1
        else:
            pos -= 1

    return solution
