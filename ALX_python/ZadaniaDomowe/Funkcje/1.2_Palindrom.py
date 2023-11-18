def is_palindrom(dane: str) -> bool:
    dane = dane.lower()
    nowe_dane = ""
    for el in dane:
        if el.isalpha() or el.isdigit():
            nowe_dane += el
    return nowe_dane == nowe_dane[::-1]


assert is_palindrom("kajak") is True
assert is_palindrom("Kajak") is True
assert is_palindrom("Kobyła ma mały bok") is True
assert is_palindrom("Kobyła, ma mały bok!") is True
assert is_palindrom(
    "Kraksa, gadam jako T. E. Jeż (ordynat) albo jako lokaj oblatany: Drożeje tokaj `Madagaskar', k...!!") is True
assert is_palindrom(
    "Na morzu tłum: tam Iwona, Remus, Adela, drab, Atos, panna, Noe Lizus, baba naga. Fart im. A na morzu"
    " jak? Jula bale. Ula - gong. Nic nad to. Ale paka. A ci na Titanica! A kapela? Ot, dancing. No - Galu."
    " Ela - baluj! Kaju - z Romanami (traf?): Aga, nabab Suzi, Leon, Anna Psota, barda Leda, Sumera nowi, mat 'Muł',"
    " tuz Roman.") is True
