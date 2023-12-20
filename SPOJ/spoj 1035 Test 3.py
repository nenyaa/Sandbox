lista = []
counter = 0
while True:
    data = int(input())
    lista.append(data)
    print(data)
    if lista[-1] == 42 and len(lista) > 1 and lista[-2] != 42:
        counter += 1
        if counter == 3:
            break
