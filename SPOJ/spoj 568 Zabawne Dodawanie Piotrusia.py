import sys

t = int(input())
for i in range(t):
    n = input()
    if int(n) >= 1 and int(n) <= 80:
        counter = 0
        while n[0] != n[-1]:
            n = int(n) + int(n[::-1])
            n = str(n)
            counter += 1
        print(n, counter)
    else:
        sys.exit(0)
