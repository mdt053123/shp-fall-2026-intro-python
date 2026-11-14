"""
Exercise 3 - Sorting with key= and lambda
-----------------------------------------
Use sorted(), min(), or max() with key=lambda ... in each function.
"""


def sort_by_length(words):
    """Shortest first; words of equal length keep their original order.

    sort_by_length(["ccc", "a", "bb", "dd"]) -> ["a", "bb", "dd", "ccc"]
    """
    # TODO
    pass


def sort_by_last_name(names):
    """Each name is "First Last". Sort by LAST name.

    sort_by_last_name(["Ada Lovelace", "Alan Turing", "Grace Hopper"])
        -> ["Grace Hopper", "Ada Lovelace", "Alan Turing"]
    """
    # TODO
    pass


def leaderboard(scores):
    """scores is a list of (name, points) tuples. Sort by points HIGH to LOW;
    break ties alphabetically by name.

    leaderboard([("Bo", 5), ("Al", 9), ("Cy", 9)]) -> [("Al", 9), ("Cy", 9), ("Bo", 5)]
    """
    # TODO
    pass


def top_n(scores, n):
    """Return just the NAMES of the top n entries of leaderboard(scores).

    top_n([("Bo", 5), ("Al", 9), ("Cy", 7)], 2) -> ["Al", "Cy"]
    """
    # TODO
    pass


def youngest(people):
    """people is a list of dicts with "name" and "age". Return the NAME of the youngest.

    youngest([{"name": "Ada", "age": 36}, {"name": "Bo", "age": 9}]) -> "Bo"
    """
    # TODO
    pass


def closest_to(nums, target):
    """Return the number in nums closest to target (first one if there's a tie).

    closest_to([1, 7, 12, 20], 10) -> 12
    """
    # TODO
    pass


def most_frequent_letter(text):
    """Return the most common LETTER in text (ignore case, spaces, punctuation).
    Break ties alphabetically.

    most_frequent_letter("Hello, World") -> "l"
    """
    # TODO
    pass


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


check("sort_by_length", lambda: sort_by_length(["ccc", "a", "bb", "dd"]), ["a", "bb", "dd", "ccc"])
check("sort_by_last_name", lambda: sort_by_last_name(["Ada Lovelace", "Alan Turing", "Grace Hopper"]),
      ["Grace Hopper", "Ada Lovelace", "Alan Turing"])
check("leaderboard", lambda: leaderboard([("Bo", 5), ("Al", 9), ("Cy", 9)]), [("Al", 9), ("Cy", 9), ("Bo", 5)])
check("top_n", lambda: top_n([("Bo", 5), ("Al", 9), ("Cy", 7)], 2), ["Al", "Cy"])
check("youngest", lambda: youngest([{"name": "Ada", "age": 36}, {"name": "Bo", "age": 9}]), "Bo")
check("closest_to", lambda: closest_to([1, 7, 12, 20], 10), 12)
check("most_frequent_letter", lambda: most_frequent_letter("Hello, World"), "l")
check("most_frequent_letter tie", lambda: most_frequent_letter("ba"), "a")
