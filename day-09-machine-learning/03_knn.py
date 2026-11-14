"""
03 - k-Nearest Neighbors (k-NN)
1-NN trusts a SINGLE neighbor, so one mislabeled or unusual point can fool it.
k-NN looks at the k closest neighbors and takes a MAJORITY VOTE.

  k = 1  -> very sensitive to noise ("overfitting")
  k big  -> smoother, but can blur real boundaries ("underfitting")
  Use an ODD k for two classes to avoid ties.
"""

from collections import Counter


def distance(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q)) ** 0.5


def knn_predict(point, data, k=3):
    # 1. distance to EVERY training example
    distances = []
    for features, label in data:
        distances.append((distance(point, features), label))
    # 2. sort by distance and keep the k closest
    distances.sort(key=lambda pair: pair[0])
    nearest = distances[:k]
    # 3. majority vote
    votes = Counter(label for _, label in nearest)
    top_count = max(votes.values())
    # Tie? Pick the tied label whose member is closest (nearest is already sorted)
    for _, label in nearest:
        if votes[label] == top_count:
            return label


data = [
    ((1, 1), "red"), ((1, 2), "red"), ((2, 1), "red"), ((2, 3), "red"),
    ((6, 6), "blue"), ((7, 5), "blue"), ((6, 8), "blue"), ((8, 7), "blue"),
    ((9, 1), "green"), ((8, 2), "green"), ((9, 3), "green"),
    ((3, 2), "blue"),        # <- a NOISY point: a "blue" sitting among the reds
]

point = (3, 1.5)
for k in [1, 3, 5]:
    print(f"k={k}: {point} -> {knn_predict(point, data, k)}")
# k=1 is fooled by the noisy blue point; k=3 and k=5 out-vote it.


def show_map(k):
    print(f"\nPrediction map with k = {k}:")
    for y in range(10, -1, -1):
        print(f"{y:>2} " + " ".join(knn_predict((x, y), data, k)[0] for x in range(11)))


show_map(1)
show_map(5)
