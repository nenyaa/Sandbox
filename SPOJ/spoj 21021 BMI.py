import sys

niedowaga = []
prawidlowa = []
nadwaga = []

n = int(input())

if 1 <= n <= 100:

    for i in range(n):
        imie, waga, wzrost = input().split()
        waga = int(waga)
        wzrost = int(wzrost) / 100
        bmi = waga / (wzrost ** 2)
        if bmi < 18.5:
            niedowaga.append(imie)
        elif 15.5 <= bmi < 25:
            prawidlowa.append(imie)
        else:
            nadwaga.append(imie)

    print(f"niedowaga")
    for x in niedowaga:
        print(x)

    print(f"wartosc prawidlowa")
    for y in prawidlowa:
        print(y)

    print(f"nadwaga")
    for z in nadwaga:
        print(z)
else:
    sys.exit(0)
