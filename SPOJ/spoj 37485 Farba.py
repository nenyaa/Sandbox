import math

a, b, c = map(int, input().split())
walls = 2 * a * c + 2 * b * c
roof = a * b
result = math.ceil(walls / 5) + math.ceil(roof / 3)
print(result)
