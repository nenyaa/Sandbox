data = input()
result = ""

if len(data) % 2 != 0:
    for i in range(0, len(data) + 1, 2):
        result += data[i]
    for i in range(len(data) - 2, 0, -2):
        result += data[i]
else:
    for i in range(0, len(data), 2):
        result += data[i]
    for i in range(len(data) - 1, 0, -2):
        result += data[i]
print(result)
