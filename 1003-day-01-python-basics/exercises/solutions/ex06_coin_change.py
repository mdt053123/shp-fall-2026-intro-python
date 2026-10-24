"""Solution - Exercise 6: Coin Change"""

cents = int(input("Amount in cents: "))

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
pennies = cents % 5

print(f"Quarters: {quarters}")
print(f"Dimes:    {dimes}")
print(f"Nickels:  {nickels}")
print(f"Pennies:  {pennies}")
