"""
02 - References, == vs is, and Mutability
A variable doesn't HOLD an object. It REFERS (points) to one.
Two variables can point to the SAME object. This matters a lot for mutable objects!
"""

# ---- == compares VALUES; 'is' checks if it's the SAME object ----
a = [1, 2, 3]
b = [1, 2, 3]
c = a                   # c points to the SAME list as a (no copy is made!)

print(a == b)           # True:  same contents
print(a is b)           # False: two different list objects
print(a is c)           # True:  same object

print()

# ---- Aliasing: changing the object through one name shows up through the other ----
c.append(4)
print(a)                # [1, 2, 3, 4]  <- a changed too! a and c are the same list
print(b)                # [1, 2, 3]     <- b is a separate list

# ---- To get an independent copy, copy it explicitly ----
d = a.copy()            # or a[:] or list(a)
d.append(99)
print(a, d)             # a is unaffected

print()

# ---- Immutable objects (int, str, tuple) can't be changed, so aliasing is harmless ----
x = "hi"
y = x
y = y + "!"             # creates a NEW string; x still points to the old one
print(x, y)

print()

# ---- Functions receive REFERENCES: a function can change a list you pass in! ----
def add_bonus(scores):
    for i in range(len(scores)):
        scores[i] += 5            # modifies the caller's list

my_scores = [80, 90]
add_bonus(my_scores)
print(my_scores)                  # [85, 95] <- changed!

def add_bonus_safely(scores):
    new_scores = []
    for s in scores:
        new_scores.append(s + 5)
    return new_scores             # returns a NEW list; original untouched

original = [80, 90]
bonus = add_bonus_safely(original)
print(original, bonus)

print()

# ---- Classic gotcha: a grid built with * shares the SAME row ----
grid = [[0] * 3] * 3             # 3 references to ONE row!
grid[0][0] = 1
print(grid)                       # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  (!)

grid = [[0] * 3 for _ in range(3)]   # 3 separate rows (a comprehension; more on Day 5)
grid[0][0] = 1
print(grid)
