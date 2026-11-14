"""
04 - NumPy Operations: Vectorized Math
Operations apply to EVERY element at once -- no loops needed.
"""

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# ---- Element-wise arithmetic ----
print(a + b)            # [11 22 33 44]
print(a * b)            # [10 40 90 160]   (element-wise, NOT matrix multiply)
print(a ** 2)           # [ 1  4  9 16]
print(a * 10)           # "broadcasting": the 10 is applied to every element
print(np.sqrt(a))

# Compare with plain lists:
print([1, 2] + [3, 4])  # list + list = concatenation!
print([1, 2] * 2)       # list * 2 = repetition!

print()

# ---- Aggregations ----
scores = np.array([88, 92, 79, 65, 95, 70])
print("sum", scores.sum(), " mean", scores.mean(), " median", np.median(scores))
print("min", scores.min(), " max", scores.max(), " std", round(scores.std(), 2))
print("index of max:", scores.argmax())
print("sorted:", np.sort(scores))

M = np.array([[1, 2, 3],
              [4, 5, 6]])
print("column sums:", M.sum(axis=0))   # axis=0 -> down the rows
print("row sums:   ", M.sum(axis=1))   # axis=1 -> across the columns

print()

# ---- Boolean masks: filter without loops ----
passing = scores >= 80
print(passing)                         # [ True  True False False  True False]
print(scores[passing])                 # [88 92 95]
print(scores[scores < 75])             # [65 70]
print("how many passed:", passing.sum())   # True counts as 1

curved = np.where(scores < 70, 70, scores)  # "if < 70, make it 70, else keep"
print(curved)

print()

# ---- Linear algebra ----
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)                           # matrix multiplication (same as our matmul!)
print(np.dot([1, 2, 3], [4, 5, 6]))    # 32

# Solve a system of equations:  x + 2y = 5,  3x + 4y = 6
x, y = np.linalg.solve(A, [5, 6])
print(f"x = {x:.2f}, y = {y:.2f}")
