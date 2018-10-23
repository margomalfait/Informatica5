# input
a = float(input('aantal ogen dobbelsteen 1 van aanvaller: '))
b = float(input('aantal ogen dobbelsteen 2 van aanvaller: '))
c = float(input('aantal ogen dobbelsteen 3 van aanvaller: '))
d = float(input('aantal ogen dobbelsteen 1 van verdediger: '))
e = float(input('aantal ogen dobbelsteen 2 van verdediger: '))

# berekening
f = max(a, b, c)
g = max(d, e)
h = a + b + c - f - min(a, b, c)
i = d + e - g

if f > g and h > i:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')

if f <= g and h <= i:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')

if f <= g and h > i or f > g and h <= i:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')