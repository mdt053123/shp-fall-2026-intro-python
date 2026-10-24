"""
04 - A Student Class with Dunder Methods
"Dunder" = Double UNDERscore. These special methods let your objects work
with Python's built-in syntax: print(), ==, [], len(), <, +, ...
"""


class Student:
    def __init__(self, name, grade_level, scores=None):
        self.name = name
        self.grade_level = grade_level
        # Why not scores=[] as the default? A default list is created ONCE and
        # SHARED by every call -- a famous Python gotcha. None is the safe choice.
        if scores is None:
            scores = []
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def advance(self):
        """Move up a grade level if the average is passing."""
        if self.average() >= 65:
            self.grade_level += 1
            print(f"{self.name} advanced to grade {self.grade_level}!")
        else:
            print(f"{self.name} needs to raise their average first.")

    # ---- Dunder methods ----
    def __str__(self):
        """Called by print() and str(): a friendly description."""
        return f"{self.name} (grade {self.grade_level}, avg {self.average():.1f})"

    def __repr__(self):
        """Called in the shell and inside lists: an unambiguous description."""
        return f"Student({self.name!r}, {self.grade_level}, {self.scores})"

    def __eq__(self, other):
        """Called by ==. Two students are equal if name and grade level match."""
        if not isinstance(other, Student):     # comparing to a non-Student? not equal
            return False
        return self.name == other.name and self.grade_level == other.grade_level

    def __lt__(self, other):
        """Called by <. Lets sorted() and min()/max() compare students by average."""
        return self.average() < other.average()

    def __len__(self):
        """Called by len(): number of scores."""
        return len(self.scores)

    def __getitem__(self, i):
        """Called by student[i]: the i-th score."""
        return self.scores[i]


ada = Student("Ada", 11, [95, 88, 92])
alan = Student("Alan", 12, [72, 60, 81])
ada_copy = Student("Ada", 11)

print(ada)                   # uses __str__
print([ada, alan])           # lists use __repr__
print(ada == ada_copy)       # True  (uses __eq__)
print(ada is ada_copy)       # False (different objects)
print(ada == "Ada")          # False (not a Student -- and no crash!)
print(alan < ada)            # True  (uses __lt__)
print(max([ada, alan]))      # works because of __lt__
print(len(ada), ada[0])      # uses __len__ and __getitem__

print()
alan.add_score(40)
alan.advance()
ada.advance()
