"""
09 - Temperature Converter
A complete small program: input -> calculation -> formatted output.
Formula: C = (F - 32) * 5/9
"""

fahrenheit = float(input("Temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is {celsius:.1f}°C")

# Try: 32 -> 0.0, 212 -> 100.0, 98.6 -> 37.0, -40 -> -40.0
