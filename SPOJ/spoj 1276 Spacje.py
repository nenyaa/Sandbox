import sys

for line in sys.stdin:
    line = list(line.split())
    sms = line[0]
    for i in range(1, len(line)):
        sms += line[i][0].upper()+line[i][1:]
    print(sms)
