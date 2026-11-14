"""
02 - Matrix Math by Hand
Writing these ourselves shows exactly what NumPy does for us (next file!).
"""


def shape(M):
    return (len(M), len(M[0]))


def mat_add(A, B):
    """Add matching entries. A and B must have the same shape."""
    if shape(A) != shape(B):
        return None
    return [[A[r][c] + B[r][c] for c in range(len(A[0]))] for r in range(len(A))]


def scalar_mul(k, A):
    return [[k * x for x in row] for row in A]


def transpose(A):
    """Rows become columns: T[c][r] = A[r][c]."""
    return [[A[r][c] for r in range(len(A))] for c in range(len(A[0]))]


def dot(u, v):
    """Dot product of two vectors: u1*v1 + u2*v2 + ... + un*vn."""
    if len(u) != len(v):
        return None
    return sum(a * b for a, b in zip(u, v))


def matmul(A, B):
    """Matrix multiplication. Entry (i, j) = dot(row i of A, column j of B).
    Requires: number of COLUMNS of A == number of ROWS of B.
    (m x k) @ (k x n) -> (m x n)"""
    if not A or not B or len(A[0]) != len(B):
        return None
    rows, inner, cols = len(A), len(B), len(B[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(inner):
                result[i][j] += A[i][k] * B[k][j]
    return result


def identity(n):
    return [[1 if r == c else 0 for c in range(n)] for r in range(n)]


def show(M):
    for row in M:
        print("  ", " ".join(f"{x:4}" for x in row))


A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]

print("A + B:");      show(mat_add(A, B))
print("3 * A:");      show(scalar_mul(3, A))
print("A @ B:");      show(matmul(A, B))        # [[19, 22], [43, 50]]
print("B @ A:");      show(matmul(B, A))        # different! Order matters.
print("A @ I = A:");  show(matmul(A, identity(2)))

C = [[1, 2, 3],
     [4, 5, 6]]       # 2x3
print("C transposed (3x2):"); show(transpose(C))
print("C @ C^T (2x2):");      show(matmul(C, transpose(C)))
print("C @ C (bad shapes):", matmul(C, C))

print("dot([1, 2, 3], [4, 5, 6]) =", dot([1, 2, 3], [4, 5, 6]))   # 32

# Why care? Matrix multiplication powers computer graphics (rotating 3D
# objects), Google's original PageRank, and every neural network in AI.
