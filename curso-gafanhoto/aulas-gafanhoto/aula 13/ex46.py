"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
 indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep

print ('\033[31m-=\033[m'*30)
print ('\033[33mCONTAGEM REGRESSIVA PARA O ESTOURO DOS FOGOS\033[m')
print ('\033[31m-=\033[m'*30)

for cont in range (10, -1, -1):
    print('\033[32m {} \033[m'.format(cont))
    sleep(1)
print('\033[31mBUM! BUM! ESTOUROU!\033[m')

