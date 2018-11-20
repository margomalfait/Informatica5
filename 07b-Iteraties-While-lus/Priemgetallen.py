# invoer
getal = int(input('Geef een getal: '))
k = 2
j = 1

# berekening
while getal > k:
    if (getal % k) == 0:
        antw = '{} is geen priemgetal'.format(getal)
        j = 0
    k += 1
if j and getal != 1:
    antw = '{} is een priemgetal'.format(getal)
elif getal == 1:
    antw = '{} is geen priemgetal'.format(getal)

# uitvoer
print(antw)