import sys

# Ensure that an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

input_str = sys.argv[1]

x = 13
z = 21

# Check if the length of the input string is a multiple of 13
if len(input_str) % 13 == 0:
    z = x / 0  # This will raise a ZeroDivisionError

# Check if the length of the input string is greater than 100 and the 26th character is 'a'
if len(input_str) > 100 and input_str[25] == 'a':
    z = x / 0  # This will raise a ZeroDivisionError

print("passed")
