"""
07 - Exceptions: Handling Errors Gracefully
Instead of crashing, CATCH errors and respond.
    try:      code that might fail
    except:   what to do if it fails
    else:     runs only if nothing failed
    finally:  ALWAYS runs
"""

# ---- Catching a specific error ----
text = "twelve"
try:
    n = int(text)
    print("Got", n)
except ValueError:
    print(f"'{text}' is not a whole number")

# ---- Several except blocks ----
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")
        return None
    except TypeError:
        print("Both values must be numbers!")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "2"))

print()

# ---- else and finally ----
for value in ["42", "oops"]:
    try:
        number = int(value)
    except ValueError as e:              # 'as e' gives you the error object
        print("Error:", e)
    else:
        print("Success:", number)
    finally:
        print("  (finished trying", repr(value) + ")")

print()

# ---- The #1 use: robust user input ----
def get_int(prompt, low, high):
    """Keep asking until the user enters a whole number from low to high."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"  Must be between {low} and {high}.")

age = get_int("Enter your age (1-120): ", 1, 120)
print("Thanks! Age =", age)

print()

# ---- RAISING your own exceptions: refuse bad data ----
def set_score(score):
    if not 0 <= score <= 100:
        raise ValueError(f"score must be 0-100, got {score}")
    return score

try:
    set_score(105)
except ValueError as e:
    print("Rejected:", e)

# Common exception types:
#   ValueError (bad value), TypeError (wrong type), KeyError (missing dict key),
#   IndexError (bad list index), ZeroDivisionError, FileNotFoundError (Day 7)
# Tip: catch SPECIFIC errors. A bare 'except:' hides bugs you'd want to see.
