"""
03 - NumPy Basics
NumPy gives Python fast arrays for numbers. Almost all scientific Python
(pandas, scikit-learn, matplotlib, PyTorch...) is built on it.

Install once:  pip install numpy   (or Thonny: Tools -> Manage packages)
"""

import numpy as np          # "np" is the standard nickname

# ---- Creating arrays ----
a = np.array([1, 2, 3, 4, 5])
print(a, type(a), a.dtype)            # dtype = the type of EVERY element

M = np.array([[1, 2, 3],
              [4, 5, 6]])
print(M)
print("shape:", M.shape, " ndim:", M.ndim, " size:", M.size)

print(np.zeros((2, 3)))               # 2x3 of zeros
print(np.ones(4))
print(np.arange(0, 10, 2))            # like range(): [0 2 4 6 8]
print(np.linspace(0, 1, 5))           # 5 evenly spaced points from 0 to 1
print(np.eye(3))                      # 3x3 identity matrix

rng = np.random.default_rng(seed=42)  # a random number generator (seeded = repeatable)
print(rng.integers(1, 7, size=10))    # 10 dice rolls
print(rng.random((2, 2)))             # 2x2 random floats in [0, 1)

print()

# ---- Indexing and slicing ----
print(a[0], a[-1], a[1:4])
print(M[1, 2])                        # row 1, col 2 (NumPy style: M[r, c])
print(M[0])                           # row 0
print(M[:, 1])                        # column 1 -- easy in NumPy!
print(M[:, 1:])                       # all rows, columns 1 onward

# ---- Arrays have ONE type: mixing turns everything into the most general one ----
print(np.array([1, 2.5, 3]))          # all floats
print(np.array([1, "a"]))             # all strings (!)

# ---- Reshape ----
nums = np.arange(12)
print(nums.reshape(3, 4))
print(nums.reshape(3, 4).T)           # .T = transpose
