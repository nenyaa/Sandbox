n = int(input())
for i in range(n):
    date = input()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counterstart = 0
    counterstop = 27
    for letter in alphabet:
        counterstart += 1
        if letter in date:
            break

    for letter in alphabet[::-1]:
        counterstop -= 1
        if letter in date:
            break

    result = counterstop - counterstart
    print(result)
