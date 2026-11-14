"""
04 - Tuples
Like lists, but IMMUTABLE (can't be changed after creation). Written with ( ).
Use them for small, fixed groups of values: coordinates, RGB colors, (name, score) pairs...
"""

point = (3, 4)
color = (255, 128, 0)

print(point[0], point[1])     # indexing works just like lists
print(len(color))

# point[0] = 10               # TypeError: 'tuple' object does not support item assignment

# ---- Unpacking: pull values out into separate variables ----
x, y = point
print(f"x = {x}, y = {y}")

r, g, b = color
print(r, g, b)

# ---- Swap two variables (this uses tuples behind the scenes) ----
a, b = 1, 2
a, b = b, a
print(a, b)                   # 2 1

# ---- Functions returning multiple values actually return a tuple ----
def min_max(nums):
    return min(nums), max(nums)

result = min_max([4, 1, 9])
print(result, type(result))   # (1, 9) <class 'tuple'>
low, high = min_max([4, 1, 9])

print()

# ---- Distance between two points ----
def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

print(distance((0, 0), (3, 4)))   # 5.0

# ---- A list of tuples is a very common structure ----
leaderboard = [("Ada", 95), ("Alan", 88), ("Grace", 97)]
for name, score in leaderboard:    # unpack each tuple in the loop
    print(f"{name}: {score}")

print()

# ---- Gotcha: a 1-item tuple needs a trailing comma ----
not_a_tuple = (5)       # just the int 5 in parentheses
one_tuple = (5,)
print(type(not_a_tuple), type(one_tuple))
