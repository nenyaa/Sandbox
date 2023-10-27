date = input().replace(" ", "")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphabet:
    count = date.count(i)
    result = round(((count / len(date)) * 100))
    sing = "*"
    print(i + "*" * result)

