n = int(input())
for i in range(n):
    l = int(input())
    data = list(map(int, input().split()))
    max1 = max(data)
    result = ""
    while max1 in data:
        for number in data:
            if max1 == number:
                result += str(max1) + " "
                data.remove(max1)
    while len(data) != 0:
        min1 = 1000
        for number in data:
            if min1 > number:
                min1 = number
        result += str(min1) + " "
        data.remove(min1)
    print(result.strip())
