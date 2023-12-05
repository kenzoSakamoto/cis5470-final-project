import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

# Calculating the modulo of the input string length and using it as a divisor
# ZeroDivisionError expected for inputs of specific lengths
input_mod = len(sys.argv[1]) % 5
result = 30 / input_mod

print("passed")
