"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
tot = 0
num = int(input('Digite um número: '))

for c in range(1, num +1):
    if num % c == 0:
        print ('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[32m', end=' ')
    print('{}\033[m'.format(c), end=' ')

print ('\nO número \033[35m{}\033[m foi divisível \033[34m{}\033[m vezes.'.format(num, tot))
print (num)

