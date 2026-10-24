"""
02 - List Methods and Built-in Functions
"""

nums = [5, 2, 8]

# ---- Adding ----
nums.append(10)          # add to the END            -> [5, 2, 8, 10]
print(nums)
nums.insert(1, 99)       # insert 99 at index 1      -> [5, 99, 2, 8, 10]
print(nums)
nums.extend([1, 2])      # add several to the end    -> [5, 99, 2, 8, 10, 1, 2]
print(nums)

# ---- Removing ----
last = nums.pop()        # remove & RETURN the last item
print(last, nums)
second = nums.pop(1)     # remove & return the item at index 1
print(second, nums)
nums.remove(8)           # remove the first 8 (by VALUE); ValueError if not there
print(nums)

print()

# ---- Searching & counting ----
grades = [90, 85, 90, 72, 90]
print(grades.index(85))  # 1   (index of first 85)
print(grades.count(90))  # 3

# ---- Built-in functions that work on lists ----
print(len(grades), sum(grades), min(grades), max(grades))
print(sum(grades) / len(grades))    # average

print()

# ---- Sorting: .sort() CHANGES the list; sorted() makes a NEW one ----
scores = [72, 95, 88, 60]
new_list = sorted(scores)
print(new_list, scores)             # original unchanged
scores.sort()
print(scores)                       # now changed
scores.sort(reverse=True)
print(scores)                       # biggest first

# GOTCHA: .sort() returns None!
# scores = scores.sort()   # now scores is None... oops

scores.reverse()                    # reverse in place
print(scores)

print()

# ---- Combining lists ----
print([1, 2] + [3, 4])      # [1, 2, 3, 4]
print([0] * 5)              # [0, 0, 0, 0, 0]

# ---- list() turns other sequences into lists ----
print(list("hello"))        # ['h', 'e', 'l', 'l', 'o']
print(list(range(5)))       # [0, 1, 2, 3, 4]
