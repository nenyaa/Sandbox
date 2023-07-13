x = int(input())
lista = []
for y in range(x):
    n = int(input())
    if n == 1 or n == 0:
        wynik = "0 1"
    elif n == 2:
        wynik = "0 2"
    elif n == 3:
        wynik = "0 6"
    elif n == 4:
        wynik = "2 4"
    elif n == 5 or n == 6 or n == 8:
        wynik = "2 0"
    elif n == 7:
        wynik = "4 0"
    elif n == 9:
        wynik = "8 0"
    else:
        wynik = "0 0"
    lista.append(wynik)
for y in lista:
    print(y)

