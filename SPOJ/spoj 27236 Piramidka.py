n = int(input())
s = input()
l = int((n - 1) / 2)
for i in range(l + 1):
    print(("." * (l - i) + s[l - i:l + 1 + i] + "." * (l - i)).strip())
