hendel_trekken = input('Trek aan de hendel van de wissel? (ja/nee) ')
man_brug = input('Man van de brug duwen? (ja/nee)')

if hendel_trekken == 'ja' and man_brug == 'nee':
    print('1')

if hendel_trekken == 'ja' and man_brug == 'ja':
    print('2')

if hendel_trekken == 'nee' and man_brug == 'ja':
    print('1')

if hendel_trekken == 'nee' and man_brug == 'nee':
    print('5')