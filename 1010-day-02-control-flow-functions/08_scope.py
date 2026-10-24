"""
08 - Scope: Local vs Global Variables
Variables created INSIDE a function only exist inside that function.
"""

# ---- Local variables disappear when the function ends ----
def make_greeting():
    message = "Hi there"     # local to make_greeting
    return message

print(make_greeting())
# print(message)             # NameError: message only existed inside the function

print()

# ---- Parameters are local too. Changing them doesn't change the caller's variable. ----
x = 3

def add_two(x):
    x += 2                   # changes the LOCAL x only
    return x

print(add_two(x))            # 5
print(x)                     # still 3!

print()

# ---- Functions CAN read global variables... ----
TAX_RATE = 0.08875

def with_tax(price):
    return price * (1 + TAX_RATE)

print(f"{with_tax(10):.2f}")

# ---- ...but to CHANGE one, you need the 'global' keyword ----
counter = 0

def increment():
    global counter           # "I mean the counter outside this function"
    counter += 1

increment()
increment()
print(counter)               # 2

# Style tip: avoid 'global' when you can. It's usually cleaner to pass values
# IN as parameters and get results OUT with return:
def incremented(value):
    return value + 1

counter = incremented(counter)
print(counter)               # 3
