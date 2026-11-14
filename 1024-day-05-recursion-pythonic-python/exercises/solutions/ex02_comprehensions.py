"""
Exercise 2 - Comprehensions  (SOLUTION)
---------------------------
Write each function body as a SINGLE return statement using a list/dict/set
comprehension (or sum/any/all with a generator).
"""


def squares_of_evens(nums):
    """squares_of_evens([1, 2, 3, 4]) -> [4, 16]"""
    return [n * n for n in nums if n % 2 == 0]


def shout_long_words(words, min_len):
    """Uppercase every word with at least min_len letters.

    shout_long_words(["hi", "there", "python"], 5) -> ["THERE", "PYTHON"]
    """
    return [w.upper() for w in words if len(w) >= min_len]


def word_lengths(sentence):
    """Return a dict word -> length for each word in the sentence.

    word_lengths("to be or not") -> {"to": 2, "be": 2, "or": 2, "not": 3}
    """
    return {w: len(w) for w in sentence.split()}


def initials(names):
    """Return the SET of first letters of the names.

    initials(["Ada", "Alan", "Grace"]) -> {"A", "G"}
    """
    return {name[0] for name in names}


def passing(scores, cutoff):
    """Given a dict name -> score, return a dict with only the students >= cutoff.

    passing({"Ada": 95, "Alan": 60}, 65) -> {"Ada": 95}
    """
    return {name: s for name, s in scores.items() if s >= cutoff}


def multiplication_table(n):
    """Return an n x n table (list of lists) where entry [r][c] = (r+1)*(c+1).

    multiplication_table(3) -> [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    """
    return [[(r + 1) * (c + 1) for c in range(n)] for r in range(n)]


def transpose(matrix):
    """Flip rows and columns.

    transpose([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
    """
    return [[row[c] for row in matrix] for c in range(len(matrix[0]))]


def count_vowels(text):
    """Use sum() with a generator: count vowels in text.

    count_vowels("comprehension") -> 5
    """
    return sum(1 for ch in text.lower() if ch in "aeiou")


def all_positive(nums):
    """Use all(): return True if every number is > 0.

    all_positive([3, 1, 2]) -> True
    """
    return all(n > 0 for n in nums)


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


check("squares_of_evens", lambda: squares_of_evens([1, 2, 3, 4]), [4, 16])
check("shout_long_words", lambda: shout_long_words(["hi", "there", "python"], 5), ["THERE", "PYTHON"])
check("word_lengths", lambda: word_lengths("to be or not"), {"to": 2, "be": 2, "or": 2, "not": 3})
check("initials", lambda: initials(["Ada", "Alan", "Grace"]), {"A", "G"})
check("passing", lambda: passing({"Ada": 95, "Alan": 60, "Grace": 65}, 65), {"Ada": 95, "Grace": 65})
check("multiplication_table(3)", lambda: multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
check("transpose", lambda: transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
check("count_vowels", lambda: count_vowels("comprehension"), 5)
check("all_positive yes", lambda: all_positive([3, 1, 2]), True)
check("all_positive no", lambda: all_positive([3, -1, 2]), False)
