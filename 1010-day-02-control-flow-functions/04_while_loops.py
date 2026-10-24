"""
04 - While Loops
Repeat a block of code AS LONG AS a condition is True.
Use while when you DON'T know in advance how many times to repeat.
"""

# ---- Basic while loop ----
count = 1
while count <= 5:
    print("count is", count)
    count += 1            # IMPORTANT: update the variable, or it loops forever!
print("Done counting.")

print()

# ---- Countdown ----
n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
print("Liftoff!")

print()

# ---- Loop until a goal is reached: how many years to double your money? ----
money = 1000
years = 0
while money < 2000:
    money *= 1.07         # 7% interest per year
    years += 1
print(f"It takes {years} years to double at 7% interest (${money:.2f}).")

print()

# ---- break: exit the loop immediately ----
n = 1
while True:               # "infinite" loop... until we break out of it
    if n * n > 50:
        break
    n += 1
print("First number whose square is over 50:", n)

print()

# ---- continue: skip the rest of THIS iteration, go to the next ----
floor = 0
while floor < 15:
    floor += 1
    if floor == 13:
        continue          # many buildings skip floor 13!
    print(floor, end=" ")
print()

# ---- DANGER: infinite loops. If you run one, press Stop (Thonny) or Ctrl+C ----
# x = 0
# while x != 7:   # x goes 0, 2, 4, 6, 8, ... never equals 7!
#     x += 2
