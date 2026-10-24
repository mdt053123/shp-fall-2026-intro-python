"""
Exercise 4 - Dice Simulator
---------------------------
Part A: Write a function roll_two_dice() that returns the SUM of two random
        dice rolls (each 1-6).

Part B: Ask the user how many times to roll. Roll that many times and count:
          - how many times the sum was 7
          - how many times you rolled doubles-worth... actually, let's keep it
            simple: how many times the sum was 2 ("snake eyes")
        Print each count and its percentage.

Part C: Math says P(sum = 7) = 6/36 (about 16.7%) and P(sum = 2) = 1/36 (about 2.8%).
        Roll 100,000 times. How close do you get?

Example run:
    How many rolls? 100000
    Sum of 7: 16622 times (16.6%)
    Sum of 2: 2791 times (2.8%)

Hint: f"{x:.1%}" formats 0.166 as 16.6%
"""

import random

# TODO
