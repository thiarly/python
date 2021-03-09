"""
Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.
"""

num = int(input('Digite um número para ver a sua tabuada: '))

for c in range(1, 11):
    #print (c)
    print('\033[32m {} x {:2} = {}\033[m'.format(num, c, num * c))



"""
num = int(input('Digite um número para ver a sua tabuada: '))
print ('{} x {:2} = {}'.format(num, 1, num*1))
print ('{} x {:2} = {}'.format(num, 2, num*2))
print ('{} x {:2} = {}'.format(num, 3, num*3))
print ('{} x {:2} = {}'.format(num, 4, num*4))
print ('{} x {:2} = {}'.format(num, 5, num*5))
print ('{} x {:2} = {}'.format(num, 6, num*6))
print ('{} x {:2} = {}'.format(num, 7, num*7))
print ('{} x {:2} = {}'.format(num, 8, num*8))
print ('{} x {:2} = {}'.format(num, 9, num*9))
print ('{} x {:2} = {}'.format(num, 10, num*10))
"""