egg = int(input())
if egg >= 1000:
    pay = 1000 * 0.5 + (egg - 1000) * 1
elif 900 <= egg <= 999:
    pay = egg * 0.45
elif 800 <= egg <= 899:
    pay = egg * 0.40
elif 700 <= egg <= 799:
    pay = egg * 0.35
elif 600 <= egg <= 699:
    pay = egg * 0.30
elif 500 <= egg <= 599:
    pay = egg * 0.25
elif 400 <= egg <= 499:
    pay = egg * 0.20
elif 300 <= egg <= 399:
    pay = egg * 0.15
elif 200 <= egg <= 299:
    pay = egg * 0.10
elif 100 <= egg <= 199:
    pay = egg * 0.05
else:
    pay = 0
print("{:.2f}".format(pay))
