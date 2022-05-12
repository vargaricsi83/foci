import random
from turtle import st
golok = []

print("1. feladat - Eredméyek:")
print("")
for i in range(5):
    golA = random.randint(0, 5)
    golB = random.randint(0, 5)
    golok.append([golA, golB])
    print("forduló: " + str(golA) + "-" + str(golB))

print("")

osszes = 0

voltDontetlen = False

hGyozelemLista = []
hGyozelem = 0
vGyozelem = 0

legnagyobbGolKulonbseg = [0, 0]

for elem in golok:
    osszes += elem[0]
    osszes += elem[1]
    if elem[0] > elem[1]:
        hGyozelemLista.append(golok.index(elem) + 1)
        hGyozelem += 1
    elif elem[0] < elem[1]:
        vGyozelem += 1
    else:
        voltDontetlen = True
    kulonbseg = 0
    if elem[0] > elem[1]:
        kulonbseg = elem[0] - elem[1]
    else:
        kulonbseg = elem[1] - elem[0]
    if legnagyobbGolKulonbseg[1] > kulonbseg:
        legnagyobbGolKulonbseg[1] = kulonbseg
        legnagyobbGolKulonbseg[0] = golok.index([elem[0], elem[1]])

print("2. feladat")
print("A meccseken átlagosan", osszes / len(golok), "gól született.")

print("")
print("3. feladat")
if hGyozelem > vGyozelem:
    print("A hazai csapat gyözött többször.")
elif hGyozelem < vGyozelem:
    print("A vendég csapat gyözött többször.")
else:
    print("A hazai csapat ugyan annyiszor gyözött, mint a vendég csapat.")

print("")
print("4. feladat")

if voltDontetlen:
    print("Volt döntetlen mérkőzés.")
else:
    print("Nem volt döntetlen mérkőzés.")

print("")
print("5. feladat - Hazai győzelmek:")
for elem in hGyozelemLista:
    print(str(elem) + ". forduló")

print("")
print("6. feladat")
print("A legnagyobb gól különbséget a(z) " + str(legnagyobbGolKulonbseg[0]) + ". fordulóban érték el, ami " + str(legnagyobbGolKulonbseg[1]) + " gól volt.")