"""
Exercise 3 - Debug Me!
----------------------
This program is supposed to ask for a name and 3 test scores, then print
the average. It has FIVE bugs (a mix of syntax errors, type errors, and
logic errors).

Find and fix them all. For each one, add a comment saying what kind of
error it was.

When fixed, entering: Sam, 90, 80, 100 should print:
    Sam's average is 90.00
    Sam's highest possible bonus score is 190
"""

name = input("Student name: )
score1 = input("Score 1: ")
score2 = int(input("Score 2: "))
score3 = int(input("Score 3: "))

average = score1 + score2 + score3 / 3

print(f"{name}'s average is {average:.2f}")
print(name + "'s highest possible bonus score is " + score3 + 90)
print(f"{nme} is done!")
