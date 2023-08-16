import sys

try:
    while True:
        data = list(map(int, input().split()))
        data.sort()

        if data[0] ** 2 + data[1] ** 2 == data[2] ** 2:
            print("prostokatny")
        elif data[0] ** 2 + data[1] ** 2 > data[2] ** 2:
            print("ostrokatny")
        elif data[0] ** 2 + data[1] ** 2 < data[2] ** 2 and data[2] < data[0] + data[1]:
            print("rozwartokatny")
        else:
            print("brak")
except:
    sys.exit(0)
