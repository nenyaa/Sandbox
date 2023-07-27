i = int(input())
lista = []
for x in range(i):
    v, v2 = map(int, input().split())
    srednia = (2 * v * v2) / (v + v2)
    srednia = int(srednia)
    lista.append(srednia)
for y in lista:
    print(y)