import sys

for line in sys.stdin:
    if eval(line):
        print("1")
    else:
        print("0")