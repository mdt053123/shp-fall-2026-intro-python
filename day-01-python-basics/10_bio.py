"""
10 - Bio Generator
Combines input, casting, math, and f-strings.
"""

CURRENT_YEAR = 2026   # ALL_CAPS is a convention for values that shouldn't change

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter a hobby: ")
food = input("Enter your favorite food: ")

age = CURRENT_YEAR - birth_year

print()
print("=" * 40)
print(f"  Meet {name}!")
print("=" * 40)
print(f"  Age (roughly): {age}")
print(f"  Loves:         {hobby}")
print(f"  Favorite food: {food}")
print(f"  In 10 years, {name} will be about {age + 10}.")
print("=" * 40)
