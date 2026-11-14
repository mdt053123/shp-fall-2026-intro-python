"""
05 - Linear Regression From Scratch
Classification predicts a CATEGORY (species). Regression predicts a NUMBER.

Find the best-fit line  y = m*x + b  through the data, where "best" means it
minimizes the squared vertical errors (the "least squares" line):

    m = sum((x - x_mean) * (y - y_mean)) / sum((x - x_mean)^2)
    b = y_mean - m * x_mean

Question: can we predict a penguin's BODY MASS from its FLIPPER LENGTH?
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def mean(values):
    return sum(values) / len(values)


def fit_line(xs, ys):
    x_bar, y_bar = mean(xs), mean(ys)
    numerator = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys))
    denominator = sum((x - x_bar) ** 2 for x in xs)
    m = numerator / denominator
    b = y_bar - m * x_bar
    return m, b


def predict(m, b, x):
    return m * x + b


def mse(ys, predictions):
    """Mean squared error: the average of (error)^2. Lower is better."""
    return mean([(y - p) ** 2 for y, p in zip(ys, predictions)])


def r_squared(ys, predictions):
    """R^2: the fraction of the variation in y that the model explains.
    1.0 = perfect, 0.0 = no better than always guessing the average."""
    y_bar = mean(ys)
    total = sum((y - y_bar) ** 2 for y in ys)
    unexplained = sum((y - p) ** 2 for y, p in zip(ys, predictions))
    return 1 - unexplained / total


# ---- Tiny example first ----
xs = [1, 2, 3, 4, 5]
ys = [2, 4, 5, 4, 5]
m, b = fit_line(xs, ys)
print(f"Tiny example: y = {m:.2f}x + {b:.2f}")

# ---- Penguins ----
flippers, masses = [], []
with open(os.path.join(HERE, "data", "penguins.csv")) as f:
    for row in csv.DictReader(f):
        if row["flipper_length_mm"] and row["body_mass_g"]:
            flippers.append(float(row["flipper_length_mm"]))
            masses.append(float(row["body_mass_g"]))

m, b = fit_line(flippers, masses)
print(f"\nPenguins: mass = {m:.1f} * flipper + ({b:.1f})")
print(f"Meaning: each extra mm of flipper adds about {m:.0f} g of body mass.")

preds = [predict(m, b, x) for x in flippers]
print(f"MSE:  {mse(masses, preds):,.0f}   (typical error is about {mse(masses, preds) ** 0.5:.0f} g)")
print(f"R^2:  {r_squared(masses, preds):.3f}")

for flipper in [180, 200, 220]:
    print(f"  a penguin with {flipper} mm flippers probably weighs about {predict(m, b, flipper):,.0f} g")

# ---- Check against NumPy's built-in fit ----
import numpy as np
m_np, b_np = np.polyfit(flippers, masses, deg=1)
print(f"\nNumPy polyfit agrees: m = {m_np:.1f}, b = {b_np:.1f}")

# ---- Plot it (close the window to finish) ----
import matplotlib.pyplot as plt
plt.scatter(flippers, masses, alpha=0.5, label="penguins")
line_x = [min(flippers), max(flippers)]
plt.plot(line_x, [predict(m, b, x) for x in line_x], color="red", label="best-fit line")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.legend()
plt.title(f"mass = {m:.1f} * flipper + {b:.0f}   (R^2 = {r_squared(masses, preds):.2f})")
plt.show()
