def nwd(a, b):
    while b:
        temp = a
        a = b
        b = temp % b
    return a

i = int(input())
for item in range(i):
    a, b = map(int, input().split())
    print(nwd(a,b))
