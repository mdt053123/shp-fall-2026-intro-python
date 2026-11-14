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
        return len(self.text.split())

    def is_palindrome(self):
        cleaned = ""
        for ch in self.text.lower():
            if ch.isalnum():
                cleaned += ch
        return cleaned == cleaned[::-1]

    def char_frequency(self):
        counts = {}
        for ch in self.text.lower():
            if ch.isalpha():
                counts[ch] = counts.get(ch, 0) + 1
        return counts

    def most_common_letter(self):
        counts = self.char_frequency()
        best = None
        for ch, n in counts.items():
            if best is None or n > counts[best]:
                best = ch
        return best

    def contains(self, sub):
        n = len(sub)
        for i in range(len(self.text) - n + 1):
            if self.text[i:i + n] == sub:
                return True
        return False

    def longest_word(self):
        longest = ""
        for word in self.text.split():
            if len(word) > len(longest):
                longest = word
        return longest

    def __len__(self):
        return len(self.text)


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
