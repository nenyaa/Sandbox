n, v1, v2 = map(int, input().split())

v1_ms = v1 * 10 / 36
v2_ms = v2 * 10 / 36
t = n / v1_ms
sdog = v2_ms * t
print("{:.2f}".format(sdog))
