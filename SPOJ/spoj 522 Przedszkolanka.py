import sys
def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a
def nww(a, b):
    return a * b // nwd(a, b)

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a >= 10 and b <= 30:
        print(nww(a, b))
    else:
        sys.exit(0)
