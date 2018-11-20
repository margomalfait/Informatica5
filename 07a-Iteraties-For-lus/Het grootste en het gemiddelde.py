# invoer
aantal_getallen = int(input('aantal getallen: '))
max = int(input('getal: '))
alle_getallen = max

# berekening
for i in range(aantal_getallen - 1):
    getal = int(input('Getal: '))
    if getal > max:
        max = getal
    alle_getallen += getal
    gemiddelde = (alle_getallen / aantal_getallen)

# uitvoer
print('Het grootste getal is ' + str(max) + ' en het gemiddelde is ' + '{:.2f}'.format(gemiddelde))