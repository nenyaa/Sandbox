result = ""
while True:
    data = list(map(int, input().split()))
    if data != []:
        data = data[::-1]
        for i in data:
            result += str(i) + " "
        print(result.strip())
        result = ""
    else:
        break
