m16, k16, m36, k36 = map(float, input().split())
lm16, lk16, lm36, lk36 = map(int, input().split())

women = (lk16*k16 + lk36*k36)/(lk16 + lk36)
print("K16K36: {:.2f}".format(women))
men = (lm16*m16 + lm36*m36)/(lm16 + lm36)
print("M16M36: {:.2f}".format(men))
all = (lk16*k16 + lk36*k36 + lm16*m16 + lm36*m36)/(lk16 + lk36 + lm16 + lm36)
print("M16K16M36K36: {:.2f}".format(all))