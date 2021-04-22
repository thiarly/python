"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando 
o usuário digitar o valor 999, que é a condição de parada. No Final, mostre quantos números
foram digitados e qual foi a soma entre eles.

(Desconsiderando o flag 999)
"""

num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um número: '))
print ('Acabou! Você digitou tantos números: {} e a soma foi {}'.format(cont, soma))

"""
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + num
print ('Acabou! Você digitou tantos números: {} e a soma foi {}'.format(cont -1, soma -999))
"""