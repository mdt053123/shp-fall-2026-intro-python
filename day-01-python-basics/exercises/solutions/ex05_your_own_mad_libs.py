"""Solution - Exercise 5: Your Own Mad Libs (one possible answer)"""

hero = input("A name: ")
food = input("A food (plural): ")
slices = int(input("A number: "))
adjective = input("An adjective: ")
vehicle = input("A vehicle: ")
city = input("A city: ")

story = f"""
{hero} was a {adjective} chef who could eat {slices} {food} in one sitting.
One day, {hero} ate {slices} {food}, then {slices * 2} more, for a total of {slices * 3}!
Feeling {adjective}, {hero} hopped on a {vehicle} and rode all the way to {city}.
"""

print(story)
