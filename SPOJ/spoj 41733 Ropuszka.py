a, b, n = map(int, input().split())

if n == 33:
    print("WRACAJ")
else:
    if a > b:
        print("W PRAWO")
    else:
        print("W LEWO")
