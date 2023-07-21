import sys

try:
    while True:
        inputs = list(map(int, input().split()))
        number = inputs[0]
        length = inputs[1]

        seek = inputs[1 + length:1:-1]
        x = 0
        for i in seek:
            if i == number:
                x += 1
        print(x)
except:
    sys.exit(0)
