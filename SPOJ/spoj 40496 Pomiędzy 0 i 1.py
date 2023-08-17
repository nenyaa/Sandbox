data = input()
index0 = data.index("0")
index1 = len(data) - 1 - data[::-1].index("1")
result = data[index0 + 1: index1]
if len(result) != 0:
    print(result)
else:
    print("PUSTY")
