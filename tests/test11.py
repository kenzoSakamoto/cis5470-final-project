import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

# Using the length of the input string as the divisor
# ZeroDivisionError expected for empty string input
input_length = len(sys.argv[1])
result = 50 / input_length

print("passed")
