import sys
import math

i = 1
while i < 100:
    try:
        sign, a, b = input().split()
        a = int(a)
        b = int(b)

        if sign == "+":
            result = a + b
        elif sign == "-":
            result = a - b
        elif sign == "*":
            result = a * b
        elif sign == "/":
            result = a / b
        elif sign == "%":
            result = a % b
        i += 1
        print(math.floor(result))
    except:
        sys.exit(0)
