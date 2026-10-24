"""
Exercise 2 - StringAnalyzer Class  (SOLUTION)
---------------------------------
A class that wraps a piece of text and answers questions about it.

  sa = StringAnalyzer("Never odd or even")
  sa.word_count()           -> 4
  sa.is_palindrome()        -> True   (ignore case and spaces)
  sa.char_frequency()       -> dict of letter -> count (lowercase letters only)
  sa.most_common_letter()   -> "e"
  sa.contains("odd")        -> True   (write it WITHOUT using 'in' on strings
                                       or .find(): compare slices yourself!)
  sa.longest_word()         -> "Never" (first one if there's a tie)
  len(sa)                   -> 17     (length of the text)
"""


class StringAnalyzer:
    def __init__(self, text):  # given
        self.text = text

    def word_count(self):
        # TODO
        pass

    def is_palindrome(self):
        # TODO
        pass

    def char_frequency(self):
        # TODO
        pass

    def most_common_letter(self):
        # TODO
        pass

    def contains(self, sub):
        # TODO
        pass

    def longest_word(self):
        # TODO
        pass

    def __len__(self):
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


sa = StringAnalyzer("Never odd or even")
check("word_count", lambda: sa.word_count(), 4)
check("is_palindrome", lambda: sa.is_palindrome(), True)
check("is_palindrome (no)", lambda: StringAnalyzer("Python").is_palindrome(), False)
check("char_frequency()['e']", lambda: sa.char_frequency()["e"], 4)
check("most_common_letter", lambda: sa.most_common_letter(), "e")
check("contains('odd')", lambda: sa.contains("odd"), True)
check("contains('xyz')", lambda: sa.contains("xyz"), False)
check("contains('even')", lambda: sa.contains("even"), True)
check("longest_word", lambda: sa.longest_word(), "Never")
check("len", lambda: len(sa), 17)
