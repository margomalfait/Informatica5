gewenste_snelheid = int(input(''))
snelheid_raket = int(input(''))
rem_snelheid = snelheid_raket
aantal_rembewegingen = 0

while rem_snelheid >= gewenste_snelheid:
    rem_snelheid = rem_snelheid - (0.3 * rem_snelheid)
    aantal_rembewegingen += 1

print('na ' + aantal_rembewegingen + ' rembewegingen is de snelheid {:.2f}'.format(rem_snelheid) )