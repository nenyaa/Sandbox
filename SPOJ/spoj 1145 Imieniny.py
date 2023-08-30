n = int(input())

for i in range(n):
    l, c = map(int, input().split())
    l -= 1
    if l == 0:
        print("TAK")
    elif c % l == 0:
        print("NIE")
    else:
        print("TAK")
