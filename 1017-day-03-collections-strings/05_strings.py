"""
05 - Strings as Sequences
A string is a sequence of characters, so indexing, slicing, len, 'in', and
for-loops all work just like with lists. But strings are IMMUTABLE.
"""

s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5
#   -6 -5 -4 -3 -2 -1

print(s[0], s[-1])      # P n
print(s[0:3])           # Pyt
print(s[2:])            # thon
print(s[::-1])          # nohtyP  (reverse!)
print(s[::2])           # Pto
print(len(s))           # 6
print("th" in s)        # True

# s[0] = "J"            # TypeError: strings are immutable
s2 = "J" + s[1:]        # ...so build a NEW string instead
print(s2)               # Jython

print()

# ---- Useful methods (they return NEW strings; the original is unchanged) ----
msg = "  Hello, World!  "
print(msg.strip())                 # remove spaces at both ends
print(msg.lower(), msg.upper())
print(msg.replace("World", "SHP"))
print(msg.strip().startswith("Hello"), msg.strip().endswith("!"))
print(msg.find("World"))           # index where it starts (-1 if not found)
print(msg.count("l"))

print()

# ---- Checking characters ----
print("123".isdigit(), "abc".isalpha(), "abc123".isalnum(), " ".isspace())
print("A".isupper(), "a".islower())

print()

# ---- split & join: convert between strings and lists ----
sentence = "the quick brown fox"
words = sentence.split()           # split on whitespace -> list of words
print(words)
print(len(words), "words")

date = "2026-09-26"
year, month, day = date.split("-")  # split on a specific character + unpack
print(year, month, day)

print(" ".join(["a", "b", "c"]))    # "a b c"
print("-".join(words))              # "the-quick-brown-fox"

print()

# ---- Looping over characters, building a new string ----
vowels = 0
no_vowels = ""
for ch in "programming":
    if ch in "aeiou":
        vowels += 1
    else:
        no_vowels += ch            # build a new string piece by piece
print(vowels, no_vowels)

# ---- Palindromes ----
word = "racecar"
print(word == word[::-1])          # True

# ---- Characters are secretly numbers: ord() and chr() ----
print(ord("A"), ord("a"), chr(66))  # 65 97 B
