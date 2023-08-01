import sys

try:
    while True:
        letter, word = input().split()
        newWord = word.replace(letter, "")
        print(newWord)
except:
    sys.exit(0)
