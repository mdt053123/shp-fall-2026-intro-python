"""Solution - Exercise 5 (Challenge): Hangman (with ASCII-art bonus)"""

import random

WORDS = ["python", "variable", "function", "dictionary", "loop", "string",
         "boolean", "integer", "algorithm", "recursion"]

STAGES = [
    "  +---+\n      |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n  |   |\n      |\n     ===",
    "  +---+\n  O   |\n /|   |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ===",
]


def display(word, guessed):
    shown = []
    for ch in word:
        if ch in guessed:
            shown.append(ch)
        else:
            shown.append("_")
    return " ".join(shown)


def play():
    word = random.choice(WORDS)
    guessed = set()
    lives = 6

    while lives > 0 and not set(word) <= guessed:
        print(STAGES[6 - lives])
        print(display(word, guessed))
        print(f"Lives: {lives}   Guessed: {' '.join(sorted(guessed))}")

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that!\n")
            continue

        guessed.add(guess)
        if guess in word:
            print("Yes!\n")
        else:
            lives -= 1
            print("Nope.\n")

    if lives > 0:
        print(f"You win! The word was '{word}'.")
    else:
        print(STAGES[6])
        print(f"Out of lives! The word was '{word}'.")


play()
