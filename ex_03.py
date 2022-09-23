

def teste_input():
    try:
        number = int(input('Digite um número:   '))
        print('O número digitado foi:', number)
    except ValueError:
        print(ValueError, 'Nenhum número válido foi digitado.')
    
teste_input()