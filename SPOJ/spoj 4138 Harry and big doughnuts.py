n = int(input())
for i in range(n):
    c, k, w = map(int, input().split())
    weight = c * w
    if k >= weight:
        print("yes")
    else:
        print("no")
