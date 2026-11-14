"""
Exercise 2 - NumPy  (SOLUTION)
------------------
Solve each one WITHOUT Python loops: use NumPy operations, masks, and methods.
"""

import numpy as np


def celsius_to_fahrenheit(temps_c):
    """Convert an array of Celsius temps.   [0, 100] -> [32., 212.]"""
    return temps_c * 9 / 5 + 32


def count_above_mean(values):
    """How many values are strictly greater than the mean?  [1, 2, 3, 10] -> 1"""
    return int((values > values.mean()).sum())


def normalize(values):
    """Min-max scale values to the range 0..1:  (x - min) / (max - min).
    [10, 20, 30] -> [0., 0.5, 1.]"""
    return (values - values.min()) / (values.max() - values.min())


def z_scores(values):
    """How many standard deviations each value is from the mean: (x - mean) / std."""
    return (values - values.mean()) / values.std()


def curve(scores, target_mean=80):
    """Add the same number of points to every score so the new mean equals target_mean,
    but cap every score at 100.   Hint: np.minimum(array, 100)"""
    return np.minimum(scores + (target_mean - scores.mean()), 100)


def top_k_indices(values, k):
    """Indices of the k largest values, largest first.
    [5, 1, 9, 7] with k=2 -> [2, 3]      Hint: np.argsort, then reverse with [::-1]"""
    return np.argsort(values)[::-1][:k]


def checkerboard(n):
    """An n x n array of 0s and 1s with 0 in the top-left corner:
    n=3 -> [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    Hint: (row + col) % 2, and np.indices or np.add.outer(np.arange(n), np.arange(n))"""
    return np.add.outer(np.arange(n), np.arange(n)) % 2


def monte_carlo_pi(n, seed=0):
    """Estimate pi: throw n random darts at the unit square [0,1) x [0,1).
    The fraction landing inside the quarter circle x^2 + y^2 <= 1 is about pi/4.
    Use rng = np.random.default_rng(seed) and rng.random(n) for x and for y."""
    rng = np.random.default_rng(seed)
    x = rng.random(n)
    y = rng.random(n)
    inside = (x ** 2 + y ** 2 <= 1).sum()
    return 4 * inside / n


def close(a, b):  # given
    """Helper for checks: True if two arrays/numbers are (almost) equal."""
    try:
        return bool(np.allclose(a, b))
    except TypeError:
        return False


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


scores = np.array([70, 85, 90, 55, 100])
check("celsius_to_fahrenheit", lambda: close(celsius_to_fahrenheit(np.array([0, 100, -40])), [32, 212, -40]), True)
check("count_above_mean", lambda: count_above_mean(np.array([1, 2, 3, 10])), 1)
check("normalize", lambda: close(normalize(np.array([10, 20, 30])), [0, 0.5, 1]), True)
check("z_scores mean 0", lambda: close(z_scores(scores).mean(), 0), True)
check("z_scores std 1", lambda: close(z_scores(scores).std(), 1), True)
check("curve", lambda: close(curve(scores, 85), [75, 90, 95, 60, 100]), True)
check("top_k_indices", lambda: list(top_k_indices(np.array([5, 1, 9, 7]), 2)), [2, 3])
check("checkerboard", lambda: checkerboard(3).tolist(), [[0, 1, 0], [1, 0, 1], [0, 1, 0]])
check("monte_carlo_pi", lambda: abs(monte_carlo_pi(1_000_000) - np.pi) < 0.01, True)
