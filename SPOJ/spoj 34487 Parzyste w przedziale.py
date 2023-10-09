n = int(input())
for item in range(n):
    a, b = map(int, input().split())
    result = ""
    if a % 2 == 0:
        for i in range(a + 2, b, 2):
            result += str(i) + " "
    else:
        for i in range(a + 1, b, 2):
            result += str(i) + " "
    if result != "":
        print(result)
    else:
        print("BRAK")
