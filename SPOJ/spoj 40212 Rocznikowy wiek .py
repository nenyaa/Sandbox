number, year = input().split()
year = int(year)
result = str(((((int(number[-1]) * 2) + 5) * 50) + 1771) - year)
if result[-2] == "0":
    print(result[-1])
else:
    print(result[-2:])