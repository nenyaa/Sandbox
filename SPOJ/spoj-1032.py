i = int(input())

for item in range(i):
    n, x, y = map(int, input().split())
    wynik = ""
    for a in range(n):
        if a % x == 0 and a % y != 0:
            wynik += str(a) + " "
    wynik = wynik.strip()
    print(wynik)