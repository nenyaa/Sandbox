text, n = input().split()
text = sorted(text)
result = 0
for i in range(int(n)):
    test = input()
    if len(text) == len(test):
        test = sorted(test)
        if text == test:
            result += 1
print(result)
