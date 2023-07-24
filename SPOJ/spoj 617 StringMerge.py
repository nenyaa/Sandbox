def string_merge(a, b):
    line = ""
    if len(a) >= len(b):
        for i in range(len(b)):
            line += a[i] + b[i]
        return ciag
    elif len(a) < len(b):
        for i in range(len(a)):
            line += a[i] + b[i]
        return line


n = int(input())
for i in range(n):
    a, b = input().split()
    print(string_merge(a, b))
