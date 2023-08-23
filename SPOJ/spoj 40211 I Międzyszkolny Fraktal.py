all = 0
rem = 0
for i in range(4):
    x, y = map(int, input().split())
    all += x
    rem += y
print(all - rem)
