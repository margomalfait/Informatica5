# invoer
hoeveelheid = int(input('hoeveel basen: '))
soorten = 'ATGC'

# berekening
for i in range(hoeveelheid - 1):
    base = str(input('Base: '))
    if base in soorten:
         soort = base

# uitvoer
print(soort)