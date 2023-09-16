def dec(n):
    result = 0
    for i in range(len(n)):
        result += int(n[-1 - i]) * 2 ** i
    return result


data = input().split()
print("{}{}:{}{}".format(dec(data[0]), dec(data[1]), dec(data[2]), dec(data[3])))
