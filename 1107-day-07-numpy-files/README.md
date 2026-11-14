# Day 7 (Sat 11/7): Matrices, NumPy, and Files

**Big idea:** First we build matrix math **by hand** with lists of lists, so we understand it. Then we let **NumPy** do it about 30× faster. We also learn to make data **permanent** with files and CSVs, and we meet **Jupyter notebooks**, the tool we'll use for data science next week.

> **Before class:** install the libraries. See [SETUP.md, Part 2](../SETUP.md#part-2-libraries-before-day-7).

## Learning goals
- [ ] Represent grids, tables, and images as lists of lists, and index them with `M[r][c]`
- [ ] Implement matrix addition, transpose, dot product, and matrix multiplication
- [ ] Create NumPy arrays, and index and slice them (`M[r, c]`, `M[:, c]`)
- [ ] Use vectorized math, aggregations (`sum`, `mean`, `axis=`), and boolean masks
- [ ] Explain why NumPy is faster than Python loops
- [ ] Read and write text files with `with open(...)`, and read/write CSVs with the `csv` module
- [ ] Run and edit a Jupyter notebook

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Warm-up: Day 6 review (Big-O quiz), check in on M5, install check | |
| 0:15 | Matrices as lists of lists | `01` |
| 0:30 | Matrix math by hand (add, transpose, dot, matmul) | `02` |
| 0:55 | NumPy basics | `03` |
| 1:10 | *Break* | |
| 1:20 | NumPy operations, masks, `axis`; speed test | `04`, `05` |
| 1:45 | Text files; CSV files | `06`, `07` |
| 2:05 | Jupyter notebooks | `08_jupyter_intro.ipynb` |
| 2:15 | Exercises / Gradebook M6 | `exercises/`, [project](../gradebook-project/m6-files-stats/) |

---

## Lecture notes

### 1. Matrices as lists (`01`, `02`)
```python
M = [[1, 2, 3],
     [4, 5, 6]]           # 2 rows x 3 cols
M[1][2]                   # 6
[row[1] for row in M]     # column 1 -> [2, 5]
[[0] * cols for _ in range(rows)]   # correct way to build a grid
```
**Matrix multiplication** (m×k) @ (k×n) gives an (m×n) matrix. Entry (i, j) is the **dot product** of row i of A with column j of B. The **inner** sizes must match. Order matters: A@B ≠ B@A in general. It powers 3D graphics, search engines, and neural networks.

### 2. NumPy (`03`–`05`)
```python
import numpy as np
a = np.array([1, 2, 3])
M = np.array([[1, 2, 3], [4, 5, 6]])
M.shape                  # (2, 3)
M[1, 2], M[:, 1]         # an element; a whole column
np.zeros((2, 3)), np.arange(0, 10, 2), np.linspace(0, 1, 5)
rng = np.random.default_rng(42); rng.integers(1, 7, size=10)
```

| Lists | NumPy arrays |
|-------|--------------|
| Any mix of types | One type (`dtype`) |
| `[1, 2] + [3, 4]` → concatenation | `a + b` → element-wise addition |
| Loops for math | **Vectorized** math: `a * 2`, `np.sqrt(a)` |
| Slower | Much faster (the loops run in C) |

- **Aggregations:** `.sum()`, `.mean()`, `np.median()`, `.std()`, `.min()`, `.max()`, `.argmax()`
- **`axis=0`** goes down the rows (one result per column). **`axis=1`** goes across the columns (one result per row).
- **Boolean masks:** `scores[scores >= 80]`, `(scores >= 80).sum()`, `np.where(cond, a, b)`
- **Linear algebra:** `A @ B`, `A.T`, `np.linalg.solve(A, b)`

### 3. Files (`06`, `07`)
```python
with open("notes.txt", "w") as f:     # "w" ERASES the file first; "a" appends; "r" reads
    f.write("line\n")                 # write() doesn't add \n for you
with open("notes.txt") as f:
    for line in f:
        print(line.strip())           # strip() removes the trailing \n
```
- `with` closes the file for you, even if an error happens.
- **Paths are relative to the folder you run from.** Seeing `FileNotFoundError`? Check your working directory.
- **CSV:** `csv.reader` gives rows as lists of **strings**. `csv.DictReader` gives dicts keyed by the header. **Convert the numbers yourself!** When writing, use `open(path, "w", newline="")`.

### 4. Jupyter (`08_jupyter_intro.ipynb`)
Run a cell with **Shift+Enter**. The last line of a cell displays automatically. Cells share variables, and **run order matters**. When confused, choose *Restart Kernel and Run All*.

---

## Common mistakes
- `[[0] * 3] * 3` makes shared rows (see Day 4).
- Expecting `list1 + list2` to add numbers. It joins the lists. Use NumPy arrays for math.
- `np.array([1, "a"])` turns everything into strings.
- Mixing up `axis=0` and `axis=1`.
- Opening with `"w"` when you meant `"a"`. The file gets wiped!
- Forgetting that CSV values are strings: `"90" > "100"` is `True` (it compares alphabetically).

## Key terms

| Term | Meaning |
|------|---------|
| **matrix** | A 2D grid of numbers (rows × columns) |
| **transpose** | Swap rows and columns |
| **dot product** | Sum of element-wise products of two vectors |
| **matrix multiplication** | Row-by-column dot products; (m×k)(k×n) → (m×n) |
| **NumPy / ndarray** | A fast numeric array library / its array type |
| **vectorization** | Applying an operation to a whole array at once (no Python loop) |
| **broadcasting** | Stretching a smaller value to match an array (e.g. `a * 10`) |
| **boolean mask** | An array of True/False used to filter another array |
| **file mode** | `"r"` read, `"w"` write (overwrite), `"a"` append |
| **CSV** | Comma-separated values, a plain-text table format |
| **Jupyter notebook** | A document mixing code, text, and output (`.ipynb`) |

## Exercises → [`exercises/`](exercises/)

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | Matrices (8 functions) | sums, search, symmetry, rotation, neighbors |
| 2 | NumPy (8 functions, no loops!) | normalizing, z-scores, curving grades, Monte Carlo π |
| 3 | Files (7 functions) | word count, round-tripping a file, weather CSV analysis |
| 4 | ⭐ Conway's Game of Life | 2D grids, simulation |

## 📘 Gradebook Project, Milestone 6
Add `save_csv`, `load_csv`, and NumPy `stats()`, then load the real 60-student class from `gradebook-project/data/grades.csv`.
→ [gradebook-project/m6-files-stats](../gradebook-project/m6-files-stats/)

## Videos and reading
1. NumPy for absolute beginners (official): https://numpy.org/doc/stable/user/absolute_beginners.html
2. NumPy tutorial (freeCodeCamp): https://www.youtube.com/watch?v=QUT1VHiLmmI
3. File objects (reading/writing): https://www.youtube.com/watch?v=Uh2ebFW8OYM
4. CSV module: https://www.youtube.com/watch?v=q5uM4VKywbA
5. Jupyter Notebook tutorial: https://www.youtube.com/watch?v=HW29067qVWk
6. 3Blue1Brown on matrix multiplication (beautiful intuition): https://www.youtube.com/watch?v=XkY2DOUCWMU
