import math

t = int(input())
for item in range(t):
    n, m = map(int, input().split())
    cookies = 0
    for i in range(n):
        time = int(input())
        cookies += math.floor(86400 / time)
    box = math.ceil(cookies / m)
    print(box)
