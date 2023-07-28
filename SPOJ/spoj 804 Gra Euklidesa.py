import sys

try:
    n = int(input())

    for i in range(n):
        a, b = map(int, input().split())
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        print(a + b)
except:
    sys.exit(0)