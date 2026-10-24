"""
Exercise 2 - String Practice  (SOLUTION)
----------------------------
Fill in each function. Run the file to see PASS/FAIL for each check.
"""


def count_vowels(text):
    """Return how many vowels (a, e, i, o, u, upper or lower case) are in text.

    count_vowels("Hello World") -> 3
    """
    # TODO
    pass


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards, IGNORING
    case, spaces, and punctuation (only letters and digits count).

    is_palindrome("A man, a plan, a canal: Panama!") -> True
    Hint: build a cleaned-up string first with .isalnum() and .lower()
    """
    # TODO
    pass


def capitalize_words(sentence):
    """Return the sentence with the first letter of each word capitalized.
    Don't use .title()!

    capitalize_words("the quick brown fox") -> "The Quick Brown Fox"
    """
    # TODO
    pass


def acronym(phrase):
    """Return the uppercase first letters of each word.

    acronym("portable network graphics") -> "PNG"
    """
    # TODO
    pass


def compress(text):
    """Run-length encoding: replace runs of the same character with char + count.

    compress("aaabccdddd") -> "a3b1c2d4"
    compress("") -> ""
    """
    # TODO
    pass


def caesar_encrypt(message, shift):
    """Shift each LETTER forward in the alphabet by `shift`, wrapping z -> a.
    Keep upper/lower case. Leave non-letters (spaces, punctuation) alone.

    caesar_encrypt("Hello, World!", 3) -> "Khoor, Zruog!"
    Hints: ord("a") is 97, chr(97) is "a". Use % 26 to wrap around.
    """
    # TODO
    pass


def caesar_decrypt(message, shift):
    """Undo caesar_encrypt. (Hint: this can be ONE line using caesar_encrypt!)

    caesar_decrypt("Khoor, Zruog!", 3) -> "Hello, World!"
    """
    # TODO
    pass


# ----------------------- Checks (don't change below) -----------------------
def check(label, actual, expected):
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("count_vowels('Hello World')", count_vowels("Hello World"), 3)
check("count_vowels('AEIOU xyz')", count_vowels("AEIOU xyz"), 5)
check("is_palindrome('racecar')", is_palindrome("racecar"), True)
check("is_palindrome('A man, a plan, a canal: Panama!')", is_palindrome("A man, a plan, a canal: Panama!"), True)
check("is_palindrome('Python')", is_palindrome("Python"), False)
check("capitalize_words('the quick brown fox')", capitalize_words("the quick brown fox"), "The Quick Brown Fox")
check("acronym('portable network graphics')", acronym("portable network graphics"), "PNG")
check("acronym('as soon as possible')", acronym("as soon as possible"), "ASAP")
check("compress('aaabccdddd')", compress("aaabccdddd"), "a3b1c2d4")
check("compress('')", compress(""), "")
check("caesar_encrypt('Hello, World!', 3)", caesar_encrypt("Hello, World!", 3), "Khoor, Zruog!")
check("caesar_encrypt('xyz', 3)", caesar_encrypt("xyz", 3), "abc")
check("caesar_decrypt('Khoor, Zruog!', 3)", caesar_decrypt("Khoor, Zruog!", 3), "Hello, World!")
