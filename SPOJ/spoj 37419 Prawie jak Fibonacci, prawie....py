n = input()
data = list(map(int, input().split()))

counter = 0
for i in range(len(data) - 2):
    if data[i] + data[i + 1] == data[i + 2]:
        counter += 1
print(counter)
