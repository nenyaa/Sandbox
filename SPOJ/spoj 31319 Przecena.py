n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x = x / 100
    y = y / 100
    result = (x + y - x * y) * 100
    print("{:.2f}".format(result))
