"""
01 - Matrices as Lists of Lists
A matrix (grid, table, image...) can be stored as a list of ROWS.
M[r][c] = the item in row r, column c.
"""

M = [[1, 2, 3],
     [4, 5, 6]]          # 2 rows x 3 columns ("a 2x3 matrix")

print(M[0])              # [1, 2, 3]  row 0
print(M[1][2])           # 6          row 1, column 2
print(len(M), "rows,", len(M[0]), "columns")

# A column is spread across rows, so gather it with a loop
col_1 = [row[1] for row in M]
print("column 1:", col_1)

print()

# ---- Looping: by index ----
for r in range(len(M)):
    for c in range(len(M[r])):
        print(f"M[{r}][{c}] = {M[r][c]}", end="   ")
    print()

# ---- Looping: by value ----
for row in M:
    for x in row:
        print(x, end=" ")
    print()

print()

# ---- Building a matrix ----
rows, cols = 3, 4
zeros = [[0] * cols for _ in range(rows)]     # correct: 3 separate rows
zeros[0][0] = 9
print(zeros)
# WRONG: [[0] * cols] * rows gives 3 references to the SAME row (see Day 4)

times_table = [[(r + 1) * (c + 1) for c in range(5)] for r in range(5)]
for row in times_table:
    print(" ".join(f"{x:3}" for x in row))

print()

# ---- Matrices are everywhere: a tiny "image" (0 = dark, 1 = light) ----
smiley = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
]
for row in smiley:
    print("".join("██" if px else "  " for px in row))
