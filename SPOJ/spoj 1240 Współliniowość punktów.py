n = int(input())

for i in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    d = x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2
    if d == 0:
        print("TAK")
    else:
        print("NIE")
