getal = int(input('Geef een getal: '))
getal_1, getal_2 = 1, 1

if getal > 2:
    for i in range(3, getal + 1):
        getal_3 = getal_1 + getal_2
        getal_1 = getal_2
        getal_2 = getal_3
    print(getal_3)

elif getal == 1 or getal == 2:
    print('1')

n = int(input('Hoeveelste getal van Fibonacci: '))

vorige, huidige = 1, 1

for i in range(n-2):
    vorige, huidige = huidige, huidige + vorige

print(huidige)