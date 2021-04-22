"""
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = (s + n)
print (f'Valor total: {s}')
#print ('Valor total: {}'.format(s))
"""
nome = 'thiarly'
idade = '30'
salário = 987.35
print (f'O {nome} tem {idade} anos e ganha R$ {salário:.2f}')
print (f'O {nome} tem {idade} anos') # -> PYTHON 3.6
print ('O {} tem {} anos'.format(nome, idade)) # -> PYTHON 3
#print ('O %s tem %d anos.' % (nome, idade)) # -> PYTHON 2


"""
n = cont = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont = cont + 1
    s = (s + n)

print (s - 999)
"""

"""
cont = 1
while cont <= 10:
    print (cont,'-> ', end= '')
    cont = cont + 1
print('\033[031mAcabou!\033[m')
"""





"""
enquanto VERDADEIRO
    se 0
        passo
    se 1
        pula
    se moeda
        pega
    se trofeu
        pula
        INTERROMPA
pega
"""
"""
while True:
    if 0 
        passo
    if 1
        pula
    if moeda
        pega
    if trofeu
        pula
        break
pega
"""