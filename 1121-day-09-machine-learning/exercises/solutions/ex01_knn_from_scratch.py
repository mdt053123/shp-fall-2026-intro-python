"""
Exercise 1 - Build Your Own k-NN Classifier  (SOLUTION)
-------------------------------------------
Build every piece of a k-NN classifier and evaluate it, with plain Python (no sklearn).
A training example is a tuple (features, label), e.g. ((5.1, 3.5), "setosa").

At the bottom, your classifier is tested on a real dataset of wheat seeds!
"""

import random
from collections import Counter


def distance(p, q):
    """Euclidean distance between two feature tuples of ANY length.

    distance((0, 0), (3, 4)) -> 5.0
    """
    return sum((a - b) ** 2 for a, b in zip(p, q)) ** 0.5


def k_nearest_labels(point, data, k):
    """Return the LABELS of the k training examples closest to point,
    closest first.

    k_nearest_labels((0, 0), [((5, 5), "b"), ((1, 0), "a"), ((0, 2), "c")], 2) -> ["a", "c"]
    """
    by_distance = sorted(data, key=lambda ex: distance(point, ex[0]))
    return [label for _, label in by_distance[:k]]


def majority_vote(labels):
    """Return the most common label. If there's a tie, return the tied label
    that appears FIRST in the list (the labels are ordered closest-first, so
    this favors the nearest neighbor).

    majority_vote(["a", "b", "b"]) -> "b"
    majority_vote(["a", "b"]) -> "a"
    """
    counts = Counter(labels)
    top = max(counts.values())
    for label in labels:
        if counts[label] == top:
            return label


def knn_predict(point, data, k=3):
    """Combine the two functions above."""
    return majority_vote(k_nearest_labels(point, data, k))


def accuracy(train, test, k):
    """Fraction of test examples that knn_predict labels correctly."""
    correct = sum(1 for features, label in test if knn_predict(features, train, k) == label)
    return correct / len(test)


def split_data(examples, test_fraction=0.2, seed=0):
    """Shuffle a COPY of examples with random.Random(seed).shuffle(...), then return
    (train, test), where test is the LAST round(len * test_fraction) examples."""
    shuffled = list(examples)
    random.Random(seed).shuffle(shuffled)
    n_test = round(len(shuffled) * test_fraction)
    return shuffled[:len(shuffled) - n_test], shuffled[len(shuffled) - n_test:]


def standardize(train, test):
    """Scale every feature to mean 0 / std 1 using the TRAINING set's mean and std.
    Return (train_scaled, test_scaled) in the same (features, label) format."""
    n = len(train[0][0])
    means = [sum(f[i] for f, _ in train) / len(train) for i in range(n)]
    stds = [(sum((f[i] - means[i]) ** 2 for f, _ in train) / len(train)) ** 0.5 for i in range(n)]

    def scale(features):
        return tuple((features[i] - means[i]) / stds[i] for i in range(n))

    return [(scale(f), l) for f, l in train], [(scale(f), l) for f, l in test]


def make_seeds_data():  # given
    """A synthetic dataset modeled on the classic UCI wheat-seeds data:
    (area, perimeter, kernel_length, asymmetry) for 3 wheat varieties."""
    rng = random.Random(1)
    centers = {"Kama": (14.3, 14.3, 5.5, 2.7), "Rosa": (18.3, 16.1, 6.1, 3.6), "Canadian": (11.9, 13.2, 5.2, 4.8)}
    spread = (1.2, 0.6, 0.25, 1.2)
    data = []
    for label, center in centers.items():
        for _ in range(70):
            data.append((tuple(round(rng.gauss(c, s), 2) for c, s in zip(center, spread)), label))
    return data


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


toy = [((5, 5), "b"), ((1, 0), "a"), ((0, 2), "c"), ((6, 5), "b"), ((5, 6), "b")]
check("distance 2D", lambda: distance((0, 0), (3, 4)), 5.0)
check("distance 4D", lambda: distance((1, 1, 1, 1), (2, 2, 2, 2)), 2.0)
check("k_nearest_labels", lambda: k_nearest_labels((0, 0), toy, 2), ["a", "c"])
check("majority_vote", lambda: majority_vote(["a", "b", "b"]), "b")
check("majority_vote tie", lambda: majority_vote(["a", "b"]), "a")
check("knn_predict k=1", lambda: knn_predict((0.5, 0.5), toy, 1), "a")
check("knn_predict k=3", lambda: knn_predict((4, 4), toy, 3), "b")
check("split_data sizes", lambda: tuple(len(part) for part in split_data(list(range(10)))), (8, 2))
check("split_data doesn't change input", lambda: (split_data(list(range(10))), list(range(10)))[1], list(range(10)))
check("standardize mean ~0", lambda: round(sum(f[0] for f, _ in standardize(toy, toy)[0]), 6), 0.0)

seeds = make_seeds_data()
try:
    train, test = split_data(seeds, 0.25, seed=42)
    check("accuracy on seeds > 85%", lambda: accuracy(train, test, 5) > 0.85, True)
    print(f"\nSeeds dataset: {len(train)} train / {len(test)} test")
    for k in [1, 3, 5, 9, 15]:
        tr_s, te_s = standardize(train, test)
        print(f"  k={k:>2}: raw {accuracy(train, test, k):.1%}   scaled {accuracy(tr_s, te_s, k):.1%}")
except Exception:
    print("\nFinish all the functions to see results on the seeds dataset.")
