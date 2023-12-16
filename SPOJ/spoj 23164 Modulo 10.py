t = int(input())
for _ in range(t):
    data = input()
    if int(data, 2) % 10 == 0:
        print("Tak")
    else:
        print("Nie")
