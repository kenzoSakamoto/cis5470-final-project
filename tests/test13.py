import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

# Decrementing the input length and using it as a divisor
# ZeroDivisionError expected for single character inputs
input_length = len(sys.argv[1]) - 1
result = 10 / input_length

print("passed")
