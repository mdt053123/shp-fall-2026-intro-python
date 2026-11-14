"""
Exercise 4 (CHALLENGE) - Conway's Game of Life  (SOLUTION)
----------------------------------------------
A grid of cells, each ALIVE (1) or DEAD (0). Every generation, all cells
update AT THE SAME TIME using these rules:

  - A live cell with 2 or 3 live neighbors stays alive (otherwise it dies)
  - A dead cell with exactly 3 live neighbors becomes alive
  (neighbors = the up-to-8 surrounding cells; the edges of the grid are dead)

From these simple rules come patterns that blink, glide, and even compute!

1. count_neighbors(grid, r, c): number of live neighbors of (r, c)
2. next_generation(grid): return a NEW grid (don't modify the old one while
   you're still reading from it!)
3. Run the file to watch a "glider" crawl across the screen.

Bonus: write the grid to a file, or try the "R-pentomino" or "Gosper glider gun".
"""

import time


def count_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (dr, dc) != (0, 0):
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    total += grid[rr][cc]
    return total


def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            n = count_neighbors(grid, r, c)
            if grid[r][c] == 1 and n in (2, 3):
                new[r][c] = 1
            elif grid[r][c] == 0 and n == 3:
                new[r][c] = 1
    return new


def show(grid):  # given
    print("\n".join("".join("██" if x else "··" for x in row) for row in grid))


def glider_demo(generations=20):  # given
    grid = [[0] * 12 for _ in range(10)]
    for r, c in [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
        grid[r][c] = 1
    for gen in range(generations):
        print(f"\nGeneration {gen}")
        show(grid)
        grid = next_generation(grid)
        if grid is None:
            print("(next_generation isn't written yet)")
            return
        time.sleep(0.15)


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


blinker_h = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
blinker_v = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
block = [[1, 1], [1, 1]]
check("count_neighbors center", lambda: count_neighbors(blinker_h, 1, 1), 2)
check("count_neighbors top-middle", lambda: count_neighbors(blinker_h, 0, 1), 3)
check("blinker flips", lambda: next_generation(blinker_h), blinker_v)
check("blinker flips back", lambda: next_generation(blinker_v), blinker_h)
check("block is stable", lambda: next_generation(block), block)
check("doesn't modify input", lambda: (next_generation(blinker_h), blinker_h)[1], [[0, 0, 0], [1, 1, 1], [0, 0, 0]])

glider_demo()
