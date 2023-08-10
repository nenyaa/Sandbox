import sys

try:
    while True:
        data = list(map(float, input().split()))

        max1 = max(data)
        if sum(data) - max1 > max1:
            print("1")
        else:
            print("0")
except:
    sys.exit(0)
