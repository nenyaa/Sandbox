a = int(input())
al = list(input().split())
b = int(input())
bl = list(input().split())

suma = sorted(list(set(al + bl)))
sumas = ""
for i in range(len(suma)):
    sumas += suma[i] + " "
print(sumas.strip())

iloczyn = [i for i in al if i in bl]
iloczyn = sorted(list(set(iloczyn)))
iloczyns = ""
if iloczyn != []:
    for i in range(len(iloczyn)):
        iloczyns += iloczyn[i] + " "
    print(iloczyns.strip())
else:
    print("NULL")
