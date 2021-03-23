"""

def lin():
    print ('-'*30)

lin()
print ('CURSO EM VÍDEO')
lin()
print ('APRENDA PYTHON')
lin()
print ('THIARLY CAVALCANTE')
lin()

"""

"""
def soma (a, b, y):
    print (f' A = {a} B = {b}, e Y = {y}')
    s = a + b - y
    print (f'A soma entre A e B menos Y = {s}')


# Programa principal:
soma (2, 4, 6)
soma (5, 6, 6)
soma (6, 9, 6)
"""
"""
def contador (* núm):
    tam = len(núm)
    print (f'Recebi os valores {núm} e são ao todo {tam} números.')


contador (5, 7, 3, 1, 4)
contador (8, 4, 7)
"""
"""
def dobra (lst):
    pos = 0
    while pos < len (lst):
        lst[pos]*=2
        pos+=1

valores = [7, 2, 5, 0, 4]
dobra (valores)
print(valores)
"""
def soma (* valores):
    s = 0
    for num in valores:
        s += num
    print (f'Somando os valores {valores} temos {s}')
soma (5, 2)
soma (2, 9, 4)