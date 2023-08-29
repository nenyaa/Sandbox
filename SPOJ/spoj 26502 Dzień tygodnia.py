week = {"Pn": 0, "Wt": 1, "Sr": 2, "Cz": 3, "Pt": 4, "So": 5, "Nd": 6}
n = int(input())
for i in range(n):
    day, nr = input().split()
    nr = int(nr)
    newnr = (week[day] + nr) % 7
    for j in week.items():
        if j[1] == newnr:
            print(j[0])
