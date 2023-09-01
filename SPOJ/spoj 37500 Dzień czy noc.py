w, z, g = input().split()
w = list(map(int, w.split(":")))
z = list(map(int, z.split(":")))
g = list(map(int, g.split(":")))

if g[0] in range(w[0], z[0] + 1):
    if g[0] == w[0] and g[1] < w[1]:
        print("noc")
    elif g[0] == z[0] and g[1] >= z[1]:
        print("noc")
    else:
        print("dzien")
else:
    print("noc")
