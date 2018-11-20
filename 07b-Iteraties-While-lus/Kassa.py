prijs = 1
totaal = 0

while prijs > 0:
    prijs = float(input('prijs: '))
    totaal += prijs

print('De totale prijs is € ' + '{:.2f}'.format(totaal))