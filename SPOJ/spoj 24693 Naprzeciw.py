q = int(input())

for i in range(q):
    n, k = map(int, input().split())
    if n % 2 != 0:
        print("BRAK")
    else:
        if k > n / 2:
            print(int(k - n / 2))
        else:
            print(int(k + n / 2))
