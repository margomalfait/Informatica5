# invoer
woord = str(input('Verborgen woord: '))
bedrag = int(input('Gedraaide geldbedrag: '))
letter = str(input('Letter: '))
totaal = 0
gegeven_letters = ''

# berekening
while letter in woord and letter not in gegeven_letters:
    totaal += bedrag
    gegeven_letters += letter
    letter = str(input('Letter: '))

if letter not in woord:
    totaal += 0

print(totaal)