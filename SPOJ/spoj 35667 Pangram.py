import sys

text = input()

alphabet = "abcdefghijklmnoprstvwxyz"
i = []
for letter in alphabet:
    if letter in text:
        i.append(text.count(letter))
    else:
        print("NIE")
        sys.exit(0)

average = sum(i) / len(i)
if average == i[0]:
    print("PANGRAM PERFEKCYJNY")
else:
    print("PANGRAM")
