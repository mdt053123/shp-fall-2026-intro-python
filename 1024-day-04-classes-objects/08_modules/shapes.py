"""
08 - Modules (part 1): shapes.py
Any .py file is a MODULE that other files can import.
This file defines some classes; use_shapes.py imports and uses them.
"""

import math

PI = math.pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def __str__(self):
        return f"Circle(r={self.radius})"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


def total_area(shapes):
    total = 0
    for s in shapes:
        total += s.area()
    return total


# This block runs ONLY when you run shapes.py directly, NOT when it's imported.
# Great for quick tests of the module.
if __name__ == "__main__":
    print("Testing shapes.py directly...")
    print(Circle(1).area(), Rectangle(2, 3).area())
