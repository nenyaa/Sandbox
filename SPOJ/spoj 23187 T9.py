t = int(input())

dictionary = {"1": "1",
              "2": "2abc",
              "3": "3def",
              "4": "4ghi",
              "5": "5jkl",
              "6": "6mno",
              "7": "7pqrs",
              "8": "8tuv",
              "9": "9wxyz",
              "0": "0"}

for _ in range(t):
    word, number = input().split()
    for i in range(len(word)):
        if word[i].lower() in dictionary[number[i]]:
            if i == len(word) - 1:
                print(f"TAK - {word}")
        else:
            print("NIE")
            break
