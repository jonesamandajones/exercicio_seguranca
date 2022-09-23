

from unicodedata import name


def name_error():
    try:
        number = int(input('Digite um número:   '))
        print('O número digitado foi:', n)
    except NameError:
        print(NameError, 'Mas o número digitado foi:', number)
name_error()
    