"""
08 - Combining Data Structures
Real data is usually a mix: lists of dicts, dicts of lists, and so on.

Which structure should I use?
  list  -> ordered items, duplicates OK, access by position       [1, 2, 2]
  tuple -> a small FIXED group that shouldn't change             (x, y)
  dict  -> look things up by a key/name                          {"Ada": 95}
  set   -> unique items, fast "is it in there?", group math      {"a", "b"}
"""

# ---- A list of dicts: each dict is one "record" (like a row in a spreadsheet) ----
students = [
    {"name": "Ada", "grade": 11, "scores": [95, 88, 92]},
    {"name": "Alan", "grade": 12, "scores": [72, 85, 90]},
    {"name": "Grace", "grade": 11, "scores": [99, 97, 100]},
]

for student in students:
    avg = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']:<6} (grade {student['grade']}): average {avg:.1f}")

# Add a new record
students.append({"name": "Linus", "grade": 10, "scores": [80]})

# Find all 11th graders
juniors = []
for s in students:
    if s["grade"] == 11:
        juniors.append(s["name"])
print("Juniors:", juniors)

print()

# ---- A dict of lists: group things by a key ----
by_grade = {}
for s in students:
    g = s["grade"]
    if g not in by_grade:
        by_grade[g] = []
    by_grade[g].append(s["name"])
print(by_grade)

print()

# ---- A 2D list (list of lists): a grid ----
board = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", "X"],
]
for row in board:
    print(" | ".join(row))
print("Center square:", board[1][1])     # row 1, column 1
