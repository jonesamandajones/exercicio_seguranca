

def file_404():
    try:
        file = open('file.txt', 'r')
        file_lines = file.readline()
        file.close()
        
    except FileNotFoundError:
        print(FileNotFoundError, 'O arquivo "file.txt" não foi encontrado.')
        
file_404()