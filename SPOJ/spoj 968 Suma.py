import sys

n = int(input())
suma = n
print(suma)

try:
    while True:
        n = int(input())
        suma += n
        print(suma)
except:
    sys.exit(0)
