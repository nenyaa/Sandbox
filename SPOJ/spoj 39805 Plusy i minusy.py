import math

n = input()
plus = n.count("+")
minus = n.count("-")
result = plus - minus
plusstr = ""
minusstr = ""
if result > 2:
    o = math.floor(result / 3)
    for i in range(o):
        plusstr += "5 "
    print(plusstr.strip())
elif result < -2:
    o = math.floor(-result / 3)
    for i in range(o):
        minusstr += "1 "
    print(minusstr.strip())
else:
    print("BRAK")
