n = int(input())
letters = input().split()
word = input()

result = ""

for letter in word:
    if letter in letters:
        result += letter + letter
    else:
        result += letter
print(result)
