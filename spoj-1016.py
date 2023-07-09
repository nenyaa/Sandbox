i = int(input())
lista = []
for x in range(i):
    v, v2 = input().split()
    v = int(v)
    v2 = int(v2)
    srednia = (2 * v * v2) / (v + v2)
    srednia = int(srednia)
    lista.append(srednia)
for y in lista:
    print(y)