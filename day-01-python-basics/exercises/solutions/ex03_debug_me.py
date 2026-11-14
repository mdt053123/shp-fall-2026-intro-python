"""Solution - Exercise 3: Debug Me!"""

name = input("Student name: ")                # BUG 1 (SyntaxError): missing closing quote
score1 = int(input("Score 1: "))              # BUG 2 (TypeError later): input wasn't cast to int
score2 = int(input("Score 2: "))
score3 = int(input("Score 3: "))

average = (score1 + score2 + score3) / 3      # BUG 3 (logic error): missing parentheses

print(f"{name}'s average is {average:.2f}")
print(name + "'s highest possible bonus score is " + str(score3 + 90))  # BUG 4 (TypeError): str + int
print(f"{name} is done!")                     # BUG 5 (NameError): typo "nme"
