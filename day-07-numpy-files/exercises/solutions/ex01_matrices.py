"""
Exercise 1 - Matrices (plain Python lists, no NumPy)  (SOLUTION)
----------------------------------------------------
A matrix is a list of rows. Don't change the input matrices -- return new ones.
"""


def dimensions(M):
    """Return (rows, cols).   dimensions([[1, 2, 3], [4, 5, 6]]) -> (2, 3)"""
    return (len(M), len(M[0]))


def row_sums(M):
    """row_sums([[1, 2], [3, 4]]) -> [3, 7]"""
    return [sum(row) for row in M]


def col_sums(M):
    """col_sums([[1, 2], [3, 4]]) -> [4, 6]"""
    return [sum(M[r][c] for r in range(len(M))) for c in range(len(M[0]))]


def find(M, target):
    """Return (row, col) of the first place target appears (reading row by row), or None.

    find([[1, 2], [3, 4]], 3) -> (1, 0)
    """
    for r in range(len(M)):
        for c in range(len(M[r])):
            if M[r][c] == target:
                return (r, c)
    return None


def is_symmetric(M):
    """True if M is square and M[r][c] == M[c][r] for all r, c.

    is_symmetric([[1, 7], [7, 2]]) -> True
    """
    n = len(M)
    if any(len(row) != n for row in M):
        return False
    for r in range(n):
        for c in range(n):
            if M[r][c] != M[c][r]:
                return False
    return True


def diagonal_sum(M):
    """Sum of the main diagonal of a square matrix (top-left to bottom-right).

    diagonal_sum([[1, 2], [3, 4]]) -> 5
    """
    return sum(M[i][i] for i in range(len(M)))


def rotate_clockwise(M):
    """Rotate a matrix 90 degrees clockwise.

    rotate_clockwise([[1, 2, 3],        [[4, 1],
                      [4, 5, 6]])  ->    [5, 2],
                                         [6, 3]]
    Hint: the new row c is the old column c, read from BOTTOM to TOP.
    """
    rows, cols = len(M), len(M[0])
    return [[M[rows - 1 - r][c] for r in range(rows)] for c in range(cols)]


def neighbors_sum(M, r, c):
    """Sum of the up-to-8 neighbors of cell (r, c), NOT including (r, c) itself.
    Stay inside the grid! (This is the heart of Conway's Game of Life.)

    neighbors_sum([[1, 1, 1], [1, 9, 1], [1, 1, 1]], 1, 1) -> 8
    neighbors_sum([[1, 1, 1], [1, 9, 1], [1, 1, 1]], 0, 0) -> 11
    """
    total = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            rr, cc = r + dr, c + dc
            if 0 <= rr < len(M) and 0 <= cc < len(M[0]):
                total += M[rr][cc]
    return total


# ----------------------- Checks (don't change below) -----------------------
def check(label, get_actual, expected):
    try:
        actual = get_actual()
    except Exception as e:
        print(f"FAIL  {label}: crashed with {type(e).__name__}: {e}")
        return
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("dimensions", lambda: dimensions([[1, 2, 3], [4, 5, 6]]), (2, 3))
check("row_sums", lambda: row_sums([[1, 2], [3, 4]]), [3, 7])
check("col_sums", lambda: col_sums([[1, 2], [3, 4]]), [4, 6])
check("col_sums 2x3", lambda: col_sums([[1, 2, 3], [4, 5, 6]]), [5, 7, 9])
check("find", lambda: find([[1, 2], [3, 4]], 3), (1, 0))
check("find missing", lambda: find([[1, 2], [3, 4]], 9), None)
check("is_symmetric yes", lambda: is_symmetric([[1, 7], [7, 2]]), True)
check("is_symmetric no", lambda: is_symmetric([[1, 7], [0, 2]]), False)
check("is_symmetric not square", lambda: is_symmetric([[1, 2, 3], [4, 5, 6]]), False)
check("diagonal_sum", lambda: diagonal_sum([[1, 2], [3, 4]]), 5)
check("rotate_clockwise", lambda: rotate_clockwise([[1, 2, 3], [4, 5, 6]]), [[4, 1], [5, 2], [6, 3]])
check("neighbors_sum middle", lambda: neighbors_sum([[1, 1, 1], [1, 9, 1], [1, 1, 1]], 1, 1), 8)
check("neighbors_sum corner", lambda: neighbors_sum([[1, 1, 1], [1, 9, 1], [1, 1, 1]], 0, 0), 11)
