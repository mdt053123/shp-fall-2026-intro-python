"""
01 - Distance: The Heart of "Similarity"
Many ML methods ask: "Which examples are MOST SIMILAR to this one?"
If each example is a list of numbers (features), similar = CLOSE together.

Euclidean distance (the Pythagorean theorem, in any number of dimensions):
    d(p, q) = sqrt( (p1-q1)^2 + (p2-q2)^2 + ... + (pn-qn)^2 )
"""


def distance_2d(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5


def distance(p, q):
    """Works for ANY number of dimensions."""
    return sum((a - b) ** 2 for a, b in zip(p, q)) ** 0.5


print(distance_2d((0, 0), (3, 4)))          # 5.0
print(distance((0, 0), (3, 4)))             # 5.0
print(distance((1, 2, 3), (4, 6, 3)))       # 5.0 (3D)

print()

# ---- Example: which fruit is this mystery fruit most similar to? ----
# Features: (weight in grams, sweetness 1-10)
fruits = {
    "apple": (150, 7),
    "lemon": (100, 2),
    "watermelon": (5000, 8),
    "grape": (5, 8),
}
mystery = (130, 6)
for name, features in fruits.items():
    print(f"{name:<11} distance = {distance(mystery, features):8.1f}")

# ---- A problem: SCALE ----
# Weight (hundreds of grams) completely dominates sweetness (1-10), so sweetness
# barely matters! Fix: put every feature on a similar scale before measuring distance.
# We'll see this matter a LOT in 04_train_test_accuracy.py.
