"""Solution - Exercise 1: FizzBuzz"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:     # must check "both" FIRST
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
