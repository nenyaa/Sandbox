from collections import Counter
import sys

numbers = []
for line in sys.stdin:
    numbers.append(line.strip())

count = Counter(numbers)
el1 = count.most_common()[0][1]
el2 = count.most_common()[1][1]

if el1 != el2:
    print(count.most_common()[0][0])
else:
    print("BRAK")
