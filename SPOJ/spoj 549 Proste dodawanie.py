i = int(input())
for y in range(i):
    n = int(input())
    liczby = list(map(int, input().split()))
    suma = 0
    for x in liczby:
        suma += x
    print(suma)
