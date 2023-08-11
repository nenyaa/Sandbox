r, d = map(float, input().split())

r1_2 = (4 * r ** 2 - d ** 2) / 4
pi = 3.141592654
circ = pi * r1_2

print("{:.2f}".format(circ))
