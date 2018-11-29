# invoer
stijn = int(input('snelheid Stijn: '))
kaat = int(input('snelheid Kaat: '))
x = int(input('afstand tussen beide huizen: '))
som = 0
tijd = 0

# berekening
while  x > som:
    som += stijn + kaat
    tijd += 1

# uivoer
print('Na ' + str(tijd) + ' s hebben Stijn en Kaat elkaar ontmoet.')