text = input()
text2 = ""
for i in text:
    if i in "1234567890 ":
        text2 += i
text2 = map(int, text2.split())
print(sum(text2))
