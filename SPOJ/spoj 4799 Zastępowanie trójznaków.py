import sys

before = ["??=", "??/", "??'", "??(", "??)", "??!", "??<", "??>", "??-"]
after = ["#", "\\", "^", "[", "]", "|", "{", "}", "~"]

for line in sys.stdin:
    for item in before:
        if item in line:
            line = line.replace(item, after[before.index(item)])
    print(line, end="")
