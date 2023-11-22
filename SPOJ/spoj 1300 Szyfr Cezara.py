import sys

for line in sys.stdin:
    line = line.strip()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABC "
    result = ""
    for i in range(len(line)):
        if line[i] in alphabet:
            if line[i] == " ":
                result += " "
            else:
                result += alphabet[alphabet.index(line[i]) + 3]
    print(result)
