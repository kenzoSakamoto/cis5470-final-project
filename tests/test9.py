import sys

# Ensure an argument is provided
if len(sys.argv) < 2:
    raise ValueError("No input provided")

input_str = sys.argv[1]

# Attempt to parse input as JSON
# JSONDecodeError expected for invalid JSON inputs
import json
data = json.loads(input_str)

print("passed")
