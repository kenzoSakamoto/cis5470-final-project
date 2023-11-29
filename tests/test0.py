import sys

assert len(sys.argv[1]) < 10


a = 1 / (len(sys.argv[1]) - 8)

print("passed")