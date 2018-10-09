# invoer
a = float(input('Geef een getal a tussen 1 en 20: '))
b = float(input('Geef een getal b tussen 1 en 20: '))

# berekening
uitkomst1 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(a, b, (a + b))
uitkomst2 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a * 10), (b * 10), ((a* 10) + (b * 10)))
uitkomst3 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a * 10 ** 2), (b * 10 ** 2), (a * 10 ** 2) + (b * 10 **2))
uitkomst4 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a * 10 ** 3), (b * 10 ** 3)), (a * 10 ** 3) + (b * 10 ** 3)
uitkomst5 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a * 10 ** 4), (b * 10 ** 4)), (a * 10 ** 4) + (b * 10 ** 4)

# uitvoer
print(uitkomst1)
print(uitkomst2)
print(uitkomst3)
print(uitkomst4)
print(uitkomst5)