#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#... descobrir qual foi o número escolhido pelo computador
#O computador deve escrever na tela se o usuário vencer ou perdeu

import random

s = (random.randint(0,5))

n = int(input('Tente descobrir o número que o computador escolher? '))
print (s)

if n == s:
    print ('Você acertou!')
else:
    print ('Você errou!')

