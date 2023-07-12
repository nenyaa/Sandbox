from tkinter import *

kontakty = []


class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email


def dodaj_kontakt():
    imie = entry_Imie.get()
    nazwisko = entry_Nazwisko.get()
    telefon = entry_Telefon.get()
    email = entry_Email.get()
    kontakt = Kontakt(imie, nazwisko, telefon, email)
    kontakty.append(kontakt)
    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)
    entry_Imie.focus()

    lista_kontaktow()


def lista_kontaktow():
    listbox_ListaKontaktow.delete(0, END)
    for i, j in enumerate(kontakty):
        listbox_ListaKontaktow.insert(i, f"{j.imie} {j.nazwisko}")


def pokaz_szczegoly():
    index = listbox_ListaKontaktow.index(ACTIVE)
    label_Imie2wartosc.config(text=kontakty[index].imie)
    label_Nazwisko2wartosc.config(text=kontakty[index].nazwisko)
    label_Telefon2wartosc.config(text=kontakty[index].telefon)
    label_Email2wartosc.config(text=kontakty[index].email)


def usun_kontakt():
    index = listbox_ListaKontaktow.index(ACTIVE)
    kontakty.pop(index)
    lista_kontaktow()


def edytuj_kontakt():
    index = listbox_ListaKontaktow.index(ACTIVE)
    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)

    entry_Imie.insert(0, kontakty[index].imie)
    entry_Nazwisko.insert(0, kontakty[index].nazwisko)
    entry_Telefon.insert(0, kontakty[index].telefon)
    entry_Email.insert(0, kontakty[index].email)

    button_DodajKontakt.config(text="Zmień kontakt", command=lambda: zmien_kontakt(index))


def zmien_kontakt(index):
    imie = entry_Imie.get()
    nazwisko = entry_Nazwisko.get()
    telefon = entry_Telefon.get()
    email = entry_Email.get()

    kontakty[index].imie = imie
    kontakty[index].nazwisko = nazwisko
    kontakty[index].telefon = telefon
    kontakty[index].email = email

    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)

    button_DodajKontakt.config(text="Dodaj kontakt", command=dodaj_kontakt)
    entry_Imie.focus()
    lista_kontaktow()


root = Tk()  # otwiera okienko
root.title("Książka telefoniczna")
root.geometry("700x300")

ramka1 = Frame(root)
ramka2 = Frame(root)
ramka3 = Frame(root)

ramka1.grid(row=0, column=0, padx=20, pady=20)
ramka2.grid(row=0, column=1, sticky=N, pady=20)
ramka3.grid(row=1, column=0, columnspan=2, sticky=W, padx=20)

label_ListaKontaktow = Label(ramka1, text="Lista kontaktów:")
label_ListaKontaktow.grid(row=0, column=0, columnspan=3)
listbox_ListaKontaktow = Listbox(ramka1, width=20, height=7)
listbox_ListaKontaktow.grid(row=1, column=0, columnspan=3)
button_PokazSzczegoly = Button(ramka1, text="Pokaż szczegóły kontaktu", command=pokaz_szczegoly)
button_PokazSzczegoly.grid(row=2, column=0)
button_UsunKontakt = Button(ramka1, text="Usuń kontakt", command=usun_kontakt)
button_UsunKontakt.grid(row=2, column=1)
button_EdytujKontakt = Button(ramka1, text="Edytuj kontakt", command=edytuj_kontakt)
button_EdytujKontakt.grid(row=2, column=2)

label_NowyKontakt = Label(ramka2, text="Nowy Kontakt")
label_NowyKontakt.grid(row=0, column=0, columnspan=2)

label_Imie = Label(ramka2, text="Imie:")
label_Imie.grid(row=1, column=0, sticky=W)
entry_Imie = Entry(ramka2)
entry_Imie.grid(row=1, column=1, sticky=W)
label_Nazwisko = Label(ramka2, text="Nazwisko:")
label_Nazwisko.grid(row=2, column=0, sticky=W)
entry_Nazwisko = Entry(ramka2, width=30)
entry_Nazwisko.grid(row=2, column=1, sticky=W)
label_Telefon = Label(ramka2, text="Telefon:")
label_Telefon.grid(row=3, column=0, sticky=W)
entry_Telefon = Entry(ramka2)
entry_Telefon.grid(row=3, column=1, sticky=W)
label_Email = Label(ramka2, text="Email:")
label_Email.grid(row=4, column=0, sticky=W)
entry_Email = Entry(ramka2)
entry_Email.grid(row=4, column=1, sticky=W)

button_DodajKontakt = Button(ramka2, text="Dodaj kontakt", command=dodaj_kontakt)
# button_DodajKontakt = Button(ramka2, text = "Dodaj Kontakt", command=lambda:test())
# button_DodajKontakt = Button(ramka2, text = "Dodaj Kontakt", command=lambda:test("ALX"))
button_DodajKontakt.grid(row=5, column=0, columnspan=2)

label_SzczegolyKontaltu = Label(ramka3, text='Szczegóły Kontaktu:')
label_SzczegolyKontaltu.grid(row=0, column=0, columnspan=8, sticky=W)

label_Imie2 = Label(ramka3, text="Imię:")
label_Imie2.grid(row=1, column=0)
label_Imie2wartosc = Label(ramka3, width=10, text="...")
label_Imie2wartosc.grid(row=1, column=1)

label_Nazwisko2 = Label(ramka3, text="Nazwisko:")
label_Nazwisko2.grid(row=1, column=2)
label_Nazwisko2wartosc = Label(ramka3, width=10, text="...")
label_Nazwisko2wartosc.grid(row=1, column=3)

label_Telefon2 = Label(ramka3, text="Telefon:")
label_Telefon2.grid(row=1, column=4)
label_Telefon2wartosc = Label(ramka3, width=10, text="...")
label_Telefon2wartosc.grid(row=1, column=5)

label_Email2 = Label(ramka3, text="Email:")
label_Email2.grid(row=1, column=6)
label_Email2wartosc = Label(ramka3, width=10, text="...")
label_Email2wartosc.grid(row=1, column=7)

root.mainloop()
