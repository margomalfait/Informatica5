# invoer
a = float(input('Geef een getal a groter dan 0: '))
b = float(input('Geef een getal b groter dan 0: '))
c = 'schuine zijde'
from math import sqrt

# berekening
linker_lid = sqrt((a ** 2) + (b ** 2))
rechter_lid = c

# uitvoer
print('{} {} {:.2f} {} {} {:.2f} {} {:.2f}'.format('In een rechthoekige driehoek met rechthoekszijden', 'a =', a, 'en', 'b =', b, 'is de schuine zijde', linker_lid))