dictionary = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
              'A': 14}
jasio = 0
stasio = 0
j = input()
for i in j:
    jasio += dictionary[i]
s = input()
for i in s:
    stasio += dictionary[i]
if jasio > stasio:
    print("JASIO")
elif stasio > jasio:
    print("STASIO")
else:
    print("REMIS")
