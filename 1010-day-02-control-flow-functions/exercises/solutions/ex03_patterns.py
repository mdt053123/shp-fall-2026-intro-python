"""Solution - Exercise 3: Patterns with Nested Loops"""


def print_square(n):
    for row in range(n):
        for col in range(n):
            print("*", end="")
        print()


def print_staircase(n):
    for row in range(1, n + 1):
        spaces = n - row
        print(" " * spaces + "*" * row)


def print_pyramid(n):
    for row in range(1, n + 1):
        spaces = n - row
        stars = 2 * row - 1
        print(" " * spaces + "*" * stars)


def print_checkerboard(n):
    for row in range(n):
        for col in range(n):
            if (row + col) % 2 == 0:
                print("#", end="")
            else:
                print(".", end="")
        print()


print_square(3)
print()
print_staircase(4)
print()
print_pyramid(4)
print()
print_checkerboard(4)
