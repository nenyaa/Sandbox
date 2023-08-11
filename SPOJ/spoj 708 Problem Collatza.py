n = int(input())

for i in range(n):
    x0 = int(input())
    if x0 != 1:
        if x0 % 2 != 0:
            xn = 3 * x0 + 1
        else:
            xn = x0 / 2
        counter = 1

        while xn != 1:
            if xn % 2 != 0:
                xn = 3 * xn + 1
            else:
                xn = xn / 2
            counter += 1
        print(counter)
    else:
        print("0")
