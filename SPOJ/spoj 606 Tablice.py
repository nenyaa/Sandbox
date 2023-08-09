n = int(input())
result = ""
for i in range(n):
    data = list(map(int, input().split()))
    data.pop(0)
    datanew = data[::-1]
    for j in datanew:
        result += str(j) + " "
    print(result.strip())
    result = ""
