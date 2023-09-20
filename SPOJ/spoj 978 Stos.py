from sys import stdin

stos = []
for line in stdin:
    if line.strip() == "+":
        n = int(stdin.readline())
        if len(stos) < 10:
            stos.append(n)
            print(":)")
        else:
            print(":(")
    elif line.strip() == "-":
        if len(stos) > 0:
            print(stos.pop(-1))
        else:
            print(":(")
