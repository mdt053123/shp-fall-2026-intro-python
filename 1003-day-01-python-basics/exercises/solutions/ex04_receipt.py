"""Solution - Exercise 4: Store Receipt"""

PENCIL_PRICE = 0.75
NOTEBOOK_PRICE = 3.50
BACKPACK_PRICE = 24.99
TAX_RATE = 0.08875

pencils = int(input(f"How many pencils (${PENCIL_PRICE:.2f} each)? "))
notebooks = int(input(f"How many notebooks (${NOTEBOOK_PRICE:.2f} each)? "))
backpacks = int(input(f"How many backpacks (${BACKPACK_PRICE:.2f} each)? "))

pencil_total = pencils * PENCIL_PRICE
notebook_total = notebooks * NOTEBOOK_PRICE
backpack_total = backpacks * BACKPACK_PRICE

subtotal = pencil_total + notebook_total + backpack_total
tax = subtotal * TAX_RATE
total = subtotal + tax

print()
print("========= RECEIPT =========")
print(f"Pencils     x{pencils:<4} ${pencil_total:.2f}")
print(f"Notebooks   x{notebooks:<4} ${notebook_total:.2f}")
print(f"Backpacks   x{backpacks:<4} ${backpack_total:.2f}")
print("---------------------------")
print(f"Subtotal          ${subtotal:.2f}")
print(f"Tax               ${tax:.2f}")
print(f"TOTAL             ${total:.2f}")
print("===========================")
