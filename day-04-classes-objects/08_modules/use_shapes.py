"""
08 - Modules (part 2): use_shapes.py
Import code from another file in the SAME folder.
"""

import shapes                              # import the whole module...
from shapes import Circle, total_area      # ...or specific names from it

c = Circle(2)                    # imported directly
r = shapes.Rectangle(3, 4)       # accessed through the module name

print(c, round(c.area(), 2))
print(r, r.area())
print("Total area:", round(total_area([c, r]), 2))

# Notice: the "Testing shapes.py directly..." message did NOT print,
# because inside shapes.py, __name__ is "shapes" (not "__main__") when imported.

# The standard library is full of modules you can import:
import math
import random
print(math.sqrt(16), math.floor(3.7), random.randint(1, 10))
