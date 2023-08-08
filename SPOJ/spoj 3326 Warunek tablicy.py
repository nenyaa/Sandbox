n = int(input())
l = []
l2 = []
for i in range(n):
    line = int(input())
    l.append(line)
sign, number = input().split()
number = int(number)

for i in l:
    if sign == ">":
        if i > number:
            l2.append(i)
    else:
        if i < number:
            l2.append(i)
for i in l2:
    print(i)
