from collections import Counter

n = int(input())
dane = ""
for i in range(n):
    dane += input()

dictionary = dict(Counter(dane.replace(" ", "")))
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alphabet:
    if letter in dictionary.keys():
        print(letter, dictionary[letter])
