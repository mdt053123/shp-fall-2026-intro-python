"""
Exercise 4 - Exceptions
-----------------------
Use try/except (and raise) to make these functions robust.
"""


def parse_int(text, default=0):
    """Convert text to an int. If that's impossible, return default instead.

    parse_int("42") -> 42,   parse_int("hi") -> 0,   parse_int("hi", -1) -> -1
    """
    # TODO
    pass


def average_of_valid(values):
    """values is a list of strings. Return the average of the ones that are valid
    numbers (int OR float), skipping the rest. Return None if none are valid.

    average_of_valid(["10", "abc", "20", "3.5.1", "30"]) -> 20.0
    """
    # TODO
    pass


def safe_get(items, index):
    """Return items[index], or None if the index is out of range.
    Use try/except IndexError (not an if statement!).

    safe_get([1, 2, 3], 1) -> 2,   safe_get([1, 2, 3], 10) -> None
    """
    # TODO
    pass


def make_username(name):
    """Return name lowercased with spaces replaced by underscores.
    RAISE a ValueError if name is empty/only spaces, or contains a digit.

    make_username("Ada Lovelace") -> "ada_lovelace"
    make_username("R2D2") -> raises ValueError
    """
    # TODO
    pass


def raises_value_error(func, arg):  # given
    """Helper for the checks: True if func(arg) raises ValueError."""
    try:
        func(arg)
    except ValueError:
        return True
    return False


# ----------------------- Checks (don't change below) -----------------------
def check(label, get_actual, expected):
    try:
        actual = get_actual()
    except Exception as e:
        print(f"FAIL  {label}: crashed with {type(e).__name__}: {e}")
        return
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("parse_int('42')", lambda: parse_int("42"), 42)
check("parse_int('hi')", lambda: parse_int("hi"), 0)
check("parse_int('hi', -1)", lambda: parse_int("hi", -1), -1)
check("average_of_valid", lambda: average_of_valid(["10", "abc", "20", "3.5.1", "30"]), 20.0)
check("average_of_valid none", lambda: average_of_valid(["x", "y"]), None)
check("safe_get ok", lambda: safe_get([1, 2, 3], 1), 2)
check("safe_get out of range", lambda: safe_get([1, 2, 3], 10), None)
check("make_username", lambda: make_username("Ada Lovelace"), "ada_lovelace")
check("make_username('R2D2') raises", lambda: raises_value_error(make_username, "R2D2"), True)
check("make_username('   ') raises", lambda: raises_value_error(make_username, "   "), True)
