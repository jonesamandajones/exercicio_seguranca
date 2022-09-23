

def divisão_mn(m, n):
    try:
        resultado = m / n 
    except ZeroDivisionError:
        n = 0
        return print(ZeroDivisionError, 'O número não pode ser dividido por zero.')
    
print(divisão_mn(2,0))