a = input().split()
b = input().split()

c = [i for i in a if i not in b or b.remove(i)]

if len(c) > 0:
    print(len(c))
    for el in sorted(c):
        print(el)
else:
    print(len(c))
