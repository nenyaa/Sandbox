import sys

try:
    while True:
        a, b, c = map(float, input().split())

        delta = b ** 2 - 4 * a * c

        if delta > 0:
            print("2")
        elif delta == 0:
            print("1")
        else:
            print("0")
except:
    sys.exit(0)
