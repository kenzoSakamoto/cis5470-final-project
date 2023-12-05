import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

# Convert the input to an integer
# ZeroDivisionError expected when input is '0'
divider = int(sys.argv[1])
result = 100 / divider

print("passed")
