import math

n = int(input())
for x in range(n):
    data = list(map(int, input().split()))
    data.pop(0)
    avarage = sum(data) / len(data)

    min1 = 100
    set1 = set()
    result = ""
    for i in data:
        test = math.fabs(i - avarage)
        if min1 >= test:
            min1 = test
            set1.add(i)
    lista = list(set1)
    for j in lista:
        if j + min1 == avarage or j - min1 == avarage:
            print(j)
            break
