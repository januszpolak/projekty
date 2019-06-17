print('Witaj w przeliczniku miar kg\stones i stones\kg')
print('Co chcesz przeliczyc?:')
print('1:kg-->stones')
print('2:stones-->kg')
odp=int(input('Wpisz 1 lub 2 '))
if odp == 1:
    print('KG-->Stones')
    kg=float(input('Ile ważysz kilogramów? '))
    stones=kg*0.157
    print('Ważysz', stones, 'w angielskiej miarze stone')
elif odp == 2:
    print('Stones-->KG')
    stone=float(input('Ile ważysz w angielskiej miarze stone? '))
    kg=stone/0.157
    print('Ważysz', kg, 'kilogramów')
else:
    print('Błąd')
input('Zakończyć program przelicznik ? Wpisz Y/N ')

