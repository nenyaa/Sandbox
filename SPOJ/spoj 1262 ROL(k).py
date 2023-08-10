n, k = map(int, input().split())
data = list(map(int, input().split()))
result = ""
for i in range(k, n):
    result += str(data[i]) + " "
for j in range(0, k):
    result += str(data[j]) + " "
print(result.strip())
