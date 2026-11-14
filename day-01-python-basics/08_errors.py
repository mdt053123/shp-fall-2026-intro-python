"""
08 - Errors (and how to read them)
Uncomment ONE error at a time, run the file, and read the message.

How to read an error message (a "traceback"):
  1. Look at the LAST line first: it names the error type and describes it.
  2. Look for the LINE NUMBER: it tells you where Python got stuck.
  3. The mistake is usually on that line or the line right before it.
"""

# ---- 1. SyntaxError: the code isn't valid Python (typo, missing quote, bracket...) ----
# The program won't run AT ALL until you fix it.
# print("Hello)

# ---- 2. NameError: using a name Python doesn't know ----
# Often a typo, or using a variable before creating it.
# print(scroe)

# ---- 3. TypeError: an operation on the wrong type ----
# print("Age: " + 16)

# ---- 4. ValueError: right type, but a bad value ----
# int("twelve")

# ---- 5. ZeroDivisionError ----
# print(10 / 0)

# ---- 6. IndentationError: unexpected spaces at the start of a line ----
#   print("indented for no reason")

# ---- 7. Logic error: NO error message, but the answer is WRONG ----
# This is the sneakiest kind. The only way to catch it is to TEST your code.
a = 80
b = 90
average = a + b / 2          # BUG: should be (a + b) / 2
print("Average:", average)   # prints 125.0 -- obviously wrong!
