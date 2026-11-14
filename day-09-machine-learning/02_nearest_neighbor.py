"""
02 - Nearest Neighbor Classification (1-NN)
To label a new point, find the CLOSEST labeled point and copy its label.
"Tell me who your neighbor is, and I'll tell you who you are."

This is SUPERVISED learning: we learn from examples that already have answers (labels).
"""

# Training data: ((x, y), label)
data = [
    ((1, 1), "red"), ((1, 2), "red"), ((2, 1), "red"), ((2, 3), "red"),
    ((6, 6), "blue"), ((7, 5), "blue"), ((6, 8), "blue"), ((8, 7), "blue"),
    ((9, 1), "green"), ((8, 2), "green"), ((9, 3), "green"),
]


def distance(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q)) ** 0.5


def nearest_neighbor(point, data):
    """Return the label of the training example closest to point."""
    best_label = None
    best_dist = float("inf")                 # "infinity": anything is closer than this
    for features, label in data:
        d = distance(point, features)
        if d < best_dist:
            best_dist = d
            best_label = label
    return best_label


for p in [(2, 2), (7, 7), (9, 2), (5, 4)]:
    print(p, "->", nearest_neighbor(p, data))

# NOTE: we do NOT add the new point to the training data. The model should only
# learn from examples whose TRUE label we know, not from its own guesses.

# ---- A "map" of what the model predicts everywhere on the grid ----
print("\nPrediction map (r = red, b = blue, g = green, CAPITALS = training points):")
training = {features: label for features, label in data}
for y in range(10, -1, -1):
    row = ""
    for x in range(11):
        if (x, y) in training:
            row += training[(x, y)][0].upper() + " "
        else:
            row += nearest_neighbor((x, y), data)[0] + " "
    print(f"{y:>2} {row}")
print("   " + " ".join(str(x % 10) for x in range(11)))
