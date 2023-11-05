d = int(input())
for i in range(d):
    n = int(input())
    nlist = map(int, input().split())
    s = 0
    for item in nlist:
        s ^= item
    print(s)

