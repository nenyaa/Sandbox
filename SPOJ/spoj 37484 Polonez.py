a, b, c = map(int, input().split())
lista = []
counterk = 0
counterm = 0
for i in range(3):
    names = input().split()
    for name in names:
        if name[-1] == "a":
            counterk += 1
        else:
            counterm += 1
print(min(counterk, counterm))
