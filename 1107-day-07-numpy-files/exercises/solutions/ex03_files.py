"""
Exercise 3 - Files  (SOLUTION)
------------------
These functions read ../data/ files and write to an output/ folder.
Always use `with open(...) as f:`.
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")          # the day's data/ folder
if not os.path.isdir(DATA):                       # (solutions/ is one folder deeper)
    DATA = os.path.join(HERE, "..", "..", "data")
OUTPUT = os.path.join(HERE, "output")
os.makedirs(OUTPUT, exist_ok=True)


def file_stats(path):
    """Return (lines, words, characters) for a text file, like the Unix 'wc' command.
    lines = number of lines, words = len(text.split()), characters = len(text)."""
    with open(path) as f:
        text = f.read()
    return (len(text.splitlines()), len(text.split()), len(text))


def longest_line(path):
    """Return the longest line in the file (without its trailing newline)."""
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f]
    return max(lines, key=len)


def write_times_table(path, n):
    """Write an n x n multiplication table: each row's numbers separated by tabs.
    For n=3 the file is:
        1\t2\t3
        2\t4\t6
        3\t6\t9
    """
    with open(path, "w") as f:
        for r in range(1, n + 1):
            f.write("\t".join(str(r * c) for c in range(1, n + 1)) + "\n")


def read_times_table(path):
    """Read a file written by write_times_table back into a list of lists of ints."""
    with open(path) as f:
        return [[int(x) for x in line.split("\t")] for line in f if line.strip()]


def rainy_days(csv_path):
    """Read weather.csv and return a list of dates where precip_in > 0."""
    with open(csv_path) as f:
        return [row["date"] for row in csv.DictReader(f) if float(row["precip_in"]) > 0]


def biggest_swing(csv_path):
    """Return (date, swing) for the day with the largest high_f - low_f difference."""
    with open(csv_path) as f:
        rows = list(csv.DictReader(f))
    best = max(rows, key=lambda r: int(r["high_f"]) - int(r["low_f"]))
    return (best["date"], int(best["high_f"]) - int(best["low_f"]))


def append_log(path, message):
    """Append message as a new line at the end of the file (create it if needed).
    Return the number of lines now in the file."""
    with open(path, "a") as f:
        f.write(message + "\n")
    with open(path) as f:
        return len(f.readlines())


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


poem = os.path.join(DATA, "poem.txt")
weather = os.path.join(DATA, "weather.csv")
table = os.path.join(OUTPUT, "table.txt")
log = os.path.join(OUTPUT, "log.txt")
if os.path.exists(log):
    os.remove(log)

check("file_stats(poem)", lambda: file_stats(poem), (16, 89, 411))
check("longest_line(poem)", lambda: longest_line(poem), "And sweetest - in the Gale - is heard -")
check("times table round trip", lambda: (write_times_table(table, 4), read_times_table(table))[1],
      [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])
check("rainy_days", lambda: len(rainy_days(weather)), 4)
check("biggest_swing", lambda: biggest_swing(weather)[1], 18)
check("append_log 1", lambda: append_log(log, "first"), 1)
check("append_log 2", lambda: append_log(log, "second"), 2)
