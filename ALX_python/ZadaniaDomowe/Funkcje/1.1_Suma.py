def suma(dane, cast_to_int=False) -> int:
    if isinstance(dane, (list, tuple, set)):
        if cast_to_int:
            nowe_dane = [int(el) for el in str(dane) if el.isdigit()]
            return sum(nowe_dane)
        else:
            nowe_dane = [el for el in dane if isinstance(el, int)]
            return sum(nowe_dane)

    elif isinstance(dane, dict):
        if cast_to_int:
            value_list = [int(value) for value in str(dane.values()) if value.isdigit()]
            return sum(value_list)
        else:
            value_list = [value for value in dane.values() if isinstance(value, int)]
            return sum(value_list)


assert suma((1, 2, 3)) == 6
assert suma((1, "2", 3)) == 4
assert suma([8, 2, 3, 0, 8]) == 21
assert suma([1, 2, "a"]) == 3
assert suma({1: 8, 2: 2, 3: 3, 4: 0, 5: 9}) == 22
assert suma({1: 8, 2: "a", 3: 3, 4: 0, 5: 9}) == 20

assert suma((1, "2", 3), cast_to_int=True) == 6
assert suma([1, 2, "a"], cast_to_int=True) == 3
assert suma({1: "8", 2: "a", 3: 3, 4: 0, 5: 9}, cast_to_int=True) == 20
