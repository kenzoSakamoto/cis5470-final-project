import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

input_str = sys.argv[1]

# Attempting to open a file with the name provided in input
# FileNotFoundError expected for non-existent file names
with open(input_str, 'r') as file:
    data = file.read()

print("passed")
