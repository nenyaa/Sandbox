n = int(input())
for x in range(n):
    text = input()
    result = ""
    currentLetter = ""
    counter = 0
    for i in range(len(text)):
        if text[i] != currentLetter:
            if counter > 2:
                result += currentLetter + str(counter)
            else:
                for j in range(counter):
                    result += currentLetter
            currentLetter = text[i]
            counter = 0
        if text[i] == currentLetter:
            counter += 1
        if i + 1 == len(text):
            if counter > 2:
                result += currentLetter + str(counter)
            else:
                for j in range(counter):
                    result += currentLetter
    print(result)
