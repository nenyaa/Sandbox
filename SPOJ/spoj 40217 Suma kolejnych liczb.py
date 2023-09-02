n, s = map(int, input().split())
centre = s / n
result = ""
if n % 2 != 0:
    x = int((n - 1) / 2)
    start = int(centre - x)
    stop = int(centre + x + 1)
    for i in range(start, stop):
        result += str(i) + " "
    print(result.strip())
else:
    x = n / 2 - 1
    start = int(centre - 0.5 - x)
    stop = int(centre + 0.5 + x + 1)
    for i in range(start, stop):
        result += str(i) + " "
    print(result.strip())
