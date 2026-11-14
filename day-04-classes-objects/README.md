# Day 4 (Sat 10/17): Classes and Objects

**Big idea:** Everything in Python is an **object**, a bundle of **data** (attributes) plus **behavior** (methods). With `class`, you can design your own types. This is how large programs stay organized.

## Learning goals
- [ ] Explain objects, types, and methods ("everything is an object")
- [ ] Explain references: `==` vs `is`, aliasing, and why mutable objects can change "at a distance"
- [ ] Write a class with `__init__`, attributes, and methods, and explain `self`
- [ ] Use dunder methods: `__str__`, `__repr__`, `__eq__`, `__lt__`, `__len__`, `__getitem__`
- [ ] Use methods to enforce rules (e.g. no negative deposits)
- [ ] Build objects out of other objects (composition)
- [ ] Split code into modules with `import`, and use `if __name__ == "__main__":`
- [ ] (Preview) Explain the basic idea of inheritance

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Warm-up: Day 3 review (dict counting, list patterns), check in on M2 | |
| 0:15 | Everything is an object | `01` |
| 0:25 | References, `==` vs `is`, mutability | `02` |
| 0:45 | Your first class: `__init__`, `self`, methods | `03` |
| 1:05 | *Break* | |
| 1:15 | Dunder methods (Student) | `04` |
| 1:35 | Objects that protect their data (BankAccount) | `05` |
| 1:50 | Composition (Cards → Deck → Hand) | `06` |
| 2:05 | Modules and imports; inheritance preview | `08_modules/`, `07` |
| 2:15 | Exercises / Gradebook M3 | `exercises/`, [project](../gradebook-project/m3-classes/) |

---

## Lecture notes

### 1. Everything is an object (`01`)
`type(x)` tells you an object's **class**. Methods are functions attached to an object: `"hi".upper()`, `lst.append(3)`. Different types have different methods.

### 2. References and mutability (`02`)
A variable **points to** an object; it doesn't contain it.
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a              # c points to the SAME list as a
a == b             # True  (same values)
a is b             # False (different objects)
c.append(4)        # a changes too!
d = a.copy()       # an independent copy
```
- A function that receives a list can **modify the caller's list**.
- Immutable types (int, str, tuple) can't be changed, so aliasing them is harmless.
- ⚠️ `[[0] * 3] * 3` creates 3 references to **one** row.

### 3. Classes (`03`)
```python
class Dog:
    def __init__(self, name, age):   # runs when you write Dog("Rex", 3)
        self.name = name             # attributes live on self
        self.age = age
        self.tricks = []

    def learn(self, trick):          # a method: the first parameter is always self
        self.tricks.append(trick)

rex = Dog("Rex", 3)                  # create an instance
rex.learn("sit")                     # same as Dog.learn(rex, "sit")
```
- **class** = the blueprint (the cookie cutter). **object/instance** = a thing built from it (a cookie).
- **`self`** is "the particular object this method is being called on."

### 4. Dunder ("double underscore") methods (`04`)

| Method | Makes this work |
|--------|-----------------|
| `__init__(self, ...)` | `Student("Ada", 11)` |
| `__str__(self)` | `print(s)`, `str(s)`, f-strings |
| `__repr__(self)` | how the object shows up inside lists and in the shell |
| `__eq__(self, other)` | `s1 == s2` (use `isinstance` to avoid crashing on other types) |
| `__lt__(self, other)` | `s1 < s2`, and therefore `sorted()`, `min()`, `max()` |
| `__len__(self)` | `len(s)` |
| `__getitem__(self, i)` | `s[i]` |
| `__contains__(self, x)` | `x in s` |
| `__add__(self, other)` | `a + b` (see the Fraction exercise) |

⚠️ **Never use a mutable default** like `def __init__(self, scores=[])`. That one list is shared by every object. Use `scores=None`, then `if scores is None: scores = []`.

### 5. Methods enforce rules (`05`)
`account.withdraw(500)` can refuse an overdraft. Code that sets `account.balance -= 500` directly cannot. A **class attribute** (like `interest_rate`) is shared by all instances.

### 6. Composition (`06`)
A `Deck` **has** `Card`s, and a `Hand` **has** `Card`s. Break a big problem into small classes that work together.

### 7. Inheritance (preview) (`07`)
`class Dog(Animal):` means a Dog **is an** Animal. It inherits the parent's methods and can **override** them. `super().__init__(...)` calls the parent's version.

### 8. Modules (`08_modules/`)
Any `.py` file can be imported by another file **in the same folder**:
```python
import shapes                     # use shapes.Circle
from shapes import Circle         # use Circle directly
```
Code under `if __name__ == "__main__":` runs only when you run the file directly, not when it's imported. It's the perfect place for tests.

---

## Common mistakes
- Forgetting `self` as the first parameter, or writing `name` instead of `self.name` inside a method.
- Forgetting the parentheses when calling a method: `s.average` vs `s.average()`.
- Returning nothing from `__str__`. It must **return** a string, not print one.
- Mutable default arguments (see above).
- Confusing the class with an instance: `Student.average()` vs `ada.average()`.

## Key terms

| Term | Meaning |
|------|---------|
| **class** | A blueprint for making objects |
| **object / instance** | One specific thing made from a class |
| **attribute** | Data stored on an object (`self.name`) |
| **method** | A function defined in a class |
| **`self`** | The object a method was called on |
| **constructor / `__init__`** | Sets up a new object's attributes |
| **dunder method** | A special `__method__` that hooks into Python syntax |
| **reference / alias** | A name that points to an object / two names pointing to the same one |
| **composition** | Objects containing other objects ("has-a") |
| **inheritance** | A class that extends another ("is-a") |
| **module** | A `.py` file you can import |

## Exercises → [`exercises/`](exercises/)

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | Rectangle (auto-checked) | methods, `__eq__`, `__lt__`, `__str__` |
| 2 | StringAnalyzer (auto-checked) | wrapping data in a class |
| 3 | Songs and Playlists (auto-checked) | composition |
| 4 | ⭐ Fraction (auto-checked) | operator overloading, Euclid's GCD |
| 5 | Virtual pet | open-ended design and a game loop |

## 📘 Gradebook Project, Milestone 3
Rebuild the gradebook with `Student` and `Gradebook` classes in `gradebook.py`. The menu in `main.py` is written for you and imports your classes.
→ [gradebook-project/m3-classes](../gradebook-project/m3-classes/)

## Videos and reading
1. Classes and instances: https://www.youtube.com/watch?v=ZDa-Z5JzLYM
2. Dunder methods: https://www.youtube.com/watch?v=3ohzBxoFHAY
3. Modules and imports: https://www.youtube.com/watch?v=CqvZ3vGoGs0
4. Official tutorial, "Classes" (sections 9.1–9.5): https://docs.python.org/3/tutorial/classes.html
