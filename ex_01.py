import math


def raiz_quadrada(n):
    try:
        raiz = math.sqrt(n)
        return raiz
    except ValueError:
        n<0
        return print(f' ValueError Número menor que 0.')
    
    
print (raiz_quadrada(-1))