n = input()
days = input().split()
counter = 0
for d in days:
    test = days.count(d)
    if test > counter:
        counter = test
print(counter, len(days))
