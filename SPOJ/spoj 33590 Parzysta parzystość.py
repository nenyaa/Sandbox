data = int(input())

if data % 2 == 0:
    print("Tak")
else:
    for i in str(data):
        if int(i) % 2 == 0:
            print("Tak")
            break
    else:
        print("Nie")
