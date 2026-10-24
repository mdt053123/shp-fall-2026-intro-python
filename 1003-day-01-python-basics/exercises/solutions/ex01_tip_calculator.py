"""Solution - Exercise 1: Tip Calculator"""

bill = float(input("Bill amount: $"))
tip_percent = float(input("Tip percent: "))
people = int(input("Number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print(f"Tip:        ${tip:.2f}")
print(f"Total:      ${total:.2f}")
print(f"Per person: ${per_person:.2f}")
