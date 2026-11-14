"""
07 - Inheritance (Optional / Preview)
A class can INHERIT from another class: it gets all the parent's attributes and
methods, and can add or override some. Think "a Dog IS AN Animal".
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def introduce(self):
        return f"I'm {self.name} and I say {self.speak()}"


class Dog(Animal):              # Dog inherits from Animal
    def speak(self):            # OVERRIDE the parent's method
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow."


class Puppy(Dog):
    def __init__(self, name, toy):
        super().__init__(name)  # run the parent's __init__ first
        self.toy = toy          # then add something new

    def introduce(self):
        return super().introduce() + f" (and I love my {self.toy})"


pets = [Dog("Rex"), Cat("Tom"), Puppy("Bit", "squeaky bone"), Animal("Mystery")]
for pet in pets:
    print(pet.introduce())     # each object uses ITS OWN version of speak()

print(isinstance(pets[2], Dog), isinstance(pets[2], Animal), isinstance(pets[1], Dog))
