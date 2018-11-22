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

getal = int(input('getal: '))

# zolang je het niet kan delen door 2, 3, 4 is het allicht een priemgetal

deler = 2

while getal % deler != 0 and getal != 1:
    deler += 1

if deler == getal:
    print('priemgetal')
else:
    print('geen priemgetal')
