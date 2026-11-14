"""
01 - Recursion Basics
A RECURSIVE function calls ITSELF on a smaller version of the problem.

Every recursive function needs:
  1. a BASE CASE: a problem so small you know the answer directly (stops the recursion)
  2. a RECURSIVE CASE: solve a smaller problem, then use its answer
"""


# ---- Countdown: the simplest recursion ----
def countdown(n):
    if n == 0:                 # base case
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)           # recursive case: a SMALLER problem

countdown(3)

print()


# ---- Factorial: n! = n * (n-1)! and 0! = 1 ----
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))            # 5 * 4 * 3 * 2 * 1 = 120

print()


# ---- Watching the CALL STACK ----
# Each call waits for the one below it to finish. We indent by depth to see this.
def factorial_traced(n, depth=0):
    indent = "    " * depth
    print(f"{indent}factorial({n}) called")
    if n == 0:
        print(f"{indent}base case -> 1")
        return 1
    result = n * factorial_traced(n - 1, depth + 1)
    print(f"{indent}factorial({n}) returns {result}")
    return result

factorial_traced(4)

print()


# ---- What happens WITHOUT a base case? ----
def forever(n):
    return forever(n + 1)      # never stops...

try:
    forever(0)
except RecursionError as e:    # (try/except is covered in 07_exceptions.py)
    print("RecursionError:", e)
# Python stops after about 1000 nested calls to protect your computer.


# ---- Recursion vs loops: same result, different style ----
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(10) == factorial_loop(10))
