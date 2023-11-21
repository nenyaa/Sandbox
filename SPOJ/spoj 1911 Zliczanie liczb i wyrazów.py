from sys import stdin

for line in stdin:
    digit = 0
    word = 0
    for i in line.split():
        if i.isalpha():
            word += 1
        else:
            digit += 1
    print(digit, word, end="\n")
