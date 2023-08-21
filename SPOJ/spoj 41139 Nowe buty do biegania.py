k = int(input())
kmil = k / 1.609344
if 0 <= kmil < 300:
    print("NIE")
elif 300 <= kmil < 500:
    print("SPRAWDZIMY TWOJE OBECNE BUTY")
else:
    print("TAK")
