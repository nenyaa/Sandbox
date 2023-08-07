n = int(input())
odczyt = list(map(int, input().split()))
counter = 0
for i in range(n):
    if i == len(odczyt) - 2:
        print(counter)
        break
    elif odczyt[i] < odczyt[i + 1] and odczyt[i + 1] > odczyt[i + 2]:
        counter += 1