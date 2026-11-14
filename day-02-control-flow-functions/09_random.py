"""
09 - The random Module
'import' loads extra tools. The random module makes random numbers and choices.
"""

import random

# random.randint(a, b): random integer from a to b, INCLUDING both ends
die = random.randint(1, 6)
print("You rolled a", die)

# random.random(): random float from 0.0 up to (not including) 1.0
print("Random float:", random.random())

# random.choice(sequence): pick one item
print("Computer picks:", random.choice(["rock", "paper", "scissors"]))
print("Random letter:", random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

print()

# ---- Simulation: flip a coin 1000 times ----
heads = 0
flips = 1000
for i in range(flips):
    if random.randint(0, 1) == 1:
        heads += 1
print(f"Heads: {heads} out of {flips} ({heads / flips:.1%})")   # :.1% formats as a percent

# ---- Seeds: make "random" results repeatable (useful for testing) ----
random.seed(42)
print(random.randint(1, 100), random.randint(1, 100))
random.seed(42)
print(random.randint(1, 100), random.randint(1, 100))   # same two numbers again!
