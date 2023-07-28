n = int(input())

for i in range(n):
    l = input()
    sum = int(l[0]) * 1 + int(l[1]) * 3 + int(l[2]) * 7 + int(l[3]) * 9 + int(l[4]) * 1 + int(l[5]) * 3 + int(
        l[6]) * 7 + int(l[7]) * 9 + int(l[8]) * 1 + int(l[9]) * 3 + int(l[10]) * 1
    suml = str(sum)
    if suml[-1] == "0":
        print("D")
    else:
        print("N")
