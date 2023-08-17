n = int(input())
result = ""
for i in range(n):
    data = input()
    for letter in data:
        if letter in "ABC":
            result += "2"
        elif letter in "DEF":
            result += "3"
        elif letter in "GHI":
            result += "4"
        elif letter in "JKL":
            result += "5"
        elif letter in "MNO":
            result += "6"
        elif letter in "PQRS":
            result += "7"
        elif letter in "TUV":
            result += "8"
        elif letter in "WXYZ":
            result += "9"
    print(result)
    result = ""
