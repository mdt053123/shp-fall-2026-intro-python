"""
03 - Your First Class
A CLASS is a blueprint. An OBJECT (or INSTANCE) is a thing built from the blueprint.
  class = cookie cutter,  objects = cookies
"""


class Dog:
    """A dog with a name, an age, and some tricks."""

    # __init__ runs automatically when you create a new Dog.
    # 'self' is the specific dog being created.
    def __init__(self, name, age):
        self.name = name          # ATTRIBUTES: data stored on each object
        self.age = age
        self.tricks = []          # every dog starts with no tricks

    # METHODS: functions that belong to the class. The first parameter is always self.
    def bark(self):
        print(f"{self.name} says woof!")

    def learn(self, trick):
        self.tricks.append(trick)

    def human_years(self):
        return self.age * 7

    def describe(self):
        if self.tricks:
            tricks = ", ".join(self.tricks)
        else:
            tricks = "nothing yet"
        return f"{self.name} ({self.age}) knows: {tricks}"


# ---- Create objects (instances) by calling the class like a function ----
rex = Dog("Rex", 3)         # Python calls Dog.__init__(rex, "Rex", 3)
fido = Dog("Fido", 5)

# ---- Each object has its OWN attributes ----
print(rex.name, rex.age)
print(fido.name, fido.age)

# ---- Call methods with dot notation ----
rex.bark()                   # same as Dog.bark(rex)
rex.learn("sit")
rex.learn("roll over")
fido.learn("fetch")

print(rex.describe())
print(fido.describe())
print(f"{rex.name} is {rex.human_years()} in human years")

# ---- Attributes can be changed ----
rex.age += 1
print(rex.describe())

# ---- Without __str__, printing an object isn't very helpful: ----
print(rex)                   # <__main__.Dog object at 0x...>  (fixed in the next file!)
