import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

input_str = sys.argv[1]

# Trying to convert input to an integer - ValueError expected for non-integer inputs
input_num = int(input_str)

# Division by the input number - ZeroDivisionError expected for input '0'
result = 10 / input_num

print("passed")
