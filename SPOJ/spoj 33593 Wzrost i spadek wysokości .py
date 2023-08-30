import math

n = int(input())
rise = 0
fall = 0
for i in range(n):
    a, d = map(int, input().split())
    if a > 0:
        rise += math.sin(math.radians(a)) * d
    elif a < 0:
        fall -= math.sin(math.radians(a)) * d
    else:
        continue
print("{:.2f}".format(rise), "{:.2f}".format(fall))
