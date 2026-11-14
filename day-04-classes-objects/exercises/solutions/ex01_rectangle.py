"""
Exercise 1 - Rectangle Class  (SOLUTION)
----------------------------
Complete the Rectangle class so every check passes.
Store the sides as self.width and self.height.

  r = Rectangle(3, 4)
  r.area()        -> 12
  r.perimeter()   -> 14
  r.is_square()   -> False
  r.scale(2)      -> makes it 6 x 8 (changes the rectangle; returns nothing)
  str(r)          -> "Rectangle(6 x 8)"
  Rectangle(2, 3) == Rectangle(2, 3)   -> True
  Rectangle(2, 3) == Rectangle(3, 2)   -> True  (same shape, just rotated!)
  Rectangle(2, 3) == "hello"           -> False (don't crash!)
  Rectangle(1, 5) < Rectangle(2, 3)    -> True  (compare by area)
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return sorted([self.width, self.height]) == sorted([other.width, other.height])

    def __lt__(self, other):
        return self.area() < other.area()


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


def scaled(w, h, factor):
    r = Rectangle(w, h)
    r.scale(factor)
    return (r.width, r.height)


check("area", lambda: Rectangle(3, 4).area(), 12)
check("perimeter", lambda: Rectangle(3, 4).perimeter(), 14)
check("is_square (3x4)", lambda: Rectangle(3, 4).is_square(), False)
check("is_square (5x5)", lambda: Rectangle(5, 5).is_square(), True)
check("scale(2)", lambda: scaled(3, 4, 2), (6, 8))
check("str", lambda: str(Rectangle(6, 8)), "Rectangle(6 x 8)")
check("== same", lambda: Rectangle(2, 3) == Rectangle(2, 3), True)
check("== rotated", lambda: Rectangle(2, 3) == Rectangle(3, 2), True)
check("== different", lambda: Rectangle(2, 3) == Rectangle(2, 4), False)
check("== not a rectangle", lambda: Rectangle(2, 3) == "hello", False)
check("< by area", lambda: Rectangle(1, 5) < Rectangle(2, 3), True)
check("max() uses <", lambda: str(max([Rectangle(1, 1), Rectangle(4, 4), Rectangle(2, 3)])), "Rectangle(4 x 4)")
