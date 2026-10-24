"""
10 - Guess the Number
Putting it all together: functions, loops, conditionals, random, and input.
"""

import random


def get_guess(low, high):
    """Keep asking until the user types a whole number between low and high."""
    while True:
        text = input(f"Guess a number ({low}-{high}): ")
        if not text.isdigit():               # .isdigit() is True if every char is 0-9
            print("  Please type a whole number.")
        elif not (low <= int(text) <= high):
            print(f"  Out of range! Pick from {low} to {high}.")
        else:
            return int(text)


def play(low=1, high=100):
    secret = random.randint(low, high)
    attempts = 0

    while True:
        guess = get_guess(low, high)
        attempts += 1

        if guess < secret:
            print("  Too low!")
        elif guess > secret:
            print("  Too high!")
        else:
            print(f"  You got it in {attempts} guesses!")
            return attempts


play()
