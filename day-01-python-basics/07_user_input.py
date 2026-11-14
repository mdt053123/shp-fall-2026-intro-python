"""
07 - User Input
input() pauses the program, waits for the user to type, and returns a STRING.
"""

name = input("What is your name? ")
print(f"Nice to meet you, {name}!")

# input() ALWAYS gives back a string, even if the user types a number:
num_text = input("Type a number: ")
print(type(num_text))             # <class 'str'>
print(num_text * 3)               # repeats the TEXT: "555" if you typed 5

# To do math, cast the input to int or float:
num = int(num_text)
print(num * 3)                    # 15 if you typed 5

# Common shortcut: cast right away
height = float(input("Your height in meters? "))
print(f"That's {height * 100:.0f} centimeters.")
