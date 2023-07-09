sklep = {"chleb": 2.50, "sok": 1.80, "woda": 3.0, "piwo": 5.50}


class Koszyk:

    def __init__(self):
        self.zakupy = {}

    def dodajProdukt(self, nazwa, ilosc):

        if nazwa in self.zakupy:
            self.zakupy[produkt] += ilosc

        else:
            self.zakupy[nazwa] = ilosc

    def usunProdukt(self, nazwa, ilosc):

        if ilosc < self.zakupy[nazwa]:
            self.zakupy[nazwa] -= ilosc

        elif ilosc == self.zakupy[nazwa]:
            self.zakupy.pop(nazwa)

        elif ilosc > self.zakupy[nazwa]:
            print("Błędna ilość")

koszyk = Koszyk()

while True:

    menu = int(input("1-dodaj produkt do koszyka, 2-pokaz zawartosc koszyka, 3-usun produkt z koszyka, 4-kasa/koniec"))

    if menu == 1:

        produkt = input("Podaj nazwe produktu")
        if produkt in sklep:
            ilosc = int(input("Podaj ilosc produktu"))
            koszyk.dodajProdukt(produkt, ilosc)
        else:
            print("Brak produktu w sklepie")

    elif menu == 2:
        for x in koszyk.zakupy:
            print(f"Produkt: {x}, Ilosc: {koszyk.zakupy[x]}")

    elif menu == 3:
        produkt = input("Podaj nazwe produktu")

        if produkt in koszyk.zakupy:
            ilosc = int(input("Podaj ilosc produktu"))
            koszyk.usunProdukt(produkt, ilosc)
        else:
            print("Brak produktu w koszyku")

    elif menu == 4:

        print("--- PARAGON ---")
        suma = 0
        for x in koszyk.zakupy:
            wartosc = koszyk.zakupy[x] * sklep[x]
            suma += wartosc
            print(f"Produkt: {x} Ilosc: {koszyk.zakupy[x]} Cena: {sklep[x]} Wartość {wartosc} ")
        print(f"Razem do zapłaty: {suma}")
        break