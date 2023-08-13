n = int(input())
for x in range(n):
    data = input().split()
    data.pop(0)
    result = ""
    for i in range(1, len(data), 2):
        result += data[i] + " "
    for j in range(0, len(data), 2):
        result += data[j] + " "
    print(result.strip())
