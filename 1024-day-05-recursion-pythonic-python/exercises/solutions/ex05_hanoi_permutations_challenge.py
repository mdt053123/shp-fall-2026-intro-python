"""
Exercise 5 (CHALLENGE) - Towers of Hanoi and Permutations  (SOLUTION)
---------------------------------------------------------
Two classic problems that are HARD with loops but elegant with recursion.

PART A: Towers of Hanoi
  There are 3 pegs (A, B, C) and n disks stacked on peg A, biggest at the
  bottom. Move all disks to peg C. You may move only one disk at a time, and
  a bigger disk can never sit on a smaller one.

  hanoi(n, source, target, spare) returns a LIST of moves like [("A", "C"), ...]

  The recursive insight: to move n disks from A to C,
    1. move the top n-1 disks from A to B (using C as the spare)
    2. move the biggest disk from A to C
    3. move the n-1 disks from B to C (using A as the spare)

  How many moves does n disks take? Can you find the pattern?

PART B: Permutations
  permutations("abc") -> ["abc", "acb", "bac", "bca", "cab", "cba"]
  (all orderings of the letters, in this order)

  Insight: for each letter, put it first, then add every permutation of
  the REMAINING letters.
"""


def hanoi(n, source="A", target="C", spare="B"):
    if n == 0:
        return []
    moves = hanoi(n - 1, source, spare, target)
    moves.append((source, target))
    moves += hanoi(n - 1, spare, target, source)
    return moves


def permutations(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i in range(len(s)):
        rest = s[:i] + s[i + 1:]
        for p in permutations(rest):
            result.append(s[i] + p)
    return result


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


check("hanoi(1)", lambda: hanoi(1), [("A", "C")])
check("hanoi(2)", lambda: hanoi(2), [("A", "B"), ("A", "C"), ("B", "C")])
check("len(hanoi(3))", lambda: len(hanoi(3)), 7)
check("len(hanoi(10))", lambda: len(hanoi(10)), 1023)
check("permutations('ab')", lambda: permutations("ab"), ["ab", "ba"])
check("permutations('abc')", lambda: permutations("abc"), ["abc", "acb", "bac", "bca", "cab", "cba"])
check("len(permutations('abcde'))", lambda: len(permutations("abcde")), 120)
