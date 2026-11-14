"""
05 - Why NumPy? Speed.
NumPy's loops run in fast, compiled C code instead of Python.
"""

import time
import numpy as np

n = 2_000_000
py_list = list(range(n))
np_array = np.arange(n)

start = time.perf_counter()
total = 0
for x in py_list:
    total += x * x
py_time = time.perf_counter() - start

start = time.perf_counter()
total_np = (np_array.astype(np.int64) ** 2).sum()
np_time = time.perf_counter() - start

print(f"Sum of squares of {n:,} numbers")
print(f"  Python loop: {py_time * 1000:8.1f} ms")
print(f"  NumPy:       {np_time * 1000:8.1f} ms")
print(f"  NumPy is about {py_time / np_time:.0f}x faster (same answer: {total == total_np})")

# Matrix multiplication: our triple loop vs NumPy
def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

size = 150
A = np.random.default_rng(0).random((size, size))
B = np.random.default_rng(1).random((size, size))

start = time.perf_counter()
C1 = matmul(A.tolist(), B.tolist())
loop_time = time.perf_counter() - start

start = time.perf_counter()
C2 = A @ B
np_time = time.perf_counter() - start

print(f"\n{size}x{size} matrix multiply")
print(f"  triple loop: {loop_time * 1000:8.1f} ms")
print(f"  NumPy @:     {np_time * 1000:8.3f} ms")
print(f"  same answer: {np.allclose(C1, C2)}")
