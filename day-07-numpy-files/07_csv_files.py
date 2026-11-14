"""
07 - CSV Files
CSV = Comma-Separated Values: the simplest spreadsheet format.
    date,high_f,low_f,precip_in
    2025-11-01,63,50,0.0
Python's built-in csv module handles the details (quotes, commas inside values...).
"""

import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("output", exist_ok=True)

# ---- Read with csv.reader: each row is a list of STRINGS ----
with open("data/weather.csv") as f:
    reader = csv.reader(f)
    header = next(reader)                  # the first row is the header
    first_row = next(reader)
print(header)
print(first_row)                           # note: '63' is a string!

# ---- Read with csv.DictReader: each row is a dict keyed by the header ----
days = []
with open("data/weather.csv") as f:
    for row in csv.DictReader(f):
        days.append({
            "date": row["date"],
            "high": int(row["high_f"]),        # convert strings to numbers!
            "low": int(row["low_f"]),
            "precip": float(row["precip_in"]),
        })

print(len(days), "days loaded")
avg_high = sum(d["high"] for d in days) / len(days)
rainy = [d["date"] for d in days if d["precip"] > 0]
warmest = max(days, key=lambda d: d["high"])
print(f"Average high: {avg_high:.1f}°F")
print(f"Rainy days: {len(rainy)}")
print(f"Warmest: {warmest['date']} ({warmest['high']}°F)")

# ---- Write a CSV ----
with open("output/weather_summary.csv", "w", newline="") as f:   # newline="" avoids blank lines on Windows
    writer = csv.writer(f)
    writer.writerow(["date", "high_c", "low_c", "rainy"])
    for d in days:
        high_c = round((d["high"] - 32) * 5 / 9, 1)
        low_c = round((d["low"] - 32) * 5 / 9, 1)
        writer.writerow([d["date"], high_c, low_c, d["precip"] > 0])
print("Wrote output/weather_summary.csv")

# ---- NumPy can load simple numeric CSVs directly ----
import numpy as np
highs = np.loadtxt("data/weather.csv", delimiter=",", skiprows=1, usecols=1)
print("NumPy mean high:", highs.mean().round(1))

# Next week, pandas makes all of this even easier: pd.read_csv("data/weather.csv")
