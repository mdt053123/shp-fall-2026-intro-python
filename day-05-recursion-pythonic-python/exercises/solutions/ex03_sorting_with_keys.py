"""
Exercise 3 - Sorting with key= and lambda  (SOLUTION)
-----------------------------------------
Use sorted(), min(), or max() with key=lambda ... in each function.
"""


def sort_by_length(words):
    """Shortest first; words of equal length keep their original order.

    sort_by_length(["ccc", "a", "bb", "dd"]) -> ["a", "bb", "dd", "ccc"]
    """
    return sorted(words, key=len)


def sort_by_last_name(names):
    """Each name is "First Last". Sort by LAST name.

    sort_by_last_name(["Ada Lovelace", "Alan Turing", "Grace Hopper"])
        -> ["Grace Hopper", "Ada Lovelace", "Alan Turing"]
    """
    return sorted(names, key=lambda n: n.split()[-1])


def leaderboard(scores):
    """scores is a list of (name, points) tuples. Sort by points HIGH to LOW;
    break ties alphabetically by name.

    leaderboard([("Bo", 5), ("Al", 9), ("Cy", 9)]) -> [("Al", 9), ("Cy", 9), ("Bo", 5)]
    """
    return sorted(scores, key=lambda s: (-s[1], s[0]))


def top_n(scores, n):
    """Return just the NAMES of the top n entries of leaderboard(scores).

    top_n([("Bo", 5), ("Al", 9), ("Cy", 7)], 2) -> ["Al", "Cy"]
    """
    return [name for name, points in leaderboard(scores)[:n]]


def youngest(people):
    """people is a list of dicts with "name" and "age". Return the NAME of the youngest.

    youngest([{"name": "Ada", "age": 36}, {"name": "Bo", "age": 9}]) -> "Bo"
    """
    return min(people, key=lambda p: p["age"])["name"]


def closest_to(nums, target):
    """Return the number in nums closest to target (first one if there's a tie).

    closest_to([1, 7, 12, 20], 10) -> 12
    """
    return min(nums, key=lambda x: abs(x - target))


def most_frequent_letter(text):
    """Return the most common LETTER in text (ignore case, spaces, punctuation).
    Break ties alphabetically.

    most_frequent_letter("Hello, World") -> "l"
    """
    counts = {}
    for ch in text.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    return min(counts, key=lambda ch: (-counts[ch], ch))


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
