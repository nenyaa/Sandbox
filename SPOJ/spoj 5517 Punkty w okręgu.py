import math

xo, yo, r = map(int, input().split())
n = int(input())
for i in range(n):
    xp, yp = map(int, input().split())
    d = math.sqrt((xp - xo) ** 2 + (yp - yo) ** 2)
    if d == r:
        print("E")
    elif d > r:
        print("O")
    else:
        print("I")
