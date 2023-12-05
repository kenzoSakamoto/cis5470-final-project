import sys

# Ensure that an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

input_str = sys.argv[1]

x = 0
y = 2
z = None

# Check if the length of the input string is a multiple of 7
if len(input_str) % 7 == 0:
    z = y / x  # This will raise a ZeroDivisionError

# Check if the length of the input string is a multiple of 13
if len(input_str) % 13 == 0:
    z = y / (x + 1)  # Increment x before division

print("passed")
