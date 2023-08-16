data = input().split("_")
result = data[0]
for i in range(1, len(data)):
    result += data[i].capitalize()
print(result)