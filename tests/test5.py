import sys

# Ensure that an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

input_str = sys.argv[1]

x = 0
y = 2

# This will raise a ZeroDivisionError
z = y / x

print("passed")
