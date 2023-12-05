import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

# Using the ASCII value of the first character of the input as a divisor
# ZeroDivisionError expected for input starting with a null character ('\0')
input_char_value = ord(sys.argv[1][0])
result = 200 / input_char_value

print("passed")
