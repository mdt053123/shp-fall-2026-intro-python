"""
11 - Mad Libs
Collect words from the user, then fill them into a story with a multi-line f-string.
"""

print("Welcome to Mad Libs! Answer the prompts below.\n")

name = input("A name: ")
adjective = input("An adjective: ")
animal = input("An animal: ")
verb = input("A verb ending in -ing: ")
number = int(input("A number: "))
place = input("A place: ")

story = f"""
----------------------------------------
One {adjective} Saturday morning, {name} walked into {place}
and found {number} {animal}s {verb} on the ceiling.
"That's odd," said {name}. "Usually there are only {number - 1}."
----------------------------------------
"""

print(story)
