import requests

print("### Żarty Chucka Norisa ###\nWskaż jedną z kategorii:")

dane = requests.get("https://api.chucknorris.io/jokes/categories")
x = dane.json()
for i in x:
    print(i, end=" ")
print("")
wybor = input()

zart = requests.get(f"https://api.chucknorris.io/jokes/random?category={wybor}")
zart = zart.json()
print(zart["value"])
