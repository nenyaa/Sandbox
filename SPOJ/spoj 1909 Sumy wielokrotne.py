import sys

try:
    result = 0
    for line in sys.stdin:
        numbers = list(map(int, line.split()))
        numbersSum = sum(numbers)
        result += numbersSum
        print(numbersSum)
    print(result)
except:
    sys.exit(0)
