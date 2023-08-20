n = int(input())
buildings = set()
for i in range(n):
    x, y = input().split()
    buildings.add(x)
print(len(buildings))
