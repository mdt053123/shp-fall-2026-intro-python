"""
Exercise 5 (CHALLENGE) - Hangman
--------------------------------
Build a game of Hangman.

  1. The computer picks a random secret word from a list (random.choice).
  2. Show the word as underscores, revealing letters that have been guessed:
         _ y t h _ n
  3. Each turn, the player guesses ONE letter.
       - Reject guesses that aren't a single letter, or were already guessed.
       - Keep track of guessed letters in a SET.
       - A wrong guess costs a life (start with 6).
  4. The player wins when every letter is revealed, and loses at 0 lives.
     Either way, reveal the word at the end.

Helpful pieces:
  - display = " ".join(ch if ch in guessed else "_" for ch in word) -- or build it with a loop!
  - set(word) <= guessed   is True when every letter of word has been guessed

Bonus: print an ASCII-art hangman that grows with each wrong guess.
"""

import random

WORDS = ["python", "variable", "function", "dictionary", "loop", "string",
         "boolean", "integer", "algorithm", "recursion"]

# TODO
