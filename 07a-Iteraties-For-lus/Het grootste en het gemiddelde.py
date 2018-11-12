# invoer
aantal_getallen = int(input('aantal getallen: '))
max = 0
alle_getallen = 0

# berekening
for i in range(aantal_getallen):
    getal = int(input('Getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    alle_getallen += getal
    gemiddelde = (alle_getallen / aantal_getallen)

# uitvoer
print('Het grootste getal is ' + str(max) + ' en het gemiddelde is ' + '{:.2f}'.format(gemiddelde))