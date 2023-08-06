a, b = map(int, input().split())
result = ""
for n in range(a, b + 1):
    if n % 6 == 0:
        result += "ab"
    elif n % 2 == 0 and n % 3 != 0:
        result += "a"
    elif n % 3 == 0 and n % 2 != 0:
        result += "b"
    else:
        continue
print(result)
