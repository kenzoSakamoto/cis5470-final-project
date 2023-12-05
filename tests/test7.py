import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

input_str = sys.argv[1]

# KeyError expected when trying to access a non-existent key in a dictionary
sample_dict = {'key1': 'value1', 'key2': 'value2'}
value = sample_dict[input_str]

print("passed")
