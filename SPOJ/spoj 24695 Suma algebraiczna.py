n = int(input())

for item in range(n):
    data = input()
    result = ""
    for i in range(len(data)):
        if i == 0 and data[i] == "|":
            result += "("
        elif data[i] != "|":
            result += data[i]
        else:
            if data[i - 1] == "|":
                result += result[i - 1]
            else:
                if data[i - 1] in "+-":
                    result += "("
                else:
                    result += ")"
    print(result)
