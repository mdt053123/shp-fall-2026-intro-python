"""Solution - Exercise 7 (Challenge): Digit Sum"""

n = int(input("Enter a 3-digit number: "))

ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100

print(f"Hundreds digit: {hundreds}")
print(f"Tens digit:     {tens}")
print(f"Ones digit:     {ones}")
print(f"Digit sum:      {hundreds + tens + ones}")

# Bonus: the string way
s = str(n)
print(f"Digit sum (string way): {int(s[0]) + int(s[1]) + int(s[2])}")
