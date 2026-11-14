"""
04 - Does It Actually Work? Train/Test Split, Accuracy, and Scaling
Real penguins! Predict SPECIES from (bill length, bill depth, flipper length, body mass).

The golden rule of ML: NEVER test on the data you trained on.
  - Split the data: ~80% TRAINING (the model learns from these)
                    ~20% TESTING  (hidden until the end, like a final exam)
  - accuracy = (correct predictions) / (total predictions) on the TEST set
"""

import csv
import os
import random
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def distance(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q)) ** 0.5


def knn_predict(point, data, k=5):
    nearest = sorted(data, key=lambda ex: distance(point, ex[0]))[:k]
    return Counter(label for _, label in nearest).most_common(1)[0][0]


def accuracy(model_data, test_data, k):
    correct = 0
    for features, true_label in test_data:
        if knn_predict(features, model_data, k) == true_label:
            correct += 1
    return correct / len(test_data)


# ---- Load the data (skipping rows with missing values) ----
FEATURES = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
examples = []
with open(os.path.join(HERE, "data", "penguins.csv")) as f:
    for row in csv.DictReader(f):
        if all(row[c] for c in FEATURES):
            features = tuple(float(row[c]) for c in FEATURES)
            examples.append((features, row["species"]))
print(len(examples), "penguins loaded. Example:", examples[0])

# ---- Split into train and test ----
random.seed(42)                       # so everyone gets the same split
random.shuffle(examples)              # shuffle first! (the file is sorted by species)
cut = int(0.8 * len(examples))
train, test = examples[:cut], examples[cut:]
print(f"train: {len(train)}   test: {len(test)}")

# ---- Baseline: always guess the most common species ----
most_common = Counter(label for _, label in train).most_common(1)[0][0]
baseline = sum(1 for _, label in test if label == most_common) / len(test)
print(f"\nBaseline (always guess {most_common}): {baseline:.1%}")

# ---- k-NN on the raw features ----
for k in [1, 5, 15]:
    print(f"k-NN (raw features),    k={k:>2}: {accuracy(train, test, k):.1%}")

# ---- The scaling problem ----
# body_mass_g is in the THOUSANDS; bill_depth_mm is around 15-20. Distances are
# dominated by body mass, so the other features barely count!
# Fix: STANDARDIZE each feature -> (value - mean) / std, using TRAINING stats only.
n_features = len(FEATURES)
means = [sum(f[i] for f, _ in train) / len(train) for i in range(n_features)]
stds = [(sum((f[i] - means[i]) ** 2 for f, _ in train) / len(train)) ** 0.5 for i in range(n_features)]


def scale(features):
    return tuple((features[i] - means[i]) / stds[i] for i in range(n_features))


train_scaled = [(scale(f), label) for f, label in train]
test_scaled = [(scale(f), label) for f, label in test]
print()
for k in [1, 5, 15]:
    print(f"k-NN (scaled features), k={k:>2}: {accuracy(train_scaled, test_scaled, k):.1%}")

# Lesson: the SAME algorithm goes from decent to excellent just by preparing the data well.
