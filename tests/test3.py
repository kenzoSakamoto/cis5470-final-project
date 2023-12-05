import sys

# Ensure that an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

input_str = sys.argv[1]

x = 0
y = 2
z = None

# Nested if statements checking the length of the input string
if len(input_str) > 50:
    if len(input_str) > 60:
        if len(input_str) > 70:
            if len(input_str) > 80:
                if len(input_str) > 90:
                    if len(input_str) > 100:
                        if len(input_str) > 110:
                            if len(input_str) > 120:
                                if len(input_str) > 130:
                                    if len(input_str) > 140:
                                        z = y / x  # This will raise a ZeroDivisionError

print("passed")
