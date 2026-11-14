"""
02 - Print Output
Escape sequences, quotes, multi-line strings, and print's sep/end options.
"""

# ---- Escape sequences: special characters that start with a backslash ----
print("Line 1\nLine 2")        # \n = new line
print("Name:\tMichael")        # \t = tab
print("A backslash: \\")       # \\ = a single backslash
print("She said \"hi\"")       # \" = a double quote inside double quotes

print()  # an empty print() prints a blank line

# ---- Single vs double quotes: both make strings ----
print('Single quotes work')
print("Double quotes work too")
print('Use one kind to hold the other: "like this"')
print("It's easier with double quotes when you need an apostrophe")

print()

# ---- Triple quotes: strings that span multiple lines ----
print("""Roses are red,
Violets are blue,
Python is readable,
And so are you.""")

print()

# ---- print() can take several values, separated by commas ----
print("I am", 16, "years old")            # separates with a space by default
print("2026", "09", "26", sep="-")        # sep= changes the separator
print("No newline here...", end="")       # end= changes what goes at the end
print(" ...see, same line!")
