"""Solution - Exercise 2: Time Converter"""

total_seconds = int(input("Enter a number of seconds: "))

hours = total_seconds // 3600
leftover = total_seconds % 3600      # seconds that didn't fit into whole hours

minutes = leftover // 60
seconds = leftover % 60

print(f"{total_seconds} seconds is {hours} hours, {minutes} minutes, and {seconds} seconds.")
