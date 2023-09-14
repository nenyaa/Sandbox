n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    h = ((a * b) ** 0.5)
    p = ((a + b) * h) / 2
    print("{:.2f}".format(p))
