"""
Exercise 3 - Dictionaries and Sets  (SOLUTION)
----------------------------------
Fill in each function. Run the file to see PASS/FAIL for each check.
"""


def value_counts(items):
    """Return a dict mapping each item to how many times it appears.

    value_counts([1, 1, 2, 3, 3, 3]) -> {1: 2, 2: 1, 3: 3}
    """
    # TODO
    pass


def word_frequency(text):
    """Return a dict of word -> count. Ignore case, and strip these
    punctuation marks from each word: . , ! ?

    word_frequency("The cat. The hat!") -> {"the": 2, "cat": 1, "hat": 1}
    """
    # TODO
    pass


def most_common(items):
    """Return the item that appears most often (if there's a tie, return any of them).
    Return None for an empty list. Use your value_counts function!

    most_common(["a", "b", "a"]) -> "a"
    """
    # TODO
    pass


def invert_dict(d):
    """Swap keys and values. (Assume all values are unique.)

    invert_dict({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    """
    # TODO
    pass


def common_friends(friends_a, friends_b):
    """Given two LISTS of friends, return a SORTED list of friends they share.

    common_friends(["Ada", "Alan", "Grace"], ["Grace", "Ada", "Linus"]) -> ["Ada", "Grace"]
    """
    # TODO
    pass


def are_anagrams(word1, word2):
    """Return True if the two words use exactly the same letters (ignore case).

    are_anagrams("Listen", "Silent") -> True
    are_anagrams("apple", "paple") -> True
    are_anagrams("aab", "abb") -> False    (careful! sets aren't enough here)
    """
    # TODO
    pass


def group_by_length(words):
    """Return a dict mapping word length -> list of words with that length
    (in their original order).

    group_by_length(["hi", "cat", "to", "dog"]) -> {2: ["hi", "to"], 3: ["cat", "dog"]}
    """
    # TODO
    pass


# ----------------------- Checks (don't change below) -----------------------
def check(label, actual, expected):
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("value_counts([1, 1, 2, 3, 3, 3])", value_counts([1, 1, 2, 3, 3, 3]), {1: 2, 2: 1, 3: 3})
check("value_counts([])", value_counts([]), {})
check("word_frequency('The cat. The hat!')", word_frequency("The cat. The hat!"), {"the": 2, "cat": 1, "hat": 1})
check("most_common(['a', 'b', 'a'])", most_common(["a", "b", "a"]), "a")
check("most_common([])", most_common([]), None)
check("invert_dict({'a': 1, 'b': 2})", invert_dict({"a": 1, "b": 2}), {1: "a", 2: "b"})
check("common_friends(...)", common_friends(["Ada", "Alan", "Grace"], ["Grace", "Ada", "Linus"]), ["Ada", "Grace"])
check("are_anagrams('Listen', 'Silent')", are_anagrams("Listen", "Silent"), True)
check("are_anagrams('aab', 'abb')", are_anagrams("aab", "abb"), False)
check("group_by_length(['hi', 'cat', 'to', 'dog'])", group_by_length(["hi", "cat", "to", "dog"]), {2: ["hi", "to"], 3: ["cat", "dog"]})
