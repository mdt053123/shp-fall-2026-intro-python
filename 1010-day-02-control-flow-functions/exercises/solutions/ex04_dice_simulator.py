"""Solution - Exercise 4: Dice Simulator"""

import random


def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)


rolls = int(input("How many rolls? "))

sevens = 0
snake_eyes = 0
for i in range(rolls):
    total = roll_two_dice()
    if total == 7:
        sevens += 1
    elif total == 2:
        snake_eyes += 1

print(f"Sum of 7: {sevens} times ({sevens / rolls:.1%})")
print(f"Sum of 2: {snake_eyes} times ({snake_eyes / rolls:.1%})")
print(f"Expected: 7 -> {6 / 36:.1%}, 2 -> {1 / 36:.1%}")
