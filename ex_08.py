



def file_close():
    try: 
        file = open('file.txt', 'r')
        file.write('Exemplo de test.')
    except IOError:
        print('Não foi possível escrever no arquivo.')
    finally:
        file.close()

file_close()

    
