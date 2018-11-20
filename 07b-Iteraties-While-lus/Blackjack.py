# invoer
kaart = int(input('kaart is: '))
totaal = 0

# berekening
while totaal < 21 and kaart > 0:
    totaal += kaart
    if totaal < 21:
        kaart = int(input('kaart is: '))

if totaal > 21:
    antw = 'Verbrand ({})'.format(totaal)

if totaal == 21:
    antw = 'Gewonnen!'

if kaart == 0:
    antw = 'Voorzichtig gespeeld ({})'.format(totaal)

# uitvoer
print(antw)