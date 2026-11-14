"""
01 - Lists
An ORDERED, CHANGEABLE (mutable) collection of values.
"""

nums = [3, 7, -4, 5, 9]
names = ["Ada", "Alan", "Grace"]
mixed = ["hi", 42, True, 3.5]      # lists can hold any mix of types
empty = []

# ---- Indexing: positions start at 0! ----
#   index:   0   1   2   3   4
#   nums  = [3,  7, -4,  5,  9]
#   neg:    -5  -4  -3  -2  -1
print(nums[0])       # 3   first
print(nums[2])       # -4
print(nums[-1])      # 9   last
print(nums[-2])      # 5   second to last
# print(nums[5])     # IndexError: list index out of range

print(len(nums))     # 5   number of items

# ---- Lists are MUTABLE: you can change items ----
nums[0] = 100
print(nums)          # [100, 7, -4, 5, 9]

# ---- Membership with 'in' ----
print("Ada" in names)       # True
print("Linus" in names)     # False

print()

# ---- Slicing: list[start:stop:step] makes a NEW list (stop not included) ----
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[1:4])    # ['b', 'c', 'd']
print(letters[:3])     # ['a', 'b', 'c']   (from the start)
print(letters[3:])     # ['d', 'e', 'f']   (to the end)
print(letters[::2])    # ['a', 'c', 'e']   (every 2nd)
print(letters[::-1])   # reversed copy

print()

# ---- Three ways to loop over a list ----
# 1. for-each: when you just need the items
for name in names:
    print(name, end=" ")
print()

# 2. for with range(len(...)): when you need the INDEX
for i in range(len(names)):
    print(i, names[i], end=" | ")
print()

# 3. while with an index: when you need full control
i = 0
while i < len(names):
    print(names[i], end=" ")
    i += 1
print()
