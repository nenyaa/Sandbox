def is_prime(m):
    if m == 1:
        return "NIE"
    for i in range(2, m):
        if m % i == 0:
            return "NIE"
    return "TAK"


n = int(input())
for i in range(n):
    x = int(input())
    print(is_prime(x))
