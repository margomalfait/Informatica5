# invoer
dv = float(input('verkeersdichtheid vrachtvervoer eerste rijvak: '))
vd = float(input('snelheid vrachtverkeer eerste rijvak: '))
da = float(input('verkeersdichtheid personenvervoer tweede rijvak: '))
va = float(input('snelhied personenwagens tweede rijvak: '))

# berekening
Pv = min(((vd * dv)/40), 1)
Pa = min(((va * da)/40), 1)
a = abs(Pv - Pa)

if min(Pv) >= 0.7 and min(Pa) >= 0.7:
    mes = 'zwart'
elif max(Pv) > 0.7 and max(Pa) > 0.7 and a <= 0.2:
    mes = 'rood'
elif a > 0.7:
    mes = 'geel'
else:
    mes = 'groen'

# uivoer
print(mes)